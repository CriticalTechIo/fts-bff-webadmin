from fastapi import APIRouter
import service.interfaces.authentication_ctrl


api_router = APIRouter()
api_router.include_router(service.interfaces.authentication_ctrl.router, tags=["login"])