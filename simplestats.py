import math

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

def calculate_statistics(numbers):
    statistics = {}
    statistics["count"] = len(numbers)
    statistics["sum"] = sum(numbers)
    statistics["mean"] = calculate_mean(numbers)
    statistics["variance"] = calculate_variance(numbers)
    statistics["standard_deviation"] = calculate_standard_deviation(numbers)
    statistics["median"] = calculate_median(numbers)
    return statistics

if __name__ == '__main__':
    numbers = []

    # Read input numbers from the user
    while True:
        num = input("Enter a number (or 'done' to finish): ")
        if num.lower() == "done":
            break
        try:
            num = float(num)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a number or 'done' to finish.")

    # Calculate and display statistics
    statistics = calculate_statistics(numbers)
    print("Numbers:", numbers)
    for stat, value in statistics.items():
        print(stat.capitalize() + ":", value)
