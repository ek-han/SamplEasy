from lib2to3.pgen2 import token
from fastapi import (
    FastAPI, WebSocket, WebSocketDisconnect, Request, Response)
from typing import List
# import httpx
from urllib import request
import requests
from requests.structures import CaseInsensitiveDict
import json
from chat_utility import *
from typing import List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates



from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# max_popularity
# min_popularity
genre = "classical"
target_key = 1 # 0 - 11
popularity = 30 # / 100
tempo = 150 # beats per minute

templates = Jinja2Templates(directory="templates")


@app.get("/")
def get_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/chat")
def get_chat(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})


@app.get("/api/current_user")
def get_user(request: Request):
    return request.cookies.get("X-Authorization")


class RegisterValidator(BaseModel):
    username: str

    class Config:
        orm_mode = True


@app.post("/api/register")
def register_user(user: RegisterValidator, response: Response):
    response.set_cookie(key="X-Authorization", value=user.username, httponly=True)


class SocketManager:
    def __init__(self):
        self.active_connections: List[(WebSocket, str)] = []

    async def connect(self, websocket: WebSocket, user: str):
        await websocket.accept()
        self.active_connections.append((websocket, user))

    def disconnect(self, websocket: WebSocket, user: str):
        self.active_connections.remove((websocket, user))

    async def broadcast(self, data: dict):
        for connection in self.active_connections:
            await connection[0].send_json(data)


manager = SocketManager()


@app.websocket("/api/chat")
async def chat(websocket: WebSocket):
    sender = websocket.cookies.get("X-Authorization")
    if sender:
        await manager.connect(websocket, sender)
        response = {
            "sender": sender,
            "message": "got connected"
        }
        await manager.broadcast(response)
        try:
            while True:
                data = await websocket.receive_json()
                await manager.broadcast(data)
        except WebSocketDisconnect:
            manager.disconnect(websocket, sender)
            response['message'] = "left"
            await manager.broadcast(response)



# @app.post("/send_message")
# def addMessage(data: Model):
    
#     doc = {
#         message : data.msg,
#         created_at : datetime.datetime.utcnow()
#     }
    
#     msg_coll.insert_one(doc)
    
#     print('hello')
#     return 'world'

# @app.get("/getAllMessages")
# def getAllMessages():
#     docs = msg_coll.find({})
#     return docs


@app.get("/get_recommendations")
def get_recommendations(genre, target_key, popularity, tempo):
    type = "track"
    
    # url given parameters
    url = f"https://api.spotify.com/v1/recommendations?seed_genres={genre}&target_key={target_key}&target_popularity={popularity}&target_tempo={tempo}&type={type}"

    headers = CaseInsensitiveDict()
    
    headers ["Accept"] = "application/json"
    headers ["Authorization"]= f"Bearer <MY_TOKEN>"


    response = requests.get(url = url,headers=headers)
    # d = json.loads(response.text)


    print(response.status_code)
    # print("hi")
    # d['tracks'][idx] -> ['album', 'artists', 'available_markets', 'disc_number', 'duration_ms', 'explicit', 'external_ids', 'external_urls', 'href', 'id', 'is_local', 'name', 'popularity', 'preview_url', 'track_number', 'type', 'uri']
    # 
    # print(d['tracks'][6]['href'])
    print(response.text)
    
