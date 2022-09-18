from fastapi import APIRouter
import service.interfaces.authentication_endpoints
import service.interfaces.user_endpoints


api_router = APIRouter()
api_router.include_router(service.interfaces.authentication_endpoints.router, tags=["Authentication"])
api_router.include_router(service.interfaces.user_endpoints.router, tags=["User"])