
from pyowm.owm import OWM
owm = OWM('3a03ca0ebf39d4b08386f513f98f8bfc')
reg = owm.city_id_registry()
mgr = owm.weather_manager()

class classweather:
    def get_weather():
        weather = mgr.weather_at_place('Moscow,RU').weather
        temp_dict_kelvin = weather.temperature()   # a dict in Kelvin units (default when no temperature units provided)
        temp_dict_kelvin['temp_min']
        temp_dict_kelvin['temp_max']    
        temp_dict_celsius = weather.temperature('celsius')['temp']  # guess?
        return temp_dict_celsius
 