def number_divisible_by_3():
    m = 1
    count = 0
    while m <= 1000:
        if m % 3 == 0:
            count += 1
            print(m)
        m += 1
    print(f"Total numbers divisible by 3 in range of 1 to 1000 are: {count}")
number_divisible_by_3()