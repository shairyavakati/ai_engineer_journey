data =(12,23,45,56,78,89,96,63,52,41,,74,85)
def calculate_mean(numbers):
    total=0
    count=0
    for value in numbers:
	total+=value
	count+=1
	mean=total/count
	return mean	
def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    total_squared_diff = 0
    count = 0

    for value in numbers:          
        diff = value - mean
        total_squared_diff += diff ** 2
        count += 1

    variance = total_squared_diff / count
    return variance
mean_value=calculate_mean(data)
variance_value=calculate_variance(data)
print("Mean:",mean_value)
print("Variance:",variance_value)