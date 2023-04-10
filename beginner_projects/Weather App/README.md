## Weather Data Retrieval
This Python script retrieves and displays weather data for a specified city using the OpenWeatherMap API. It provides information such as temperature, humidity, pressure, and wind speed.

### Installation
Make sure you have Python 3.x installed on your system. You can download Python from the official website: https://www.python.org/downloads/

Install the required package: requests. You can install it using pip:

`pip install requests`

Sign up for a free API key at https://openweathermap.org/appid. Replace `your_api_key` in the script with your actual API key.

### Usage
Save the script as `weather_data.py`.

Open a terminal and navigate to the directory where you saved the script.

Run the script:

`python weather_data.py`

Enter the name of the city when prompted:

`Enter the name of the city: New York`

The script will display the weather data for the specified city:

`City: New York
Weather: scattered clouds
Temperature: 24.5°C
Feels Like: 23.9°C
Min Temperature: 23.2°C
Max Temperature: 25.6°C
Humidity: 53%
Pressure: 1013 hPa
Wind Speed: 3.6 m/s`

### License
This project is licensed under the MIT License. See the LICENSE file for details.
