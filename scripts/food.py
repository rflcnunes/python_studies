import requests
import os
from dotenv import load_dotenv

load_dotenv()
headers = {
    "X-RapidAPI-Key": os.environ.get('FOOD_API_KEY'),
    "X-RapidAPI-Host": os.environ.get('FOOD_API_HOST')
}
url = os.environ.get('FOOD_API_URL')


def get_food():
    try:
        food = input("Enter a food or a ingredient: ")
        querystring = {"prefix": {food}}

        response = requests.request("GET", url, headers=headers, params=querystring)
        response = response.json()

        for food in response['results']:
            print(food['display'].capitalize())

    except IndexError:
        print("Food not found")
