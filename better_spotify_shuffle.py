'''
Shuffles a given playlist using a pseudorandom shuffle rather than
Spotify's built-in shuffle feature
'''
import sys
import random

import spotipy
import spotipy.util as util

################## - DEFINE CLIENT - ##################
CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = 'http://localhost:8888/callback/'
#######################################################

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Whoops, need your username!")
    print("usage: python user_playlists.py [username]")
    sys.exit()


SCOPE = 'user-read-playback-state streaming playlist-read-collaborative user-modify-playback-state \
    user-read-currently-playing playlist-read-private user-library-read'

token = util.prompt_for_user_token(username, SCOPE, client_id=CLIENT_ID, \
    client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)

if token:
    sp = spotipy.Spotify(auth=token)
    device = None
    #Determine which device to play on
    for d in sp.devices()['devices']:
        if d['is_active']:
            device = d
    if not device:
        print("No device found")
        sys.exit()
    #Find user's playlists and display
    playlists = sp.user_playlists(username)
    for i, playlist in enumerate(playlists['items']):
        print(i+1, '.', playlist['name'])
    selected = int(input("Select a playlist by number: "))
    print("Queuing songs...")
    results = sp.playlist(playlists['items'][selected-1]['id'], fields="tracks,next")['tracks']['items']
    random.shuffle(results)
    for i, item in enumerate(results):
        track = item['track']
        if i == 0:
            sp.start_playback(device_id=device['id'], uris=[track['uri']])
        else:
            sp.add_to_queue(uri=track['uri'], device_id=device['id'])
    print("Done!")
else:
    print("Can't get token for", username)
