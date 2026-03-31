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


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
        self.hours_passed = 0

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)
        self.hours_passed += 1

    def print_status(self):
        print(f"\nRace: {self.name} | Distance: {self.distance} km | Hours passed: {self.hours_passed}")
        print(f"{'RegNum':<8} | {'MaxSpeed':<10} | {'CurSpeed':<12} | {'Distance':<15}")
        print("-" * 55)
        for car in self.cars:
            print(f"{car.registration_number:<8} | {car.max_speed:<10} | {car.current_speed:<12} | {car.travelled_distance:<15.0f}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)

    def get_winner(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return car
        return None


# --- Main Program ---
def main():
    # Create 10 cars
    cars = []
    for i in range(1, 11):
        reg_num = f"ABC-{i}"
        max_speed = random.randint(150, 200)
        cars.append(Car(reg_num, max_speed))

    # Create race
    race = Race("Grand Demolition Derby", 8000, cars)

    # Simulate race
    while not race.race_finished():
        race.hour_passes()
        if race.hours_passed % 10 == 0:
            race.print_status()

    # Print final status
    race.print_status()
    winner = race.get_winner()
    if winner:
        print(f"\nWinner: {winner.registration_number}!")
    print("\nRace finished!")


if __name__ == "__main__":
    main()