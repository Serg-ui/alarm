from sqlalchemy.orm import relationship
from db.base import Base
import sqlalchemy as sa
from .groups import user_group

friendship = sa.Table("friendship", Base.metadata,
                      sa.Column("user_from", sa.Integer, sa.ForeignKey("users.id"), primary_key=True),
                      sa.Column("user_to", sa.Integer, sa.ForeignKey("users.id"), primary_key=True)
                      )


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(128))
    e_mail = sa.Column(sa.String(255))
    phone = sa.Column(sa.String(50), index=True, unique=True)
    created_at = sa.Column(
        sa.DateTime(), nullable=False, server_default=sa.func.now()
    )

    friends = relationship("User",
                           secondary=friendship,
                           primaryjoin=id == friendship.c.user_from,
                           secondaryjoin=id == friendship.c.user_to,
                           backref="friend",
                           )

    groups_admin = relationship("Groups", back_populates="creator")
    groups = relationship('Groups', secondary=user_group, back_populates='users')

    def list_friends(self):
        friendship_union = sa.select([
            friendship.c.user_from,
            friendship.c.user_to,
        ]).union(
            sa.select([
                friendship.c.user_to,
                friendship.c.user_from, ]
            )
        ).alias()

        User.all_friends = relationship('User',
                                        secondary=friendship_union,
                                        primaryjoin=User.id == friendship_union.c.user_from,
                                        secondaryjoin=User.id == friendship_union.c.user_to,
                                        viewonly=True)
        return self.all_friends
