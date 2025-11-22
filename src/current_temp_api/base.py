from abc import ABC, abstractmethod


class WeatherAPIBase(ABC):
    def __init__(self, latitude, longitude, **kwargs):
        super().__init__()

    @abstractmethod
    def get_current_temperature(self):
        pass
