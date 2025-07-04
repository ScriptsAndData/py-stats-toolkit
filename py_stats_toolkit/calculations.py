"""
This module provides a collection of functions for performing
basic statistical calculations on lists of numbers.

Functions include:
- Count
- Sum
- Mean (Arithmetic Average)
- Minimum
- Maximum
- Harmonic Mean
- Variance
- Standard Deviation
"""

import math

def calculate_count(data):
    """
    Calculates the number of elements in a given list.

    Args:
        data (list): The list of numbers.

    Returns:
        int: The total number of elements in the list.
    """
    return len(data)

def calculate_sum(data):
    """
    Calculates the sum of all numerical elements in a given list.

    Args:
        data (list): The list of numbers.

    Returns:
        (int, float): The total sum of the elements.
    """
    total_sum = 0
    for num in data:
        total_sum += num
    return total_sum

def calculate_mean(data):
    """
    Calculates the arithmetic mean (average) of a list of numbers.

    Args:
        data (list): The list of numbers.

    Returns:
        float: The arithmetic mean of the list.

    Raises:
        ValueError: If the input list is empty.
    """
    if not data:  # More Pythonic way to check for empty list
        raise ValueError("Cannot calculate average of an empty list")
    return calculate_sum(data) / calculate_count(data)

def calculate_min(data):
    """
    Finds the minimum value in a list of numbers.

    Args:
        data (list): The list of numbers.

    Returns:
        (int, float): The minimum value found in the list.

    Raises:
        ValueError: If the input list is empty.
    """
    if not data:
        raise ValueError("Cannot find minimum value of an empty list")

    min_val = data[0]
    for num in data[1:]: # Start from the second element
        min_val = min(min_val, num)
    return min_val

def calculate_max(data):
    """
    Finds the maximum value in a list of numbers.

    Args:
        data (list): The list of numbers.

    Returns:
        (int, float): The maximum value found in the list.

    Raises:
        ValueError: If the input list is empty.
    """
    if not data:
        raise ValueError("Cannot find maximum value of an empty list")

    max_val = data[0]
    for num in data[1:]: # Start from the second element
        max_val = max(max_val, num)
    return max_val

def calculate_harmonic_mean(data):
    """
    Calculates the harmonic mean of a list of positive numbers.

    The harmonic mean is the reciprocal of the arithmetic mean of the
    reciprocals of the data points. It is typically used for rates or ratios.

    Args:
        data (list): The list of positive numbers.

    Returns:
        float: The harmonic mean of the list.

    Raises:
        ValueError: If the input list is empty or contains non-positive numbers.
    """
    if not data:
        raise ValueError("Cannot calculate harmonic mean of an empty list")
    if any(num <= 0 for num in data):
        raise ValueError("Harmonic mean requires all data points to be positive and non-zero.")

    sum_of_reciprocals = sum(1 / num for num in data)
    harmonic_mean = calculate_count(data) / sum_of_reciprocals
    return harmonic_mean

def calculate_variance(data):
    """
    Calculates the sample variance of a list of numbers.

    Args:
        data (list): The list of numbers.

    Returns:
        float: The variance of the list.

    Raises:
        ValueError: If the input list is empty.
    """
    if not data:
        raise ValueError("Cannot calculate variance of an empty list")
    mean = calculate_mean(data)
    squared_differences_sum = sum((x - mean) ** 2 for x in data)
    variance = squared_differences_sum / calculate_count(data)
    return variance

def calculate_std_dev(data):
    """
    Calculates the standard deviation of a list of numbers.

    Standard deviation is the square root of the variance. It measures
    the amount of variation or dispersion of a set of values.

    Args:
        data (list): The list of numbers.

    Returns:
        float: The standard deviation of the list.

    Raises:
        ValueError: If the input list is empty.
    """
    if not data:
        raise ValueError("Cannot calculate standard deviation of an empty list")
    return math.sqrt(calculate_variance(data))
