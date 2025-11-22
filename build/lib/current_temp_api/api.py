import requests
from .base import WeatherAPIBase


class OpenMeteo(WeatherAPIBase):
    def __init__(self, latitude, longitude, **kwargs):
        self.latitude = latitude
        self.longitude = longitude

    def get_current_temperature(self):
        payload = {"latitude": self.latitude, "longitude": self.longitude,
                   "current_weather": True}
        result = requests.get("https://api.open-meteo.com/v1/forecast",
                              params=payload)
        json_result = result.json()
        return json_result["current_weather"]["temperature"]


class OpenWeather(WeatherAPIBase):
    def __init__(self, latitude, longitude, **kwargs):
        super().__init__(latitude, longitude, **kwargs)
        self.latitude = latitude
        self.longitude = longitude
        self.api_token = kwargs.get("api_token")

    def get_current_temperature(self):
        payload = {"lat": self.latitude, "lon": self.longitude,
                   "appid": self.api_token}
        result = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params=payload)
        json_result = result.json()
        return json_result["main"]["temp"]
