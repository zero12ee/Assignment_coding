# 1. Check course code format (3 uppercase letters + 3 digits)
def is_course_code(code):
    if len(code) != 6:
        return False
    return code[:3].isupper() and code[:3].isalpha() and code[3:].isdigit()


# 2. Check hex color format (# + 6 hex characters)
def is_hex_color(color):
    if len(color) != 7:
        return False
    if color[0] != "#":
        return False
    for ch in color[1:]:
        if not (ch.isdigit() or ch.upper() in "ABCDEF"):
            return False
    return True


# 3. Sum all numbers in text
def sum_numbers_in_text(text):
    total = 0
    num = ""
    for ch in text:
        if ch.isdigit():
            num += ch
        else:
            if num != "":
                total += int(num)
                num = ""
    if num != "":
        total += int(num)
    return total


# 4. Redact phone numbers (10 digits or starting with +84)
def redact_phone_numbers(text):
    words = text.split()
    result = []
    for word in words:
        if (word.isdigit() and len(word) == 10) or word.startswith("+84"):
            result.append("[REDACTED]")
        else:
            result.append(word)
    return " ".join(result)

while True:
    print("Choose an option (1-5):")
    print("1. Check course code format")
    print("2. Check hex color format")
    print("3. Sum all numbers in text")
    print("4. Redact phone numbers")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        code = input("Please enter course code: ")
        if is_course_code(code):
            print("Valid course code.")
        else:
            print("Invalid course code.")
    elif choice == "2":
        color = input("Please enter hex color: ")
        if is_hex_color(color):
            print("Valid hex color.")
        else:
            print("Invalid hex color.")
    elif choice == "3":
        text = input("Please enter text: ")
        total = sum_numbers_in_text(text)
        print(f"Sum of numbers in text: {total}")
    elif choice == "4":
        text = input("Please enter text: ")
        redacted = redact_phone_numbers(text)
        print(f"The redacted text is: {redacted}")
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")