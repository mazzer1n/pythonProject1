import csv
import os

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.car_type = None
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        _, ext = os.path.splitext(self.photo_file_name)
        return ext

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = int(passenger_seats_count)

class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        self.body_length, self.body_width, self.body_height = self.parse_body_whl(body_whl)

    def parse_body_whl(self, body_whl):
        if body_whl:
            return map(float, body_whl.split('x'))
        return 0.0, 0.0, 0.0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra

def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            try:
                car_type, brand, passenger_seats_count, photo_file_name, body_whl, carrying, extra = row
                if car_type == 'car':
                    car_list.append(Car(brand, photo_file_name, carrying, passenger_seats_count))
                elif car_type == 'truck':
                    car_list.append(Truck(brand, photo_file_name, carrying, body_whl))
                elif car_type == 'spec_machine':
                    car_list.append(SpecMachine(brand, photo_file_name, carrying, extra))
            except (ValueError, IndexError):
                pass
    return car_list

cars = get_car_list('cars.csv')
for car in cars:
    print(f'Type: {car.car_type}, Brand: {car.brand}, Photo Ext: {car.get_photo_file_ext()}')
    if isinstance(car, Truck):
        print(f'Body Volume: {car.get_body_volume()}')
    print('-' * 30)

