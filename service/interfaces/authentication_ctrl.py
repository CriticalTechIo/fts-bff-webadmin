from typing import Any
from fastapi import APIRouter, Body, Depends, HTTPException
from fts_webadmin_api.rest import authentication

router = APIRouter()


@router.post("/login/access-token", response_model=authentication.Token)
def login_access_token(
    #db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    return "accesstoken"
    # user = crud.user.authenticate(
    #     db, email=form_data.username, password=form_data.password
    # )
    # if not user:
    #     raise HTTPException(status_code=400, detail="Incorrect email or password")
    # elif not crud.user.is_active(user):
    #     raise HTTPException(status_code=400, detail="Inactive user")
    # access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    # return {
    #     "access_token": security.create_access_token(
    #         user.id, expires_delta=access_token_expires
    #     ),
    #     "token_type": "bearer",
    # }