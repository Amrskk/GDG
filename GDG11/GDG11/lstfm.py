import requests

API_KEY = '057c40c0a7c06cea6620e992b25d5c02'

artist_name = input("Artist name: ")

url = f'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={artist_name}&api_key={API_KEY}&format=json'

response = requests.get(url)
data = response.json()

if 'toptracks' in data:
    print(f"\nArtist's top tracks {artist_name}:")
    for track in data['toptracks']['track'][:10]:
        print(f"- {track['name']}")
else:
    print("Error u dumb")
