import requests
import json
import os
from dotenv import load_dotenv
load_dotenv('config.env')


def get_location_key(location):
    """
    Searching the AccuWeather location key for a given location name

    Args:
        location: The query string of the location (e.g., "London", "New York")

    Returns:
        The AccuWeather location key (a string) if the location is found, 
        or None if there is an error or the location is not found
    """
    search_url = 'http://dataservice.accuweather.com/locations/v1/search'

    params = {'q': location,
              'apikey': accuweather_token}
    response = requests.get(search_url, params=params)
    try:
        response.raise_for_status()
        if response.json():
            return response.json()[0]['Key']
    except Exception as e:
        print(f'Error: {e}')
        return None


def get_weather_by_location_key(location_key):
    weather_url = f'http://dataservice.accuweather.com/currentconditions/v1/{
        location_key}'
    params = {'apikey': accuweather_token}
    response = requests.get(weather_url, params=params)
    try:
        response.raise_for_status()
        weather_data = response.json()[0]
        return {
            'temperature': weather_data['Temperature']['Metric']['Value'],
            'weather_text': weather_data['WeatherText']
        }
    except Exception as e:
        print(f'Error: {e}')
        return None


if __name__ == '__main__':
    accuweather_token = os.getenv('accuweather_token')
    print(get_weather_by_location_key(get_location_key('London')))
