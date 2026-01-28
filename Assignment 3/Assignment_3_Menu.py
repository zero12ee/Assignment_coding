# Assigment 1_Total numbers divisible by 3 from 1 to 1000
def number_divisible_by_3():
    m = 1
    count = 0
    while m <= 1000:
        if m % 3 == 0:
            count += 1
            print(m)
        m += 1
    print(f"Total numbers divisible by 3 in range of 1 to 1000 are: {count}")

#Assignment 2_Inches to centimeters converter
def inches_to_centimeters():
    while True:
        inches = float(input("Enter length in inches (please input negative to quit): "))
        if inches < 0:
            print("Exiting the converter.")
            break
        try:
            cm = inches * 2.54
            print(f"{inches} inches is equal to {cm} centimeters.")
        except ValueError:
            print("Please enter a valid number.")

# Assignment 3_number comparison
def Number_comparison():
    largest = None
    smallest = None
    count = 0
    print("Please input a number to compare. Press Enter to quit.")
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            print(f"Total numbers entered: {count}")
            print(f"The largest number is: {largest}")
            print(f"The smallest number is: {smallest}")
            break
        try:
            number = float(user_input)
            count += 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        def check_largest():
            if largest is None or number > largest:
                return number
            return largest
        def check_smallest():
            if smallest is None or number < smallest:
                return number
            return smallest
        largest = check_largest()
        smallest = check_smallest()

# Assignment 4_Guess the number game
def guess_the_number_game():
    import random
    secret_number = random.randint(1, 10)
    print("Welcome to the Guess the Number Game!^^!")
    print("I'm thinking of a number between 1 and 10. \nCan you guess what it is? ;P")
    while True:
        try:
            guess = int(input("Please enter your guess: "))
            if guess == secret_number:
                print(f"Correct!!!! Congratulations! You guessed the secret number correctly. It was {secret_number}.")
                print("Thanks for playing the Guess the Number Game! Goodbye! :D")
                break
            elif guess < 1 or guess > 10:
                print("Ah ah! @@ \nYour guess is out of bounds. Please guess a number between 1 and 10.")
            elif guess < secret_number:
                print("Too low! Please try a higher number.")
            else:
                print("Too high! Please try a lower number.")
        except ValueError:
            print("Ah Ah! @@ \nPlease enter a valid integer.")

# Assignment 5_Login your account with max 5 attempts
def login_system():
    Attemp = 0
    Max_Attempt = 5
    while Attemp < Max_Attempt:
        Username = input("Please enter your username: ")
        Password = input("Please enter your password: ")

        if Username == "python" and Password == "rules":
            print("Login successful! Welcome to the system.")
            break

        elif Username != "python" or Password != "rules":
            Attemp += 1
            
            if Attemp == Max_Attempt:
                print("Maximum login attempts reached. Access denied.\nPlease contact the administrator.")
            elif Max_Attempt - Attemp == 1:
                print(f"Wrong username or password. Please try again. \nYou have {Max_Attempt - Attemp} attempts left.")
                print("Warning!\nWarning!\nWarning!\nThis is your last attempt. Please be careful!")
            else:
                print(f"Wrong username or password. Please try again. \nYou have {Max_Attempt - Attemp} attempts left.")

# Assignment 6_Character extractor 
def character_extractor():
   text = input("Please enter a string: ")
   length = len(text)

   if length % 2 == 1:
        print(f"The middle character of the string is: {text[length // 2]}") 
   else:
        middle_1 = text[(length // 2) - 1]
        middle_2 = text[length // 2]
        print(f"The middle characters of the string are: {middle_1} and {middle_2}")

# Assignment 7_Acronym maker with find() function
def make_acronym():
   phrase = input("Please kindly enter a phrase: ")
   acronym = ""

   index = 0
   while index < len(phrase) and phrase[index] == " ":
      index += 1
   if index < len(phrase):
      acronym += phrase[index].upper()

   space_index = phrase.find(" ", index)
   while space_index != -1 and space_index + 1 < len(phrase):
        
      next_index = space_index + 1
      while next_index < len(phrase) and phrase[next_index] == " ":
         next_index += 1
      if next_index < len(phrase):
         acronym += phrase[next_index].upper()
      space_index = phrase.find(" ", next_index)
   print(f"The acronym is: {acronym}")

# Menu to select assignments
def assignment_3_menu():
    while True:
        print("\nAssignment Menu:")
        print("1. Total numbers divisible by 3 from 1 to 1000")
        print("2. Inches to centimeters converter")
        print("3. Number comparison")
        print("4. Guess the number game")
        print("5. Login your account with max 5 attempts")
        print("6. Character extractor")
        print("7. Acronym maker with find() function")
        print("Exit")

        choice = input("Please select an assignment to run (1-7). Type \"enter\" to exit: ").lower()

        if choice == '1':
            number_divisible_by_3()
        elif choice == '2':
            inches_to_centimeters()
        elif choice == '3':
            Number_comparison()
        elif choice == '4':
            guess_the_number_game()
        elif choice == '5':
            login_system()
        elif choice == '6':
            character_extractor()
        elif choice == '7':
            make_acronym()
        elif choice == 'exit':
            print("Exiting the assignment menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    assignment_3_menu()