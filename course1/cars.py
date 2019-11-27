import csv
import os

class TruckVolumeException(BaseException):
    pass

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        try:
            extention = os.path.splitext(self.photo_file_name)[1]
        except os.error as e:
            print(e)
        else:
            return extention


class Car(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        CarBase.__init__(self,brand,photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count
        self.car_type = car_type


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl=""):
        CarBase.__init__(self,brand,photo_file_name, carrying)
        self._body_whl = body_whl
        self.car_type = car_type
        self.body_height = 0
        self.body_length = 0
        self.body_width = 0
        self.parse_body_whl(self._body_whl)

    def parse_body_whl(self, body_whl):
        try:
            if body_whl == "":
                self.body_length, self.body_width, self.body_height = 0, 0, 0
            else:
                self.body_length, self.body_width, self.body_height = tuple(map(float, body_whl.split("x")))
        except:
            print("Non-valid body volume")

    def get_body_volume(self):
        return self.body_width * self.body_length * self.body_height




class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        CarBase.__init__(self,brand,photo_file_name, carrying)
        self.extra = extra
        self.car_type = car_type

def validate_row(row):
    if len(row) < 7:
        return 0
    if not row[0] or not row[1] or not row[3] or not row[5]:
        return 0
    if row[0] == "car" and not row[2]:
        return 0
    if row[0] == "spec_machine" and not row[6]:
        return 0
    return True


def create_car(row):
    car_type = row[0]
    brand = row[1]
    photo = row[3]
    carrying = float(row[5])
    if car_type == "spec_machine":
        extra = row[6]
        return SpecMachine(car_type,brand,photo,carrying,extra)
    if car_type == "car":
        passenger_seat_cout = int(row[2])
        return Car(car_type,brand,photo,carrying,passenger_seat_cout)
    if car_type == "truck":
        body_whl = row[4]
        return Truck(car_type,brand,photo,carrying,body_whl)



def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if validate_row(row):
                car_list.append(create_car(row))
            else:
                continue
    return car_list


# lastochka = Truck("truck","Renault", 'picture.png',2500, '2x3x4')
#
# print(lastochka.get_body_volume())
# print(lastochka.get_photo_file_ext())
# l = get_car_list('cars.csv')
# print(l[0].passenger_seats_cout)



