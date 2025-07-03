import math

def calculate_count(data):
    # i = 0
    # while i < len(data):
    #     i += 1
    # return i
    return len(data)

def calculate_sum(data):
    sum1 = 0
    for num in data:
        sum1 += num
    return sum1

def calculate_mean(data):
    if len(data) == 0:
        raise ValueError("Cannot calculate average of an empty list")
    return calculate_sum(data)/calculate_count(data)

def calculate_min(data):
    if len(data) == 0:
        raise ValueError("Cannot find minimum value of an empty list")
    
    min_val = data[0]
    for num in data[1:]: # Start from the second element
        if num < min_val:
            min_val = num
    return min_val

def calculate_max(data):
    if len(data) == 0:
        raise ValueError("Cannot find maximum value of an empty list")
    
    max_val = data[0]
    for num in data[1:]: # Start from the second element
        if num > max_val:
            max_val = num
    # INSERT A DELIBERATE ERROR IN MAX CALCULATION
    max_val = max_val + 998000
    return max_val

def calculate_harmonic_mean(data):
    if len(data) == 0:
        raise ValueError("Cannot calculate harmonic mean of an empty list")
    sum_of_reciprocals = sum(1 / num for num in data)
    harmonic_mean = calculate_count(data) / sum_of_reciprocals
    return harmonic_mean

def calculate_variance(data):
    if len(data) == 0:
        raise ValueError("Cannot calculate variance of an empty list")
    mean = calculate_mean(data)
    squared_differences_sum = sum((x - mean) ** 2 for x in data)
    variance = squared_differences_sum / calculate_count(data)
    return variance

def calculate_std_dev(data):
    if len(data) == 0:
        raise ValueError("Cannot calculate standard deviation of an empty list")
    # Standard deviation is the square root of variance
    return math.sqrt(calculate_variance(data))
