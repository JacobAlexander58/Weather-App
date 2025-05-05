import tkinter as tk
from tkinter import messagebox
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv('OPENWEATHER_API_KEY')


def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name.")
        return

    if not api_key:
        messagebox.showerror("API Key Error", "API key is missing. Please set it in the .env file.")
        return

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']

        result = (
            f"Weather in {city.capitalize()}: {weather.capitalize()}\n"
            f"Temperature: {temperature}°C\n"
            f"Humidity: {humidity}%\n"
            f"Pressure: {pressure} hPa"
        )
        result_label.config(text=result)
    else:
        result_label.config(text="City not found or invalid API key!")

# -------- GUI Setup --------
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 12), width=30)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="Weather details will appear here", font=("Arial", 11), justify="left", wraplength=350)
result_label.pack(pady=20)

root.mainloop()
