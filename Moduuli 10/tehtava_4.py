import random

class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed <= 0:
            self.current_speed = 0

    def drive(self, time):
        new_distance = self.travelled_distance + (self.current_speed * time)
        self.travelled_distance = new_distance


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        i = random.randint(-10,15)
        for car in self.cars:
            car.accelerate(i)
            car.drive(1)

    def print_status(self):
        for car in self.cars:
            print(f"Status: {car.license_plate}, "
                  f"{car.maximum_speed}, {car.current_speed}, "
                  f"{car.travelled_distance}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False