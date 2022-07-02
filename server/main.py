from fastapi import FastAPI
import httpx
from urllib import request
import requests
from requests.structures import CaseInsensitiveDict
import json

# max_popularity
# min_popularity


app = FastAPI()

genre = "classical"
target_key = 1 # 0 - 11
popularity = 30 # / 100
tempo = 150 # beats per minute

@app.get("/get_categories")
def get_recommendations(genre, target_key, popularity, tempo):
    type = "track"
    
    # url given parameters
    url = f"https://api.spotify.com/v1/recommendations?seed_genres={genre}&target_key={target_key}&target_popularity={popularity}&target_tempo={tempo}&type={type}"

    headers = CaseInsensitiveDict()

    token = 'BQCgRqyY2bN4aHKAPwqkvrB3HMHId4M7eM_9nprphvxyNGUL3fhfU5NkivgD_T5rPRFV6dIADDj1GwBgKWwjxVSUPvO3DahHf6ZM7Q2uZ8yGGkpLtSfFMFCxstgdlw7F9n9rk9aKHpUbg7jhuXf-kFr_of2rgAKNxjWtnxbd4CjU-EfhFbKa865K9JI'
    headers ["Accept"] = "application/json"
    headers ["Authorization"]= f"Bearer {token}"


    response = requests.get(url = url,headers=headers)
    # d = json.loads(response.text)


    print(response.status_code)
    # print("hi")
    # d['tracks'][idx] -> ['album', 'artists', 'available_markets', 'disc_number', 'duration_ms', 'explicit', 'external_ids', 'external_urls', 'href', 'id', 'is_local', 'name', 'popularity', 'preview_url', 'track_number', 'type', 'uri']
    # 
    # print(d['tracks'][6]['href'])
    print(response.text)
    
    
   
get_recommendations(genre, target_key, popularity, tempo)