from sqlalchemy.orm import relationship
from db.base import Base
import sqlalchemy as sa


user_group = sa.Table("user_group", Base.metadata,
                      sa.Column("user", sa.Integer, sa.ForeignKey("users.id"), primary_key=True),
                      sa.Column("group", sa.Integer, sa.ForeignKey("groups.id"), primary_key=True)
                      )


class Groups(Base):
    __tablename__ = 'groups'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(150))
    creator_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))

    creator = relationship('User', back_populates="groups_admin")
    users = relationship('User', secondary=user_group, back_populates='groups')
