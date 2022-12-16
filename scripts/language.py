import requests

url = "https://ce.judge0.com/languages/"

response = requests.request("GET", url)
response = response.json()

print("Languages supported by Judge0 API:")
print("=================================")

for language in response:
    print(f"{language['name']}")
