# -*- coding: utf-8 -*-

"""

Created on Tue Feb 20 10:05:44 2018

 

@author: biryukovnd

"""

 

class FileReader():
   
	def __init__(self, path):
		self.path = path

	def read(self):
		try:
			with open(self.path, 'r') as f:
				text = f.read()
			return text
		except Exception as e:
			print("Не верный путь")
			return ""

def main():
	reader = FileReader("exampl.txt")
	print(reader.read())
    

if __name__ == "__main__":
	main()