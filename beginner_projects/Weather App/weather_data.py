import requests

def get_weather_data(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    return response.json()

def display_weather_data(data):
    if data["cod"] != "404":
        main_data = data["main"]
        weather_data = data["weather"][0]
        print(f"City: {data['name']}")
        print(f"Weather: {weather_data['description']}")
        print(f"Temperature: {main_data['temp']}°C")
        print(f"Feels Like: {main_data['feels_like']}°C")
        print(f"Min Temperature: {main_data['temp_min']}°C")
        print(f"Max Temperature: {main_data['temp_max']}°C")
        print(f"Humidity: {main_data['humidity']}%")
        print(f"Pressure: {main_data['pressure']} hPa")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("City not found. Please check the city name and try again.")

def main():
    api_key = "your_api_key"
    city = input("Enter the name of the city: ").strip()
    weather_data = get_weather_data(city, api_key)
    display_weather_data(weather_data)

if __name__ == "__main__":
    main()
