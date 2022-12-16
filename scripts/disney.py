# https://api.disneyapi.dev/character?name=mickey
# https://disneyapi.dev/docs

import requests

character = input("Enter a character: ")
character = character.replace(" ", "%20")

print(f"Getting data for {character}")
url = f"https://api.disneyapi.dev/character?name={character}"

response = requests.request("GET", url)
response = response.json()['data']

for character in response:
    print(character['name'])
