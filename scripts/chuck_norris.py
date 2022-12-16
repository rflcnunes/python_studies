import requests

response = requests.request("GET", "https://api.chucknorris.io/jokes/random")
response = response.json()

print("A Chuck Norris joke: ")
print(response['value'])
