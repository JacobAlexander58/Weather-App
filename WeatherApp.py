from dotenv import load_dotenv
import os
import requests


def get_weather(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']

        print(f"Weather in {city.capitalize()}: {weather.capitalize()}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
    else:
        print("City not found or invalid API key!")


def main():
    print("Welcome to the Weather App!")

    load_dotenv()  # Load the .env file here
    api_key = os.getenv('OPENWEATHER_API_KEY')  # Get the API key here

    if not api_key:
        print("API key not found. Make sure it's set in the .env file.")
        return

    while True:
        city = input("Enter a city name (or 'quit' to exit): ").strip()
        if city.lower() == 'quit':
            print("Goodbye!")
            break
        get_weather(city, api_key)


if __name__ == "__main__":
    main()


