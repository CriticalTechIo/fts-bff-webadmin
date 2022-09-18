from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel
from service.plumbing.db.base_class import Base

class Role(BaseModel):
    name: str
    permissions: List[str]

class User(Base):
    id: UUID
    email: str
    firstname: str
    lastname: str
    password_hash: str
    title: Optional[str]
    organization: Optional[str]
    roles: List[Role]






