import requests
import os
from dotenv import load_dotenv

load_dotenv()

URL = os.environ.get('RICK_AND_MORTY_API_URL_CHARACTERS')
STATUS = ("Alive", "Dead", "Unknown")


def get_characters_by_status_of_life():
    try:
        response = requests.request("GET", URL).json()

        print(f"Options status: {STATUS}")
        status_searchable = input("Enter a status: ").capitalize()

        if status_searchable not in STATUS:
            print("Status not found, try again with a valid status")
            return

        for character in response['results']:
            if character['status'] == status_searchable:
                print(f"{character['name']} - {character['status']} - {character['species']} - {character['gender']}")
                print(f"Location: {character['location']['name']}")
                print(f"Origin: {character['origin']['name']}")
                print(f"URL: {character['image']}")

    except IndexError:
        print("Character not found")
