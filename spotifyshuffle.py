#initial variables

redirect_uri = "http://localhost:4202"

# URLS
AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'

#defining variables for the Rest Call.
SCOPE = "playlist-read-private playlist-modify-public playlist-modify-private user-library-modify"

import requests

auth_code = requests.get (AUTH_URL,{
    'client_id' : CLIENT_ID,
    'response_type' : 'code',
    'scope' : SCOPE,
})
print(auth_code)

auth_header = base64.urlsafe_b64encode((CLIENT_ID + ':' + CLIENT_SECRET).encode())
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic %s' % auth_header.decode('ascii')
}

payload = {
    'grant_type': 'authorization_code',
    'code': auth_code,
    'redirect_uri': 'https://open.spotify.com/collection/playlists',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
}