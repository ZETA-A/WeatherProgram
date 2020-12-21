import os
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

print("===========================================================")

print("[Information] Loading API...")

print("===========================================================")



config_dict = get_default_config()

config_dict['language'] = 'en'



owm = OWM('APIKEY', config_dict)



mgr = owm.weather_manager()

observation = mgr.weather_at_place('Seoul,KR') #Here type live your city

weather = observation.weather

weather.status



print("===========================================================")

print("[Information] API load succeed.")

print("===========================================================")


print("Today weather is")

print(weather.status)



mgr = owm.weather_manager()

weather = mgr.weather_at_place('Seoul,KR').weather

temp_dict_kelvin = weather.temperature()

temp_dict_kelvin['temp_min']

temp_dict_kelvin['temp_max']

temp_dict_kelvin = weather.temperature('celsius')



print("The minimum temperature")

print(temp_dict_kelvin['temp_min'])

print("The highest temperature")

print(temp_dict_kelvin['temp_max'])
