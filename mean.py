def calculate_mean(numbers):
  return sum(numbers) / len(numbers)

data_points = [100, 200, 300]
the_mean = calculate_mean(data_points)

print(f"numbers: {data_points}")
print(f"calculated mean: {the_mean}")