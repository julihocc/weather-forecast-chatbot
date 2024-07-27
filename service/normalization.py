import datetime
from typing import Optional, Tuple
from dotenv import load_dotenv
import os

from pyowm.owm import OWM

load_dotenv()
owm_api_key = os.getenv("OWM_KEY")  # A
assert owm_api_key
print(f"OWM_KEY: {owm_api_key}")

reg = OWM(owm_api_key).city_id_registry()


def text_to_coordinate(text_city: str) -> Tuple[float, float]:
    """parse city name to coordinate

    return latitude, longitude
    """

    list_of_locations = reg.locations_for(text_city)

    # select the first one (maybe incorrect)
    city = list_of_locations[0]

    return city.lat, city.lon


def text_to_date(text_date: str) -> Optional[datetime.date]:
    """convert text based date info into datetime object

    if the convert is not supported, it will return None
    """

    today = datetime.datetime.now()
    one_more_day = datetime.timedelta(days=1)

    if text_date == "hoy":
        return today.date()
    if text_date == "mañana":
        return (today + one_more_day).date()
    if text_date == "pasado mañana":
        return (today + one_more_day * 2).date()

    # not supported
    if text_date in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]:
        return None

    # not supported
    if text_date in ["ayer", "anteayer"]:
        return None

    # anything else
    return None