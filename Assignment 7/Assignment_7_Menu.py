import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

    def __str__(self):
        return f"Reg.Num: {self.registration_number:<8} | Max.Spd: {self.max_speed:<10} | Cur.Spd: {self.current_speed:<12} | Travl.Dis: {self.travelled_distance:<15.0f}"





# ---Car registration and acceleration test---
def step1():
    car = Car("ABC-123", 142)
    print("Initial car properties:")
    print(car)

    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)
    print("\nSpeed after accelerations:", car.current_speed)

    car.accelerate(-200)
    print("Speed after emergency brake:", car.current_speed)



# ---Test drive---
def step2():
    car = Car("ABC-123", 142)

    old_distance = float(input("Enter old travelled distance (km): "))
    car.travelled_distance = old_distance

    speed_change = int(input("Enter speed change before driving: "))
    car.accelerate(speed_change)

    hours = float(input("Enter hours to drive: "))
    car.drive(hours)


    print("\nCar properties after driving:")
    print(car)


# ---Car race simulation ---
def step3():
    cars = []
    for i in range(1, 11):
        reg_num = f"ABC-{i}"
        max_speed = random.randint(150, 200)
        cars.append(Car(reg_num, max_speed))

    race_finished = False
    while not race_finished:
        for c in cars:
            speed_change = random.randint(-10, 15)
            c.accelerate(speed_change)
            c.drive(1)
            if c.travelled_distance >= 10000:
                race_finished = True
                winner = c
                break

    print("\nRace results:")
    for c in cars:
        print(c)

    print(f"\n Winner: {winner.registration_number} with {winner.travelled_distance:.1f} km!")


# ---Main---
def main():
    print("Choose a step to run:")
    print("1 - Car registration and acceleration test")
    print("2 - Test drive")
    print("3 - Race simulation")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        step1()
    elif choice == "2":
        step2()
    elif choice == "3":
        step3()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
