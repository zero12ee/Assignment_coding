import requests
import json
def main():
    while True:
        print("\nPlease choose an option:")
        print("1. Airport_service_apis")
        print("2. Prime_number_apis")
        print("3. Exit")
        choice = input("Please enter your choice (1-3): ")
        if choice == "1":
            url = "http://127.0.0.1:5000/airport/LFLL"
            return url
        elif choice == "2":
            url = "http://127.0.0.1:5001/prime_number/17"
            return url
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def run():
    url = main()
    response = requests.get(url).json()
    print(response)
if __name__ == "__main__":
    run()
