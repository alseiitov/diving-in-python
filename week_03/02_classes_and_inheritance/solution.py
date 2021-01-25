import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.is_valid = True

        self.brand = brand
        if brand == "":
            self.is_valid = False
        self.photo_file_name = photo_file_name
        if self.get_photo_file_ext() == "":
            self.is_valid = False
        try:
            carrying = float(carrying)
        except ValueError:
            self.is_valid = False
            carrying = 0.0

        self.carrying = carrying

    def get_photo_file_ext(self):
        valid_ext = ['.jpg', '.jpeg', '.png', '.gif']
        try:
            ext = os.path.splitext(self.photo_file_name)[1]
            if ext not in valid_ext:
                self.is_valid = False
        except IndexError:
            self.is_valid = False
            return ''
        return ext


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'

        try:
            passenger_seats_count = int(passenger_seats_count)
        except ValueError:
            self.is_valid = False
            passenger_seats_count = 0

        self.passenger_seats_count = passenger_seats_count

    @classmethod
    def create_object(object_class, row):
        brand, passenger_seats_count, photo_file_name, carrying = row[1], row[2], row[3], row[5]
        return object_class(brand, photo_file_name, carrying, passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        body_whl_floats = body_whl.split('x')
        try:
            if len(body_whl_floats) != 3:
                body_width, body_height, body_length = 0.0, 0.0, 0.0
            else:
                body_length = float(body_whl_floats[0])
                body_width = float(body_whl_floats[1])
                body_height = float(body_whl_floats[2])
        except (IndexError, ValueError):
            self.is_valid = False
            body_width, body_height, body_length = 0.0, 0.0, 0.0

        self.body_width, self.body_height, self.body_length = body_width, body_height, body_length

    def get_body_volume(self):
        vol = self.body_height * self.body_length * self.body_width
        return vol

    @classmethod
    def create_object(object_class, row):
        brand, photo_file_name, body_whl, carrying = row[1], row[3], row[4], row[5]
        return object_class(brand, photo_file_name, carrying, body_whl)


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra
        if extra == "":
            self.is_valid = False

    @classmethod
    def create_object(object_class, row):
        brand, photo_file_name, carrying, extra = row[1], row[3], row[5], row[6]
        return object_class(brand, photo_file_name, carrying, extra)


def get_car_list(csv_filename):
    car_list = []
    car_types = {'car': Car, 'truck': Truck, 'spec_machine': SpecMachine}

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            try:
                car_type = row[0]
            except IndexError:
                continue

            if car_type in car_types:
                car = car_types[car_type].create_object(row)
                if car.is_valid:
                    car_list.append(car)

    return car_list
