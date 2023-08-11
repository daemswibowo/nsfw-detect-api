from fastapi import APIRouter
from .controllers.nsfw_controller import router as nsfw_router

routes = APIRouter(prefix="/v1")
_routers = [nsfw_router]

for router in _routers:
    routes.include_router(router)
