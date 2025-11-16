class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Hissi on kerroksessa {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Hissi on kerroksessa {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor > self.current_floor:
            while self.current_floor < target_floor:
                self.floor_up()
        elif target_floor < self.current_floor:
            while self.current_floor > target_floor:
                self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []

        for _ in range(elevator_count):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_index, target_floor):
        if 0 <= elevator_index < len(self.elevators):
            elevator = self.elevators[elevator_index]
            elevator.go_to_floor(target_floor)