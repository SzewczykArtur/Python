# Take top 100 songs in entered date and make a playlist on spotify

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# connect to SPOTIFY
CLIENT_ID = ''
CLIENT_SECRET = ''
URIs = 'http://example.com'
SCOPE = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=SCOPE,
        redirect_uri=URIs,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path='token.txt',
        username='Artur')
)

user_id = sp.current_user()['id']

# Download list with top music
chosen_date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
URL ='https://www.billboard.com/charts/hot-100'
response = requests.get(f'{URL}/{chosen_date}/')
soup = BeautifulSoup(response.text, 'html.parser')
music_data = soup.select('li ul li h3')
songs = [song.getText().strip() for song in music_data]

year = int(chosen_date[0:4])
songs_uri = []
for song in songs:
    result = sp.search(q=f'tracks={song} year={year}', type='track')
    try:
        uri = result['tracks']['items'][0]['uri']
        songs_uri.append(uri)
        print(uri)
    except IndexError:
        print("{song} doesn't exist in Spotify")

# Creates a playlist
playlist_name = f'{chosen_date} Billboard 100'

user_id = sp.current_user()['id']
new_playlist = sp.user_playlist_create(
    user=user_id,
    name=playlist_name,
    public=False,
)
sp.playlist_add_items(playlist_id=new_playlist['id'], items=songs_uri)
