from lib2to3.pgen2 import token
from fastapi import FastAPI
# import httpx
from urllib import request
import requests
from requests.structures import CaseInsensitiveDict
import json
import uvicorn
from chat_utility import *
from pydantic import BaseModel


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

class Model(BaseModel):
    msg: str

@app.post("/send_message")
def addMessage(data: Model):

    doc = {
        message : data.msg,
        created_at : datetime.datetime.utcnow()
    }
    
    msg_coll.insert_one(doc)
    
    print('hello')
    return 'world'

@app.get("/getAllMessages")
def getAllMessages():
    docs = msg_coll.find({})
    return docs


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
    
@app.get("/")
def get_categories():
    return 'hello world'
