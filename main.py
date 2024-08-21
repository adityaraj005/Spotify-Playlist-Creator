from bs4 import BeautifulSoup
import spotipy
import requests
from spotipy.oauth2 import SpotifyOAuth
import os

USER_CLIENT_ID = os.environ.get("USER_CLIENT_ID")
USER_CLIENT_SECRET = os.environ.get("USER_CLIENT_SECRET")
USER_URI = os.environ.get("USER_URI")


# ----------------SCRAPING WEBSITE--------------------------

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all(name="h3", class_="a-no-trucate")

song_names = [song.getText().strip() for song in song_names_spans]

songs = ["".join(song_name) for song_name in song_names]  # this is the list of songs. Which we want to search and add
# inside spotify playlist.

# ------------------SPOTIFY URIS----------------------------

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=USER_CLIENT_ID, client_secret=USER_CLIENT_SECRET,
                                               redirect_uri=USER_URI,
                                               scope="playlist-modify-private"))
result1 = sp.current_user()

USER_ID = result1["id"]

song_uries = []

for song in songs:
    result2 = sp.search(song)  # this will search songs in spotify.

    try:
        song_uries.append(result2['tracks']['items'][0]['uri'])

    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


# ------------------CREATING PLAYLIST---------------------------

result3 = sp.user_playlist_create(user=USER_ID, public=False, name=f"{date} Billboard 100")

PLAYLIST_ID = result3['id']

sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=song_uries)
