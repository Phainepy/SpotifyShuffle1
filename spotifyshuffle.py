#import
from secretcreds import *
import requests
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth

SCOPE = "playlist-read-private playlist-modify-public playlist-modify-private user-library-modify playlist-read-collaborative"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,redirect_uri=redirect_uri,scope=SCOPE))

playlist_id = "3H9t666C6120bwnUvKzWwe"
results = sp.playlist(playlist_id)
print(json.dumps(results, indent=4))


print("Song - Artist - Album - id\n")

for item in results['tracks']['items']:
    track_id = item['track']['id']
    print(
        item['track']['name'] + ' - ' +
        item['track']['artists'][0]['name'] + ' - ' +
        item['track']['album']['name'] + ' - ' +
        item['track']['id']
    )


#'''
sp.user_playlist_create(user="76zzjj3qikd0y3sw7ulm32jue",name="TrueShuffle",description="Uses Spotify API for creation",public=True,)
sp.user_playlist_add_tracks(user="76zzjj3qikd0y3sw7ulm32jue",playlist_id="0X2mrBCmoTDCU4nv9rjWrl",tracks=my_list_from_string)

#Logic= If playlist called TrueShuffle Exists
#'''