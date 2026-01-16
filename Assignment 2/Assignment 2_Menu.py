import math

# 1. Zander size check
def check_zander_size():
    length = int(input("Enter the length of the zander in cm: "))
    if length < 42:
        print(f"Release the fish back into the lake. It is {42 - length} cm below the size limit.")
    else:
        print("The fish meets the size limit.")

# 2. Cruise cabin description
def cabin_description():
    cabin_class = input("Enter cabin class (LUX, A, B, C): ").upper()
    if cabin_class == "LUX":
        print("Upper-deck cabin with a balcony.")
    elif cabin_class == "A":
        print("Above the car deck, equipped with a window.")
    elif cabin_class == "B":
        print("Windowless cabin above the car deck.")
    elif cabin_class == "C":
        print("Windowless cabin below the car deck.")
    else:
        print("Invalid cabin class")

# 3. Hemoglobin level checker
def check_hemoglobin():
    sex = input("Enter your biological sex (male/female): ").lower()
    hemoglobin = float(input("Enter your hemoglobin value (g/l): "))
    
    if sex == "female":
        if hemoglobin < 117:
            print("Your hemoglobin level is low.")
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

# 4. Leap year checker
def is_leap_year():
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

# 5. Pizza value comparison
def unit_price(diameter, price):
    radius = diameter / 2
    area_m2 = math.pi * (radius ** 2) / 10000  # cm² to m²
    return price / area_m2

def compare_pizzas():
    print("Enter details for Pizza 1:")
    d1 = float(input("Diameter (cm): "))
    p1 = float(input("Price (USD): "))
    
    print("Enter details for Pizza 2:")
    d2 = float(input("Diameter (cm): "))
    p2 = float(input("Price (USD): "))
    
    up1 = unit_price(d1, p1)
    up2 = unit_price(d2, p2)
    
    print(f"Pizza 1 unit price: ${up1:.2f}/m²")
    print(f"Pizza 2 unit price: ${up2:.2f}/m²")
    
    if up1 < up2:
        print("Pizza 1 offers better value for money.")
    elif up2 < up1:
        print("Pizza 2 offers better value for money.")
    else:
        print("Both pizzas offer the same value.")

# ------------------------------
# Menu system
# ------------------------------
def main():
    while True:
        print("\n--- Assignments 2 Menu ---")
        print("1. Zander size check")
        print("2. Cruise cabin description")
        print("3. Hemoglobin level checker")
        print("4. Leap year checker")
        print("5. Pizza value comparison")
        print("0. Exit")

        choice = input("Choose an assignment (0-5): ")

        if choice == "1":
            check_zander_size()
        elif choice == "2":
            cabin_description()
        elif choice == "3":
            check_hemoglobin()
        elif choice == "4":
            is_leap_year()
        elif choice == "5":
            compare_pizzas()
        elif choice == "0":
            print("Goodbye! Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
