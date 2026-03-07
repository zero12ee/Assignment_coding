def five_greatest_numbers():
    numbers = []
    while True:
        entry = input("Please enter a number (enter empty string to quit): ")
        if entry == "":
            break
        numbers.append(int(entry))
    numbers.sort(reverse=True)
    print("Five greatest numbers are:", numbers[:5])


def month_to_season():
    seasons = ("Winter", "Spring", "Summer", "Autumn")
    month = int(input("Please enter month number (1-12): "))
    if month in (12, 1, 2):
        print(seasons[0])
    elif month in (3, 4, 5):
        print(seasons[1])
    elif month in (6, 7, 8):
        print(seasons[2])
    elif month in (9, 10, 11):
        print(seasons[3])
    else:
        print("Invalid month. Please try again.")


def names_with_set():
    names = set()
    while True:
        name = input("Please enter a name (enter empty string to quit): ")
        if name == "":
            break
        if name in names:
            print("Existing name")
        else:
            print("New name")
            names.add(name)
    print("\nList of names:")
    for jiao in names:
        print(jiao)


def word_frequency(text):
    words = text.split()
    freq = {}
    for word in words:
        word = word.lower().strip(".,!?")
        freq[word] = freq.get(word, 0) + 1
    return freq


def get_numbers():
    numbers = []
    while True:
        entry = input("Enter a number (enter empty string to quit): ")
        if entry == "":
            break
        numbers.append(int(entry))
    return numbers

def remove_odds(numbers):
    return [n for n in numbers if n % 2 == 0]

def test_remove_odds():
    original = get_numbers()
    filtered = remove_odds(original)

    print("Original list:", original)
    print("Filtered list (no odds):", filtered)


def main():
    while True:

        print("1. Five greatest numbers")
        print("2. Month to season")
        print("3. Names with set")
        print("4. Word frequency")
        print("5. Remove odd numbers")
        print("0. Quit")

        choice = input("Please choose an option: ")

        if choice == "1":
            five_greatest_numbers()
        elif choice == "2":
            month_to_season()
        elif choice == "3":
            names_with_set()
        elif choice == "4":
            text = input("Please enter text: ")
            print(word_frequency(text))
        elif choice == "5":
            test_remove_odds()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":  
    main()