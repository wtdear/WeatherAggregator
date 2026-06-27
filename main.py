import sys
from src.weather_app.api_client import WeatherClient

def main():
    print("=== 🌤️ Погодный Агрегатор ===")
    print("Для выхода введите 'выход', 'exit' или нажмите Ctrl+C")

    try:
        client = WeatherClient()
    except ValueError as e:
        print(f"❌ Ошибка инициализации: {e}")
        sys.exit(1)

    while True:
        try:
            city = input("\n🏙️ Введите название города: ").strip()
            

            if city.lower() in ['выход', 'exit', 'q']:
                print("До свидания! 👋")
                break
 
            if not city:
                print("Название города не может быть пустым. Попробуйте еще раз.")
                continue

            weather = client.get_weather(city)

            print("-" * 35)
            print(f"Погода: {city.title()}")
            print(f"Температура: {weather['temperature']}°C")
            print(f"На улице: {weather['description'].capitalize()}")
            print("-" * 35)
            
        except Exception as e:
            print(f"❌ Упс! Ошибка: {e}")
            
        except KeyboardInterrupt:
            print("\nПрограмма принудительно завершена. До свидания! 👋")
            sys.exit(0)

if __name__ == "__main__":
    main()