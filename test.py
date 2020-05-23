#plot a distribution density histogram from an number array
#you have to write numbers into a text file, splitting it by space
#and pass the file path to script as a command line argument
import random
import sys
import math
from collections import defaultdict
from bisect import bisect_left
import matplotlib.pyplot as plt

def get_random_array(num,beg,end):
    mylist = [0]
    for i in range(num):
        mylist.append(random.uniform(beg,end))
    return mylist

def get_interval_quantity(array_length):
    return round(5 * math.log10(array_length))

def get_delta_x(array):
    return round((max(array) - min(array))/get_interval_quantity(len(array)),3)

def get_list_intervals(min_in_array,delta_x,interval_quantity):
    list_for_return = [0]
    list_for_return.remove(0)
    left_bound = 0
    right_bound = delta_x
    for i in range(interval_quantity):
        list_for_return.append([left_bound,right_bound])
        left_bound+=delta_x
        right_bound+=delta_x
        left_bound = round(left_bound,3)
        right_bound = round(right_bound,3)
    return list_for_return

def count_intervals(sequence, intervals):
    count = defaultdict(int)
    intervals.sort()
    for item in sequence:
        pos = bisect_left(intervals, item)
        if pos == len(intervals):
            count[None] += 1
        else:
            count[intervals[pos]] += 1
    return count

#entry point
print(sys.argv[1])
file = open(sys.argv[1],'r')
contents = file.read()
str_array = contents.split(' ')
array = []
for i in str_array:
    array.append(float(i))
#array = get_random_array(500,0,100)
file.close()
array.sort()
iq = get_interval_quantity(len(array))
dx = get_delta_x(array)
intervals = get_list_intervals(min(array),dx,iq)
str_intervals = {}
for i in intervals:
    str_intervals[str(i)]=0
for i in intervals:
    str_intervals[str(i)]=(count_intervals(array,i)[i[1]])
plt.bar(str_intervals.keys(), str_intervals.values(), 0.7, color='g')
plt.show()