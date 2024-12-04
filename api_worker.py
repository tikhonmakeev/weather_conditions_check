import requests
import json
import os
from dotenv import load_dotenv
load_dotenv('config.env')


accuweather_token = os.getenv('accuweather_token')
search_url = 'http://dataservice.accuweather.com/locations/v1/search?apikey=' + \
    accuweather_token


def get_location_key(location):
    """
    Searching the AccuWeather location key for a given location name

    Args:
        location: The query string of the location (e.g., "London", "New York")

    Returns:
        The AccuWeather location key (a string) if the location is found, 
        or None if there is an error or the location is not found
    """
    params = {'q': location}
    response = requests.get(search_url, params=params)
    try:
        response.raise_for_status()
        if response.json():
            return response.json()[0]['Key']
    except Exception as e:
        print(f'Error: {e}')
        return None


print(get_location_key('seoul'))
