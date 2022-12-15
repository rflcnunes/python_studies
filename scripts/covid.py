import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://covid-193.p.rapidapi.com/history"
today = datetime.date.today()

headers = {
    "X-RapidAPI-Key": os.environ.get('COVID_API_KEY'),
    "X-RapidAPI-Host": os.environ.get('COVID_API_HOST')
}


def get_total_cases():
    try:
        country = input("Enter a country: ")
        date = input("Enter a date (YYYY-MM-DD): ") or today.strftime("%Y-%m-%d")

        print(f"Getting data for {country} on {date}")
        querystring = {"country": {country}, "day": {date}}

        response = requests.request("GET", url, headers=headers, params=querystring)
        response = response.json()

        print(f"Total cases: {response['response'][0]['cases']['total']}")
        print(f"Total deaths: {response['response'][0]['deaths']['total']}")
        print(f"Total recovered: {response['response'][0]['cases']['recovered']}")

    except IndexError:
        print("Country not found")
