import requests
import os
import json

URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
KEY = os.environ.get("API_KEY")


def get_weather() -> None:

    result_from_weather_api = requests.get(URL + f"q={FILTERING}&key={KEY}")

    weather_dict = json.loads(result_from_weather_api.text)

    print(f"Performing request to Weather API for city {FILTERING}...")
    print(
        f"{FILTERING}/{weather_dict['location']['country']}"
        f" {weather_dict['location']['localtime']} "
        f"Weather: {weather_dict['current']['temp_c']} Celsius,"
        f" {weather_dict['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
