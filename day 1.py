# Step 1: Data
data = [10, 12, 15, 18, 20]


# Step 2: Mean function
def calculate_mean(numbers):
    total = 0
    count = 0

    for value in numbers:
        total += value
        count += 1

    mean = total / count
    return mean


# Step 3: Variance function
def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    squared_diff_sum = 0
    count = 0

    for value in numbers:
        diff = value - mean
        squared_diff_sum += diff ** 2
        count += 1

    variance = squared_diff_sum / count
    return variance


# Step 4: Function calls
mean_value = calculate_mean(data)
variance_value = calculate_variance(data)

print(f"The mean is {mean_value}")
print(f"The variance is {variance_value}")
