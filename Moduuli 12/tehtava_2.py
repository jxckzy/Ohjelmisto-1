import requests

municipality = input("Enter municipality name: ")

api_key = ""
url = f"http://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        description = data['weather'][0]['description']
        temperature = data['main']['temp']
        print(f"Weather: {description}")
        print(f"Temperature: {temperature} Celsius")
    else:
        print(f"Error: HTTP status {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")