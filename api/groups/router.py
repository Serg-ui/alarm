from fastapi import APIRouter, Depends
from utils import get_db
from sqlalchemy.orm import Session, joinedload
from db.models import User, Groups
from api.groups.schemas import CreateGroup, UserToGroup


router = APIRouter()

@router.get(path='/all')
def get_all_groups(db: Session = Depends(get_db)):
    return db.query(Groups).all()


@router.get(path='/')
def get_group(group_id: int, db: Session = Depends(get_db)):
    group = db.query(Groups).options(joinedload(Groups.users)).filter_by(id=group_id).one()
    return group


@router.post(path='/')
def create_group(data: CreateGroup, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(id=data.user_id).one()
    group = Groups(name=data.group_name)
    user.groups_admin = [group]
    user.groups.append(group)
    db.add(user)
    db.commit()
    db.refresh(group)

    return group


@router.put(path='/')
def add_user_to_group(data: UserToGroup, db: Session = Depends(get_db)):
    group = db.query(Groups).filter_by(id=data.group_id).one()
    if group.creator_id == data.admin_id:
        user = db.query(User).filter_by(id=data.user_id).one()
        group.users.append(user)
        db.commit()
        return True
    return {'error': 'admin_id is not admin for this group'}

