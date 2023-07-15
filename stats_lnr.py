def calculate_linear_regression(x, y):
    n = len(x)

    # Calculate the mean of x and y
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    # Calculate the slope (beta1) and intercept (beta0) of the regression line
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator = sum((xi - mean_x) ** 2 for xi in x)
    beta1 = numerator / denominator
    beta0 = mean_y - beta1 * mean_x

    return beta1, beta0

# Test the function
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

slope, intercept = calculate_linear_regression(x, y)
print("Linear Regression Line:")
print("Slope:", slope)
print("Intercept:", intercept)

# ps: beta version pa lang to huhu di ko pa to masyado magets eh
