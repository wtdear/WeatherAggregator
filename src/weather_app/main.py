from weather_app.api_client import WeatherClient

def run():
    client = WeatherClient()
    city = input("Введите город: ")
    weather = client.get_weather(city)
    print(f"Погода в {city}: {weather.temperature}°C")