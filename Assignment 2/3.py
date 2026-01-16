def check_hemoglobin():
    sex = input("Enter your biological sex (male/female): ").lower()
    hemoglobin = float(input("Enter your hemoglobin value (g/l): "))
    
    if sex == "female":
        if hemoglobin < 117:
            print("hemoglobin level is low.")
        elif hemoglobin > 155:
            print("Your hemoglobin level is high.")
        else:
            print("Your hemoglobin level is normal.")
    elif sex == "male":
        if hemoglobin < 134:
            print("Your hemoglobin level is low.")
        elif hemoglobin > 167:
            print("Your hemoglobin level is high.")
        else:
            print("Your hemoglobin level is normal.")
    else:
        print("Invalid input for biological sex.")
check_hemoglobin()