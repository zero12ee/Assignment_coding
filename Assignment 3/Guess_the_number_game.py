

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
guess_the_number_game()