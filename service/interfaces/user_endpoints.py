import email
from typing import Any, List
from uuid import UUID, uuid4
from fastapi import APIRouter, Body, Depends, HTTPException
from fts_webadmin_api.rest.user import RestUser

router = APIRouter()

@router.post("/user", response_model=RestUser)
def create_user(
    #db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
    input: RestUser
) -> RestUser:
    return RestUser(
        id=uuid4(),
        firstname=input.firstname,
        lastname=input.lastname,
        email=input.email,
        title="Blankmon",
        
    )

@router.get("/user", response_model=List[RestUser])
def get_users(
    #db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> List[RestUser]:
    return [
        RestUser(
        id=uuid4(),
        firstname="Simon",
        lastname="Testtsson",
        email="testmon@teststonm.com",
        title="Blankmon",
        ),
        RestUser(
        id=uuid4(),
        firstname="Merja",
        lastname="Testtsson",
        email="merja@teststonm.com",
        title="Blankmon",
        ),
    
    ]

@router.get("/user/<uuid>", response_model=RestUser)
def get_user(
    #db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
    uuid: UUID
) -> RestUser:
    return RestUser(
        id=uuid,
        firstname="Simon",
        lastname="Testtsson",
        email="testmon@teststonm.com",
        title="Blankmon",
        
    )

@router.put("/user/<uuid>", response_model=RestUser)
def update_user(
    #db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
    uuid: UUID,
    input: RestUser
) -> RestUser:
    return RestUser(
        id=uuid,
        firstname="Simon",
        lastname="Testtsson",
        email="testmon@teststonm.com",
        title="Blankmon",
        
    )
