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

inches_to_centimeters()
        
        
        
