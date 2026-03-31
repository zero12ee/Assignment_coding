import random

class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = 0  # Always start at Ground floor (bottom floor for task 1)

    def floor_up(self, notification=True):
        if self.current_floor < self.top:
            self.current_floor += 1
            if notification:
                print(f"Elevator is now at floor {self._format_floor(self.current_floor)}")

    def floor_down(self, notification=True):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            if notification:
                print(f"Elevator is now at floor {self._format_floor(self.current_floor)}")
                
    def go_to_floor(self, target_floor, notification=True):
        if target_floor < self.bottom or target_floor > self.top:
            print("Invalid floor.")
            return
        while self.current_floor < target_floor:
            self.floor_up(notification)
        while self.current_floor > target_floor:
            self.floor_down(notification)

    def _format_floor(self, floor):
        if floor < 0:
            return f"B{abs(floor)}"
        if floor == 0:
            return "G"
        return str(floor)


class Building:
    def __init__(self, building_type, floors, basements, num_elevators):
        self.building_type = building_type
        self.floors = floors
        self.basements = basements
        self.bottom = -basements
        self.top = floors
        self.elevators = [Elevator(self.bottom, self.top) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor, notification=True):
        if 1 <= elevator_number <= len(self.elevators):
            print(f"\nRunning elevator {elevator_number} to floor {self._format_floor(destination_floor)}")
            self.elevators[elevator_number - 1].go_to_floor(destination_floor, notification)
        else:
            print("Invalid elevator number.")

    def fire_alarm(self):
        print("\nWarning! Fire alarm system activated!")
        print("All elevators returning to Ground floor...")
        print("Please evacuate the building immediately!\n")
        for i in range(len(self.elevators)):
            print(f"\nElevator {i + 1}:")
            while self.elevators[i].current_floor > 0:
                self.elevators[i].floor_down()
            while self.elevators[i].current_floor < 0:
                self.elevators[i].floor_up()

    def show_status(self):
        print("\nElevator Status Board")
        for i in range(len(self.elevators)):
            print(f"Elevator {i + 1}: Floor {self.elevators[i]._format_floor(self.elevators[i].current_floor)}")
        print("-" * 30)

    def _format_floor(self, floor):
        if floor < 0:
            return f"B{abs(floor)}"
        if floor == 0:
            return "G"
        return str(floor)


def create_random_building():
    building_type = random.choice(["Office", "Mall", "Apartment", "Complex"])
    if building_type == "Office":
        floors = random.randint(4, 15)
    elif building_type == "Mall":
        floors = random.randint(1, 6)
    elif building_type == "Apartment":
        floors = random.randint(5, 21)
    else:  # Complex
        mall = random.randint(1, 6)
        office = random.randint(10, 40)
        residential = random.randint(10, 40)
        floors = mall + office + residential

    # Basement based on floors
    if floors <= 5:
        basements = 1
    elif 6 <= floors < 15:
        basements = 2
    elif 15 <= floors < 21:
        basements = random.randint(2, 3)
    else:
        basements = 3

    # Elevator number rules
    if building_type == "Mall":
        if floors <= 2:
            num_elevators = 2
        elif floors <= 5:
            num_elevators = 4
        else:  
            num_elevators = 6
    elif floors <= 5:
        num_elevators = 1
    elif floors < 11:
        num_elevators = 2
    elif floors < 21:
        num_elevators = 4
    elif floors <= 40:
        num_elevators = 6
    else:  # >40 floors
        num_elevators = 8

    return Building(building_type, floors, basements, num_elevators)


def run_elevator_simulation(building, activated, notification=True):
    possible_floors = [building._format_floor(f) for f in range(building.bottom, building.top + 1)]

    num_active = random.randint(1, len(building.elevators))
    print(f"\nActivating {num_active} elevators...")

    for i in range(1, num_active + 1):
        destination_label = random.choice(possible_floors)

        if destination_label.startswith("B"):
            destination = -int(destination_label[1:])
        elif destination_label == "G":
            destination = 0
        else:
            destination = int(destination_label)

        if building.elevators[i - 1].current_floor != 0:
            building.elevators[i - 1].current_floor = 0

        if notification:
            print(f"\nElevator {i} moving from G to {destination_label}")
        else:
            print(f"\nElevator {i} sent to {destination_label}")

        building.run_elevator(i, destination, notification)
        activated.add(i)

    building.show_status()


if __name__ == "__main__":
    print("Choose a task:")
    print("1. Task 1: Move one elevator to a chosen floor, then back to Ground")
    print("2. Task 2: Building creation with fire alarm system")
    choice = input("Please enter your choice (1-2): ")

    if choice == "1":
        building = Building("Test", 10, 1, 3)
        print("\nBuilding created with floors G to 10 and 3 elevators.")
        floor = int(input("Please enter the floor to go to: "))
        print("\nTask 1:")
        building.run_elevator(1, floor)   # use elevator 1
        building.run_elevator(1, 0)       # back to Ground (bottom)

    elif choice == "2":
        building = create_random_building()
        print(f"\nBuilding successfully built: {building.building_type} "
              f"with {building.floors} floors, {building.basements} basements, "
              f"and {len(building.elevators)} elevators.")

        activated = set()
        run_elevator_simulation(building, activated, notification=True)

        while True:
            print("1. Continue running elevators (notification ON)")
            print("2. Continue running elevators (notification OFF)")
            print("3. Activate fire alarm system")
            print("4. Exit simulation")
            sub_choice = input("Please enter your choice (1-4): ")

            if sub_choice == "1":
                run_elevator_simulation(building, activated, notification=True)
            elif sub_choice == "2":
                run_elevator_simulation(building, activated, notification=False)
            elif sub_choice == "3":
                building.fire_alarm()
                building.show_status()
                break
            elif sub_choice == "4":
                print("Simulation ended.")
                break
            else:
                print("Invalid choice.")