import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_username = '314qj4l3bfwgio7no4axtg4hvqlm'
clientId = 'b3c01351e96a4d4c9d09fa5e786f1a05'
clientSecret = '07cfb26d649a4be6868caf5ce27dbf6b'
redirect_url = 'http://google.com/callback/ '

get = SpotifyClientCredentials(clientId,clientSecret,redirect_url)
sp = spotipy.Spotify(auth_manager=get)