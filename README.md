# Better-Spotify-Shuffle

A simple Python3 script to utilize a psuedorandom shuffle rather than Spotify's shuffle algorithm, which many find faulty.

## Prerequisites
The dependencies can be found in `requirements.txt`
Playback functionality requires a Spotify Premium account
- Spotipy (2.12.0)

## Setup
There is a one-time setup that is required.

Log into the [Spotify developer dashboard](https://developer.spotify.com/dashboard/) and create a new application.

Copy the client ID and client secret into the `CLIENT_ID` and `CLIENT_SECRET` variables, respectively.

`REDIRECT_URI` can be set to anything, example: `http://localhost:8888/callback/'`.  Make sure to add this in the Spotify dashboard at `Edit Settings > Redirect URIs`
