def calculate_median(numbers):
  
  sorted_numbers = sorted(numbers)
  n = len(sorted_numbers)

  if n % 2 == 1:
    # Odd number of elements
    return sorted_numbers[n // 2]
  else:
    # Even number of elements
    mid1 = sorted_numbers[n // 2 - 1]
    mid2 = sorted_numbers[n // 2]
    return (mid1 + mid2) / 2