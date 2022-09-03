import requests

MY_LAT = 12.991491
MY_LNG = 78.178757

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
}

response = requests.get("https://api.sunrise-sunset.org/json?lat=12.991491&lng=78.178757")
response.raise_for_status()
print(response.json())
