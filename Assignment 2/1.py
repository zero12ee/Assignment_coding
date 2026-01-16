def check_zander_size():
    length = int(input("Enter the length of the zander in cm: "))
    if length < 42:
        print(f"Release the fish back into the lake. It is {42 - length} cm below the size limit.")
    else:
        print("The fish meets the size limit.")

check_zander_size()