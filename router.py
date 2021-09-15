from fastapi import APIRouter
from api.users import router as users_router
from api.groups import router as groups_router

routers = APIRouter()
routers.include_router(users_router.router, prefix='/api/user')
routers.include_router(groups_router.router, prefix='/api/groups')

