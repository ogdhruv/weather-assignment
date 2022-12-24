import requests


def checkweather(city):

    # a utility made for views to get the city's weather data
    # using the open weathermap api then converting it into a readable dictionary.
    
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=9f32194273ba3564f3330c2cda96dc7a"
    w_dataset = requests.get(url.format(city)).json()
    context = {
        "city_name": w_dataset["name"],
        "city_country": w_dataset["sys"]["country"],
        "temp": round(w_dataset["main"]["temp"] - 273.0,2),
        "pressure": w_dataset["main"]["pressure"],
        "humidity": w_dataset["main"]["humidity"],
        "weather": w_dataset["weather"][0]["main"],
        "icon": w_dataset["weather"][0]["icon"],
    }
    return context
