import math

# Statistics Functions

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_variance(numbers):
    avg = calculate_mean(numbers)
    squared_diff = [(x - avg) ** 2 for x in numbers]
    return sum(squared_diff) / len(numbers)

def calculate_standard_deviation(numbers):
    return math.sqrt(calculate_variance(numbers))

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(numbers)
    if n % 2 == 0:
        mid = n // 2
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[n // 2]

# Probability Functions

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def calculate_permutation(n, r):
    return calculate_factorial(n) / calculate_factorial(n - r)

def calculate_combination(n, r):
    return calculate_factorial(n) / (calculate_factorial(r) * calculate_factorial(n - r))

def calculate_probability(n, r):
    return 1 / calculate_permutation(n, r)

if __name__ == '__main__':
    # Test the functions

    numbers = [1, 2, 3, 4, 5]
    print("Numbers:", numbers)
    print("Mean:", calculate_mean(numbers))
    print("Variance:", calculate_variance(numbers))
    print("Standard Deviation:", calculate_standard_deviation(numbers))
    print("Median:", calculate_median(numbers))

    print()

    n = 5
    r = 2
    print("Permutation P({}, {}):".format(n, r), calculate_permutation(n, r))
    print("Combination C({}, {}):".format(n, r), calculate_combination(n, r))
    print("Probability of selecting {} out of {}:".format(r, n), calculate_probability(n, r))
