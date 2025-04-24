#import
from secretcreds import *
import requests
import spotipy
import json
import random
from spotipy.oauth2 import SpotifyOAuth

SCOPE = "playlist-read-private playlist-modify-public playlist-modify-private user-library-modify playlist-read-collaborative"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,redirect_uri=redirect_uri,scope=SCOPE))

playlist_id = "3H9t666C6120bwnUvKzWwe"
results = sp.playlist(playlist_id)
print(json.dumps(results, indent=4))

#instantiating An empty list.
my_list_from_string = [] 

print("Song - Artist - Album - id\n")

for item in results['tracks']['items']:
    track_id = item['track']['id']
    my_list_from_string.append (track_id)
    print(
        item['track']['name'] + ' - ' +
        item['track']['artists'][0]['name'] + ' - ' +
        item['track']['album']['name'] + ' - ' +
        item['track']['id']
    )

random.shuffle(my_list_from_string)

#Create the playlist, add tracks to playlist. New PLyalist ID comes from the response.
resp = sp.user_playlist_create(user="76zzjj3qikd0y3sw7ulm32jue",name="TrueShuffle",description="Uses Spotify API for creation",public=True,)
sp.user_playlist_add_tracks(user="76zzjj3qikd0y3sw7ulm32jue",playlist_id= resp["id"] ,tracks=my_list_from_string)
