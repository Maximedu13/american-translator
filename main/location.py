import json
import urllib.request

def location():
    """ get the user location """
    with urllib.request.urlopen("https://geolocation-db.com/json") as url:
        data = json.loads(url.read().decode())
    country_code = data["country_code"]
    city = data["city"]
    return country_code, city

def weatherforecast():
    api_key = 'cdbebf7e6d1e1b360be28f616054d54d'
    country_code, city = location()
    with urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + city +',' + country_code + "&appid=" + api_key) as url:
        data = json.loads(url.read().decode())
    return data