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
            accuweather location key(string) if found location,
            or None if there is an error or loc is not found
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

    def get_one_day_forecast(self):
        """Getting the weather forecast for one day

        Returns:
            dict(temp, humidity, wind_speed, rain_chance), or None if error
        """

        weather_url = f'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{
            self.location_key}'
        params = {'apikey': accuweather_token,
                  'details': True,
                  'metric': True}
        response = requests.get(weather_url, params=params)
        try:
            response.raise_for_status()
            if response.json():
                # print(response.json())
                weather_data = response.json()['DailyForecasts'][0]['Day']
                return {
                    'temperature': weather_data['WetBulbTemperature']['Average']['Value'],
                    'wind_speed': weather_data['Wind']['Speed']['Value'],
                    'humidity': weather_data['RelativeHumidity']['Average'],
                    'rain_chance': weather_data['RainProbability']}
        except Exception as e:
            print(f'Error: {e}')
            return None


if __name__ == '__main__':
    accuweather_token = os.getenv('accuweather_token')
    weather_loc = Weather('London')
    print(weather_loc.get_one_day_forecast())
