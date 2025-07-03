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

def count(data):
    i = 0
    while i < len(data):
        i += 1
    return i

def summation(data):
    sum1 = 0
    for num in data:
        sum1 += num
    return sum1

def average(data):
    if len(data) == 0:
        raise ValueError("Cannot calculate average of an empty list")
    return summation(data)/count(data)

def minimum(data):
    if len(data) == 0:
        raise ValueError("Cannot find minimum value of an empty list")
    
    min_val = data[0]
    for num in data[1:]: # Start from the second element
        if num < min_val:
            min_val = num
    return min_val

def maximum(data):
    if len(data) == 0:
        raise ValueError("Cannot find maximum value of an empty list")
    
    max_val = data[0]
    for num in data[1:]: # Start from the second element
        if num > max_val:
            max_val = num
    return max_val

def harmonic_mean(data):
    if len(data) == 0:
        raise ValueError("Cannot calculate harmonic mean of an empty list")
    sum_of_reciprocals = sum(1 / num for num in data)
    harmonic_mean = count(data) / sum_of_reciprocals
    return harmonic_mean

def variance(data):
    if len(data) == 0:
        raise ValueError("Cannot calculate variance of an empty list")
    mean = average(data)
    squared_differences_sum = sum((x - mean) ** 2 for x in data)
    variance = squared_differences_sum / count(data)
    return variance

def standard_dev(data):
    if len(data) == 0:
        raise ValueError("Cannot calculate standard deviation of an empty list")
    # Standard deviation is the square root of variance
    return math.sqrt(variance(data))
