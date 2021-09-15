from pydantic import BaseModel


class UserScheme(BaseModel):
    id: int
    name: str
    e_mail: str
    phone: str

    class Config:
        orm = True


class CreateUserScheme(BaseModel):
    name: str
    e_mail: str
    phone: str

    class Config:
        orm = True


class MakeFriendsScheme(BaseModel):
    id_user_from: int
    id_user_to: int
