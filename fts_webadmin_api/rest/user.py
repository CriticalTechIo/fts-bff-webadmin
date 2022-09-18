from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel

class RestRole(BaseModel):
    name: str
    permissions: List[str]

class RestUser(BaseModel):
    id: Optional[UUID]
    email: str
    firstname: str
    lastname: str
    password_hash: Optional[str]
    title: Optional[str]
    organization: Optional[str]
    roles: Optional[List[RestRole]]