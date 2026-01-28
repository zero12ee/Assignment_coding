def login_system():
    Attemp = 0
    Max_Attempt = 5
    while Attemp < Max_Attempt:
        Username = input("Enter your username: ")
        Password = input("Enter your password: ")

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

login_system()