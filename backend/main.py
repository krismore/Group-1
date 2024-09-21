from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import requests

Private_Key = "389f67d3-f485-4b8d-8f66-2801c158ae16"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    username: str
    
@app.post('authenticate')
async def authenticate(user: User):
    response = requests.put('https://api.chatengine.io/users/',
    data={
        "username": user.username,
        "password": user.password,
        "first_name": user.username,
    }                        ,
    headers={ "Private-Key": PRIVATE_KEY }
    )
<<<<<<< Tabnine <<<<<<<
return response.json()
>>>>>>> Tabnine >>>>>>># {"conversationId":"9993083c-5f5c-4271-a641-0b541d3429c8","source":"instruct"}


