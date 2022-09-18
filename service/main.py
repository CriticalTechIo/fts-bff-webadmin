from fastapi import FastAPI
from service.interfaces.rest_router import api_router
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(api_router)