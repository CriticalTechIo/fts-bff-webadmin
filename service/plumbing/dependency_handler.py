

from typing import Generator
from service.plumbing.db.session import SessionLocal
from service.services.authentication_service import AuthenticationService
import logging

logger = logging.getLogger("FTSBFF")

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def get_user_service():
    pass

def get_authentication_service()->AuthenticationService:
    return AuthenticationService(get_db, logger)