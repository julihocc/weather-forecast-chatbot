from pyowm.owm import OWM
import os
from dotenv import load_dotenv


load_dotenv()
owm_api_key = os.getenv("OWM_KEY")  # A
assert owm_api_key
print(f"OWM_KEY: {owm_api_key}")

owm = OWM(owm_api_key)
mgr = owm.weather_manager()

config_dict = owm.configuration
print(config_dict)

reg = owm.city_id_registry()
list_of_tuples = london = reg.ids_for('London', matching='like')
print(list_of_tuples)  

one_call = mgr.one_call(lat=52.5244, lon=13.4105)

one_call.forecast_daily[0].temperature('celsius').get('feels_like_morn', None)