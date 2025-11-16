class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

license_plate = "ABC-123"
maximum_speed = 142
car = Car(license_plate, maximum_speed)
print(f"License plate: {car.license_plate}\n"
      f"Maximum speed: {car.maximum_speed} km/h\n"
      f"Current speed: {car.current_speed} km/h\n"
      f"Travelled distance: {car.travelled_distance} km")