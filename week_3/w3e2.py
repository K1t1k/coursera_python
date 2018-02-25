from os.path import splitext
import csv

class CarBase:
	def __init__(self, brand, photo_file_name, carrying):
		self.brand = brand
		self.photo_file_name = photo_file_name
		self.carrying = carrying

	def get_photo_file_ext(self):
		return splitext(self.photo_file_name)[1]


class Car(CarBase):
	def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
		super().__init__(brand, photo_file_name, carrying)
		self.car_type = "car"
		self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
	def __init__(self, brand, photo_file_name, carrying, body_whl):
		super().__init__(brand, photo_file_name, carrying)
		self.car_type = "truck"
		self.body_whl = body_whl

	@property
	def body_width(self):
		self.body_whl.split("x")[0]

	@property
	def body_height(self):
		self.body_whl.split("x")[1]

	@property
	def body_length(self):
		self.body_whl.split("x")[2]

	def get_body_volume(self):
		return body_width * body_height * body_length


class SpecMachine(CarBase):
	def __init__(self, brand, photo_file_name, carrying, extra):
		super().__init__(brand, photo_file_name, carrying)
		self.car_type = "spec_machine"
		self.extra = extra


def get_car_list(csv_filename):
    with open(csv_filename, 'r+', encoding='utf-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        list_car = []
        for row in reader:
            car_property = {}
            listtypeproperty = [
                'car_type','brand','passenger_seats_count','photo_file_name',
                'body_whl','carrying','extra'
            ]
            if len(row) < 7:
                continue
            else:
                for i in range(7):
                    car_property[listtypeproperty[i]] = row[i]
                #print(car_property)
                list_car.append(car_property)
        print(list_car)

            



get_car_list('coursera_week3_cars.csv')