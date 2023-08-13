from spotify_client import *
import pandas as pd
from tqdm import tqdm

client_id = "aaa4a590d47040aa871244fd2518fa79"
client_secret = "ea20c35dbbd94a66b3ce7712c1519bef"

spotify = SpotifyAPI(client_id, client_secret)

"""
user_id = str(input("Input the username"))

def playlist():
    playlists = spotify.get_user_playlist(_id=user_id)
    for i in playlists['items']:
        print(i['name'],i['id'])
"""
# chosen_playlist = str(input("Copy the playlist ID"))
chosen_playlist = "0UiDVV2N7rsOozwRGm8WbG"
playlist_meta = spotify.get_playlist_items(chosen_playlist)

track_id = []
track_name = []
track_releasedate = []
#print(playlist_meta["items"][0]["track"]["album"]["release_date"])

while True:
    playlist_items = playlist_meta["items"]
    for i in playlist_items:
        track_id.append(i["track"]["id"])
        track_name.append(i["track"]["name"])
        track_releasedate.append(i["track"]["album"]["release_date"][:4])
    playlist_meta = spotify.get_next(playlist_meta["next"])

    if not playlist_meta["next"]:
        playlist_items = playlist_meta["items"]
        for i in playlist_items:
            track_id.append(i["track"]["id"])
            track_name.append(i["track"]["name"])
            track_releasedate.append(i["track"]["album"]["release_date"][:4])
        break

print("total {} songs imported from playlist".format(len(track_id)))

features = ["danceability", "energy"]
danceability = []
energy = []
uri = []


print("Obtaining tracks metadata....")
for i in tqdm(track_id):
    track_features = spotify.get_track_features(i)
    while not track_features:
        track_features = spotify.get_track_features(i)
    danceability.append(track_features["danceability"])
    energy.append(track_features["energy"])
    uri.append(track_features["uri"])

data = pd.DataFrame(
    {
        "name": track_name,
        "id": track_id,
        "release date": track_releasedate,
        "danceability": danceability,
        "energy": energy,
        "uri": uri,
    }
)
csv_name = input("Enter csv name")
data.to_csv(f"{csv_name}.csv")
