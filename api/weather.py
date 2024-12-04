import requests
import os

degree_sign = u'\N{DEGREE SIGN}'

def location_check(location):
    api_key = os.getenv('API_KEY')
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={location}"
    response = requests.get(complete_url)
    return response.json()

def wind_check(degree):
    if degree > 337.5 or degree < 22.5:
        return '- Northerly'
    elif degree > 22.5 and degree < 67.5:
        return '- North Easterly'
    elif degree > 67.5 and degree < 112.5:
        return '- Easterly'
    elif degree > 112.5 and degree < 157.5:
        return '- South Easterly'
    elif degree > 157.5 and degree < 202.5:
        return '- Southerly'
    elif degree > 202.5 and degree < 247.5:
        return '- South Westerly'
    elif degree > 247.5 and degree < 292.5:
        return '- Westerly'
    return '- North Westerly'

def get_weather(location):
    x = location_check(location)
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"] - 273.15
        z = x["weather"]
        weather_description = z[0]["description"]
        w = x["wind"]
        wind_speed = w["speed"]
        wind_deg = w["deg"]
        location = location.capitalize()
        temp_out = f"{current_temperature:.2f}{degree_sign}"
        return location, temp_out, weather_description.capitalize()
    return "City not found", "N/A", ""
