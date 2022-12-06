"""
### Application Programming Interface (API) ###

API is a set of commands, functions, protocols and objects 
that programmers can use to create software or interact with an external system.

Your Program >> [Request API] >> External System >> [Response] >> Your Program

HTTP Code:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
https://www.webfx.com/web-development/glossary/http-status-codes/

1xx: Hold On
2xx: Here You Go
3xx: Go away
4xx: You Screwed Up
5xx: I Screwed Up
"""

import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (latitude, longitude)
# print(iss_position)

#----------------------------------------------------------------#

MY_LAT = 18.285540
MY_LONG = 99.512787

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise)
print(sunset)


time_now = datetime.now()

print(time_now.hour)