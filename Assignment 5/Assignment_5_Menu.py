def greatest_numbers():
    numbers = []
    while True:
        num_list = input("Please enter a number (or press Enter to quit): ")
        if num_list == "":
            break
        numbers.append(int(num_list))
    numbers = list(set(numbers))
    numbers.sort(reverse=True)
    print("Five greatest unique numbers:")
    for num in numbers[:5]:
        print(num)


def prime_check():
    num = int(input("Please enter an integer: "))
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    else:
        print(f"{num} is not a prime number.")

def city_names():
    cities = []
    for i in range(5):
        city = input(f"Please enter city {i+1}: ")
        cities.append(city)
    print("Cities entered:")
    for city in cities:
        print(city)

def sum_list():
    numbers = []
    while True:
        The_list = input("Please enter a number (or press Enter to quit): ")
        if The_list == "":
            break
        numbers.append(int(The_list))
    result = sum(numbers)
    print("The list:", numbers)
    print("Sum of the list:", result)

def remove_odds():
    numbers = []
    while True:
        user_input = input("Please enter a number (or press Enter to quit): ")
        if user_input == "":
            break
        numbers.append(int(user_input))
    filtered_list = [num for num in numbers if num % 2 == 0]
    print("Original list:", numbers)
    print("Even numbers only list:", filtered_list)

def main():
    while True:
        print("\n--- MENU ---")
        print("1. Enter numbers and show 5 greatest")
        print("2. Check if a number is prime")
        print("3. Enter and print 5 city names")
        print("4. Sum a list of numbers")
        print("5. Remove odd numbers from a list")
        print("6. Quit")

        choice = input("Please choose an option (1-6): ")

        if choice == "1":
            greatest_numbers()
        elif choice == "2":
            prime_check()
        elif choice == "3":
            city_names()
        elif choice == "4":
            sum_list()
        elif choice == "5":
            remove_odds()
        elif choice == "6":
            print("Goodbye! See ya!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

