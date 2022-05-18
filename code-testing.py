#!/usr/bin/env python3
import requests
import datetime

ASTRONOMYAPI_ID = "<your api id>"
ASTRONOMYAPI_SECRET = "<your api secret key>"


# def get_observer_location():
# Returns the longitude and latitude for the location of this machine.

url = "http://ip-api.com/json?fields=lat,lon"
response = requests.request("GET", url)
response_data = response.json()

print(response_data)

latitude = response_data["lat"]
longitude = response_data["lon"]
print(latitude)
print(longitude)
