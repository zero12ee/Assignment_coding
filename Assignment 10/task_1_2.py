import requests

def chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    data = response.json()
    print("Joke:", data["value"])

def weather_report(city):
    api_key = "5bf2d7a6f20cb9bea2ec09683e9cf784"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        print("City not found.")
        return

    description = data["weather"][0]["description"]
    temp_kelvin = data["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15
    print(f"Weather in {city}: {description}, {temp_celsius:.1f}°C")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Get a random Chuck Norris joke")
        print("2. Get weather report for a city")
        print("3. Exit")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            chuck_norris_joke()
        elif choice == "2":
            city = input("Enter city name: ")
            weather_report(city)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
