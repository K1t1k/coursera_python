# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 10:05:44 2018

@author: biryukovnd

"""
import os
import tempfile


class File:

    def __init__(self, path):
        self.path = path

    def write(self, text):

        with open(self.path, 'a') as f:

            f.write(text)

    def __str__(self):
        return self.path

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        with open(self.path, 'a') as f:
            result = f.readline()
        return result

    def __add__(self, obj):
        with open(self.path, 'r') as f:
            file1 = f.read()

        with open(obj.path, 'r') as f:
            file2 = f.read()
            
        with open(os.path.join(tempfile.gettempdir(),'tf.txt'), 'w') as f:
            f.write(file1 + file2)


def main():
    reader1 = File("C:\Users\BiryukovND\AnacondaProjects\example1.txt")
#    reader2 = File("C:\Users\BiryukovND\AnacondaProjects\example2.txt")
#    reader3 = reader1 + reader2
    for i in reader1:
        print(i)

if __name__ == "__main__":
    main()