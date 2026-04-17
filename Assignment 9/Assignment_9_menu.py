def count_lines(filename):
    count = 0
    with open(filename) as f:
        for line in f:
            if line.strip() != "":
                count += 1
    return count

def keyword_lines(filename, keyword):
    result = []
    line_number = 1
    with open(filename) as f:
        for line in f:
            if keyword in line:
                result.append(line_number)
            line_number += 1
    return result

def to_upper(filename):
    with open(filename) as f:
        text = f.read()
    with open("output.txt", "w") as output:
        output.write(text.upper())
    print("Saved uppercase text to output.txt")

def average_score(filename):
    total = 0
    count = 0
    with open(filename) as f:
        for line in f:
            if line.strip() != "":
                name, score = line.split(",")
                score = int(score)
                print(f"{name} scored {score}")
                total += score
                count += 1
    avg = total / count if count > 0 else 0
    return avg

def main():
    mbox_file = "mbox-short.txt"   # used for tasks 1–3
    student_file = "students.txt"  # used for task 4

    while True:
        print("\nChoose an option:")
        print("1. Count non-blank lines in mbox-short.txt")
        print("2. Find keyword line numbers in mbox-short.txt")
        print("3. Convert mbox-short.txt to uppercase (save to output.txt)")
        print("4. Calculate average score from students.txt")
        print("5. Exit")

        choice = input("Please enter choice (1-5): ")

        if choice == "1":
            print("Total non-blank lines:", count_lines(mbox_file))
        elif choice == "2":
            keyword = input("Please enter your keyword: ")
            print("Keyword found in lines:", keyword_lines(mbox_file, keyword))
        elif choice == "3":
            to_upper(mbox_file)
        elif choice == "4":
            print("Average score:", average_score(student_file))
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
