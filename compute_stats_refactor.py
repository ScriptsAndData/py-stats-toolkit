import os
import math
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'random_nums.txt')

def read_ints():
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            num = int(line)
            data.append(num)
    return data

def count():
    data = read_ints()
    i = 0
    while i < len(data):
        i += 1
    return i

def summation():
    data = read_ints()
    sum1 = 0
    for num in data:
        sum1 += num
    return sum1

def average():
    return summation()/count()

def minimum():
    data = read_ints()
    min = 99999999
    for num in data:
        if num < min:
            min = num
    return min

def maximum():
    data = read_ints()
    max = 0
    for num in data:
        if num > max:
            max = num
    return max

def harmonic_mean():
    data = read_ints()
    sum_of_reciprocals = sum(1 / num for num in data)
    harmonic_mean = count() / sum_of_reciprocals
    return harmonic_mean

def variance():
    data = read_ints()
    mean = average()
    squared_differences_sum = sum((x - mean) ** 2 for x in data)
    variance = squared_differences_sum / count()
    return variance

def standard_dev():
    # Standard deviation is the square root of variance
    return math.sqrt(variance())
