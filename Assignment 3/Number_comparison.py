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

Number_comparison()