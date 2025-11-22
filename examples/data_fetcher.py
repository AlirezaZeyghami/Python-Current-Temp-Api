from current_temp_api.api import OpenMeteo, OpenWeather

latitude = 41.0
longitude = 28.9375

open_meteo_obj = OpenMeteo(latitude, longitude)
temp = open_meteo_obj.get_current_temperature()
print(temp)

open_weather_object = OpenWeather(
    latitude,
    longitude,
    api_token="5b359688084605fad812f1566d0fdc4b")
print(open_weather_object.get_current_temperature())
