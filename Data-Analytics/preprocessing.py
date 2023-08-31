import random
from random import randrange
import csv


def remove_column(filename, newfile, k):
    with open(filename, 'r') as i, open(newfile, 'w') as o:
        cr = csv.reader(i)
        cw = csv.writer(o)
        for row in cr:
            cw.writerow(row[0:k])


def decision(probability):
    return random.random() < probability

def create_list(filename):
    my_list = []
    my_file = open(filename, "r")
    tempData = my_file.read()
    my_list = tempData.split("\n")
    my_file.close()
    
    return my_list
    # print(my_list)

if __name__ == "__main__":
    print(randrange(0, 2000)) 
    bool = decision(0.2)
    print(bool)
