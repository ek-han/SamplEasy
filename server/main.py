from fastapi import FastAPI
import httpx
import spotipy
from spotipy.oauth2 import SpotifyOAuth



app = FastAPI()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="28ffcff09ef14b88883d00d860f4c680",
                                               client_secret="9e206a28d9934fd9812251d25de963f5",
                                               redirect_uri="http://localhost:3000/callback",
                                               scope="user-library-read"))

@app.get("/")
def get_categories():
    top_artists = sp.current_user_followed_artists(limit=20, after=None)
    print(top_artists)


get_categories()

@app.post("/send_message")
def send_message(username, content)
    return (data)