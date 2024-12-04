import requests
import json
import os
from dotenv import load_dotenv
load_dotenv('config.env')


class Weather:
    def __init__(self, location):
        self.location = location
        self.location_key = self.get_key()

    def get_key(self):
        """
        Searching the AccuWeather location key

        Args:
            location: The query string of the location (e.g., "London", "New York")

        Returns:
            The AccuWeather location key (a string) if the location is found, 
            or None if there is an error or the location is not found
        """
        search_url = 'http://dataservice.accuweather.com/locations/v1/search'

        params = {'q': self.location,
                  'apikey': accuweather_token}
        response = requests.get(search_url, params=params)
        try:
            response.raise_for_status()
            if response.json():
                return response.json()[0]['Key']
        except Exception as e:
            print(f'Error: {e}')
            return None

    def get_current_weather(self):
        weather_url = f'http://dataservice.accuweather.com/currentconditions/v1/{
            self.location_key}'
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
    weather_loc = Weather('London')
    print(weather_loc.get_current_weather())
