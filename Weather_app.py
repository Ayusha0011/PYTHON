import requests

print("Welcome to the weather app")

city = input("Which city do you want to know the temperature of? ")

# (For now, we use fixed latitude & longitude)
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "hourly": "temperature_2m"
}

url = "https://api.open-meteo.com/v1/forecast"

# Make the API request
response = requests.get(url, params=params)

# Check if request worked
if response.status_code == 200:
    data = response.json()   # Extract JSON as dictionary

    # Access hourly temperatures
    temperatures = data["hourly"]["temperature_2m"]

    print("\nHourly temperatures:")
    for temp in temperatures[:10]:   # show first 10 values
        print(temp)

    # Save to file
    with open("Weatherdata.txt", "a") as f:
        for temp in temperatures:
            f.write(str(temp) + "\n")

else:
    print("Failed to fetch weather data")
