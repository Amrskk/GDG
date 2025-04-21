import requests

API_KEY = 'eda7d124ed28438c9217948b914fde57'
game_name = input("Game name: ")
url = f"https://api.rawg.io/api/games?key={API_KEY}&search={game_name}"

response = requests.get(url)
data = response.json()

results = data.get('results', [])
if results:
    print(f"\n'{game_name}':\n")
    for game in results[:5]:
        print(f"Name: {game['name']}")
        print(f"Released: {game.get('released', 'N/A')}")
        print(f"Rating: {game.get('rating', 'N/A')}")
        print("---")
else:
    print("No games found bro I am sorry")