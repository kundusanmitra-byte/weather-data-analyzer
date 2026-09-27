# Weather Data Analyzer

A simple Python script that fetches live weather data for multiple cities using the OpenWeatherMap API, and compares them to identify the hottest and coldest city among the ones entered.

## What it does

- Takes a list of city names as input from the user
- Fetches real-time weather data (temperature, conditions, humidity) for each city via a public REST API
- Handles invalid city names or failed requests gracefully, without crashing
- Compares temperatures across all valid cities to identify the hottest and coldest one

## Example

```
Enter city names separated by commas: Mumbai, Delhi, Kolkata, Chennai

Mumbai: 28.41°C, overcast clouds
Delhi: 23.2°C, overcast clouds
Kolkata: 28.91°C, scattered clouds
Chennai: 31.55°C, overcast clouds

Hottest city: Chennai (31.55°C)
Coldest city: Delhi (23.2°C)
```

## Tech / concepts used

- Fetching data from a REST API using the `requests` library
- Parsing and navigating nested JSON responses
- Functions, dictionaries, loops, and conditional logic
- Error handling for invalid input / failed API responses (`status_code` checks)
- Environment variables (`.env` file) to keep the API key out of the source code

## How to run it

1. Clone this repository
2. Install dependencies:
   ```
   pip install requests python-dotenv
   ```
3. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
4. Create a `.env` file in the project folder with:
   ```
   API_KEY=your_api_key_here
   ```
5. Run the script:
   ```
   python weather_app.py
   ```
6. When prompted, enter city names separated by commas (e.g. `Delhi, Mumbai, Kolkata`)

## Why I built this

I come from a data/analytics background (Excel, SQL, KQL) and wanted hands-on experience with Python — specifically working with APIs, JSON data, and basic data comparison logic, as a first step toward applying Python to data-focused work.
