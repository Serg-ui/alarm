from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session, joinedload

from utils import get_db
from db.models.user import User
from api.users.schemas import CreateUserScheme, MakeFriendsScheme


router = APIRouter()


@router.get(path='/all')
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.get(path='/')
def get_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user = db.query(User).options(joinedload(User.groups)).filter_by(id=user_id).one()
        user.list_friends()
    except NoResultFound:
        raise HTTPException(404, "Такого юзера нет")
    return user


@router.post(path='/')
def create_user(new_user: CreateUserScheme, db: Session = Depends(get_db)):
    user = User(**new_user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@router.put(path='/')
def make_friendship(users: MakeFriendsScheme, db: Session = Depends(get_db)):
    user_from = db.query(User).filter_by(id=users.id_user_from).one()
    user_to = db.query(User).filter_by(id=users.id_user_to).one()

    user_from.friends.append(user_to)

    db.add(user_from)
    db.commit()

    return user_from.list_friends()
