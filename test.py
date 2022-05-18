import requests

response = requests.get("https://api.github.com/events")
# print(response.text)
print(response.status_code)

events = response.json()
print(events[0])
print(events[0]["type"])
print(events[0]["actor"]["display_login"])
