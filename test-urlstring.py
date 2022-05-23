import requests
payload = {
    "latitude": latitude,
    "longitude": longitude,
    "elevation": elevation,
    "time": current_time,
    "from_date": from_date,
    "to_date": to_date,
}

sun_url = "https://api.astronomyapi.com/api/v2/bodies/positions/sun?', params=payload, auth=("ASTRONOMYAPI_ID", "ASTRONOMYAPI_SECRET")"
print(sun_url)