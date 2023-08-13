from spotify_client import *
import pandas as pd
from tqdm import tqdm

# https://developer.spotify.com/console

client_id = "aaa4a590d47040aa871244fd2518fa79"
client_secret = "ea20c35dbbd94a66b3ce7712c1519bef"
access_token = "BQA47B_00GzQhFZxShC3kmbtMZdkWCJ_8JzulJq1yFhzhHkF1OPpf-26o21hnSIrRRhQrY1jm7rdEQCB83wrU5ZzNutNQxh51LON8BDME-cbnVFcLnFcsfVth10G9bAfOtwznLIfi4-QTTl14HBBUY4Mo3aoUvpZjs4d-NALfIYkFBDX8LCTZ3jsUHL91bOStCUkkvkf3RJNlA"
user_id = "evan.russel"

spotify = SpotifyAPI(client_id, client_secret)

data = pd.read_csv("I.csv")


def make_playlist():
    playlist = spotify.create_playlist(
        _id=user_id,
        access_token=access_token,
        name="00-15",
        description="2000 - 2015",
    )
    return playlist["id"]


#playlist_id = make_playlist()
playlist_id = '27aBeuogt6h68V0hOOLjxQ'
for i in tqdm(range(len(data))):
    if data["energy"][i] > 0.6:
        spotify.add_playlist_item(
            _id=playlist_id, uri=data["uri"][i], access_token=access_token
        )
