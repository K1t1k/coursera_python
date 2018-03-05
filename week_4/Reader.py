# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 10:05:44 2018

@author: biryukovnd
"""
import io
import os
import tempfile


class File:
    def __init__(self, path):
        self.path = path
        self.text = list()
        try:
            with open(path, 'r') as f:
                for line in f:
                    self.text.append(line)
            self.end = len(self.text) - 1
        except:
            print('file not found')

    def write(self, text):
        with open(self.path, 'a') as f:
            f.write(text)

    def __str__(self):
        return self.path

#    def __iter__(self):
#       return self

#   def __next__(self):
#       if self.end < 0:
#           raise StopIteration
#       index = self.end
#       self.end = self.end - 1
#       return self.text[index]

    def __getitem__(self, index):
#        path_file = os.path.join(tempfile.gettempdir(), os.path.normcase(self.path_to_file))
        with io.open(self.path, 'r+', encoding='utf-8') as f:
            data_file = f.readlines()
        return data_file[index]

    def __add__(self, obj):
        with open(self.path, 'r') as f:
            file1 = f.read()
        with open(obj.path, 'r') as f:
            file2 = f.read()
#       with open(os.path.join(tempfile.gettempdir(), 'tf.txt'), 'w') as f:
#            f.write(file1 + file2)
        return_class = File(os.path.join(tempfile.gettempdir(), 'tf.txt'))
        return_class.write(file1 + file2)
        return return_class


def main():
    obj = File('/home/kitik/coding/coursera_python/week_4/textfile.txt')
    for i in obj:
        print(i)


if __name__ == "__main__":
    main()