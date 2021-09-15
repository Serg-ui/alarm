from pydantic import BaseModel


class CreateGroup(BaseModel):
    user_id: int
    group_name: str


class UserToGroup(BaseModel):
    admin_id: int
    group_id: int
    user_id: int
