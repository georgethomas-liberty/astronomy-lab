#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime, date, time, timezone
from pprint import pprint

from_date = date.today()
to_date = date.today()
timenow = datetime.now()
current_time = timenow.strftime("%H:%M:%S")

ASTRONOMYAPI_ID = "0676a500-7552-477c-9610-b4dd6d813f76"
ASTRONOMYAPI_SECRET = "1daa70b3767f42843bf372bed31cbc5aab65ddb3b7ed08ec9e8e8000c81167859d95e6c33fc6c473235c2e6c1c64399248555972d50046e050b073161eef3ba00b0749294b9682d3875e731c8fe23802b5dd0a773a5df6cf4a6687c181372b2f519db82d347f3fc122f1d0f3297ed127"


def get_observer_location():
    # Returns the longitude and latitude for the location of this machine.

    loc_url = "http://ip-api.com/json?fields=lat,lon"
    response = requests.get(loc_url)
    response_data = response.json()

    latitude = response_data["lat"]
    longitude = response_data["lon"]
    # print(latitude)
    # print(longitude

    # NOTE: Replace with your real return values!
    return {latitude}, {longitude}


def get_sun_position(latitude, longitude):
    # Returns the current position of the sun in the sky at the specified location

    sun_response = requests.get(
        "https://api.astronomyapi.com/api/v2/bodies/positions/sun",
        auth=(ASTRONOMYAPI_ID, ASTRONOMYAPI_SECRET),
    )
    print(sun_response.status_code)
    sun_response_data = sun_response.json()
    sun_1 = sun_response_data["data"]["bodies"][0]
    # print(sun_1)

    # Parameters:
    # latitude (str)
    # longitude (str)

    # Returns:
    # float: azimuth
    # float: altitude

    # NOTE: Replace with your real return values!
    return 0, 0


def print_position(azimuth, altitude):
    """Prints the position of the sun in the sky using the supplied coordinates

    Parameters:
    azimuth (float)
    altitude (float)"""

    print("The Sun is currently at: ")


if __name__ == "__main__":
    latitude, longitude = get_observer_location()
    azimuth, altitude = get_sun_position(latitude, longitude)
    print_position(azimuth, altitude)
