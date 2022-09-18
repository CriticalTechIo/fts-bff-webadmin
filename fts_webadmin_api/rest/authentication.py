from pydantic import BaseModel

class RestToken(BaseModel):
    access_token: str
    token_type: str

class RestLoginForm(BaseModel):
    username: str
    password: str