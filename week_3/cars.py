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
		if  self.body_whl:
			print(self.body_whl)
			self.body_width = float(self.body_whl.split("x")[0])
			self.body_height = float(self.body_whl.split("x")[1])
			self.body_length = float(self.body_whl.split("x")[2])


#	body_width = property()
#	body_height = property()
#	body_length = property()

#	@body_width.setter
#	def body_width(self):
#		self._body_width = float(self.body_whl.split("x")[0])
#		print(self._body_width)

#	@body_height.setter
#	def body_height(self):
#		self._body_height = float(self.body_whl.split("x")[1])
#		print(self._body_height)

#	@body_length.setter
#	def body_length(self):
#		self._body_length = float(self.body_whl.split("x")[2])
#		print(self._body_length)

	def get_body_volume(self):
		return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
	def __init__(self, brand, photo_file_name, carrying, extra):
		super().__init__(brand, photo_file_name, carrying)
		self.car_type = "spec_machine"
		self.extra = extra


def get_car_list(csv_filename):
	car_list = []
	with open(csv_filename, 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			try:
				if row[0] and row[0].replace(';',''):
					car_list.append(row)
			except Exception:
				print("exception")
	data = car_list[1:]
	cars = []

	for car in data:
		l = car[0].split(';')
		if l[0] == 'car':
			cars.append(Car(brand=l[1], 
				photo_file_name=l[3], 
				carrying=float(l[5]), 
				passenger_seats_count=int(l[2])))

		elif l[0] == 'truck':
			cars.append(Truck(brand=l[1], 
				photo_file_name=l[3], 
				carrying=float(l[5]), 
				body_whl=l[4]))

		elif l[0] == 'spec_machine':
			cars.append(SpecMachine(brand=l[1], 
				photo_file_name=l[3], 
				carrying=float(l[5]), 
				extra=l[6]))
	return cars



def main():
	cars_list = get_car_list('/home/kitik/coding/coursera_python/week_3/coursera_week3_cars.csv')

	

if __name__ == "__main__":
	main()