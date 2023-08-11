from fastapi import APIRouter
from .controllers.todo_controller import router as todo_router
from .controllers.nsfw_controller import router as nsfw_router

routes = APIRouter(prefix="/v1")
_routers = [todo_router, nsfw_router]

for router in _routers:
    routes.include_router(router)
