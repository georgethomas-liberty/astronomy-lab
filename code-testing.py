#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime, date, time, timezone

from_date = date.today()
to_date = date.today()
timenow = datetime.now()
current_time = timenow.strftime("%H:%M:%S")

ASTRONOMYAPI_ID = "0676a500-7552-477c-9610-b4dd6d813f76"
ASTRONOMYAPI_SECRET = "1daa70b3767f42843bf372bed31cbc5aab65ddb3b7ed08ec9e8e8000c81167859d95e6c33fc6c473235c2e6c1c64399248555972d50046e050b073161eef3ba00b0749294b9682d3875e731c8fe23802b5dd0a773a5df6cf4a6687c181372b2f519db82d347f3fc122f1d0f3297ed127"


# def get_observer_location():
# Returns the longitude and latitude for the location of this machine.

loc_url = "http://ip-api.com/json?fields=lat,lon"
response = requests.get(loc_url)
response_data = response.json()

print(response_data)

latitude = response_data["lat"]
longitude = response_data["lon"]

elev_url = "https://api.open-elevation.com/api/v1/lookup?locations={0},{1}".format(
    latitude, longitude
)
print(elev_url)
elev_response = requests.get(elev_url)
elev_response_data = elev_response.json()
elevation = elev_response_data["results"][0]["elevation"]


print(latitude)
print(longitude)
print(elevation)

payload = {
    "latitude": "latitude",
    "longitude": "longitude",
    "elevation": "elevation",
    "time": "current_time",
    "from_date": "from_date",
    "to_date": "to_date",
}

# sun_url = '"https://api.astronomyapi.com/api/v2/bodies/positions", auth=("ASTRONOMYAPI_ID", "ASTRONOMYAPI_SECRET")'


sun_response = requests.get(
    "https://api.astronomyapi.com/api/v2/bodies/positions/sun",
    auth=(ASTRONOMYAPI_ID, ASTRONOMYAPI_SECRET),
)
print(sun_response.status_code)
sun_response_data = sun_response.json()
sun_1 = sun_response_data["data"]["bodies"][0]
print(sun_1)
