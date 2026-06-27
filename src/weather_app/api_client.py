import requests
from src.weather_app.config import API_KEY

class WeatherClient:

    def __init__(self):
        self.api_key = API_KEY
    
    def get_weather(self, city: str) -> dict:
        '''Метод получает текущую погоду для указанного города.'''

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"Ошибка при получении данных: {response.status_code}")

        data = response.json()
        return {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }