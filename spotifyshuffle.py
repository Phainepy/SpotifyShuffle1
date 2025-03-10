#import
from secretcreds import *
import requests
import base64
import spotipy

'''
#Get the Access Token, client credentials flow though. It's too simple. 

def get_access_token(CLIENT_ID, CLIENT_SECRET):
    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_bytes = auth_string.encode("ascii")
    auth_base64 = base64.b64encode(auth_bytes).decode("ascii")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers=headers, data=data)
    json_result = result.json()
    return json_result["access_token"]

access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)


#Make API Requests
def get_artist_info(artist_name, access_token):
    url = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist"
    headers = {"Authorization": f"Bearer {access_token}"}
    result = requests.get(url, headers=headers)
    json_result = result.json()
    return json_result

artist_name = "The Beatles"
artist_info = get_artist_info(artist_name, access_token)
print(artist_info)
'''

from spotipy.oauth2 import SpotifyOAuth

SCOPE = "playlist-read-private playlist-modify-public playlist-modify-private user-library-modify playlist-read-collaborative"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,redirect_uri=redirect_uri,scope=SCOPE))
playlists = sp.current_user_playlists()

for playlist in playlists['items']:
    print (playlist['name'])