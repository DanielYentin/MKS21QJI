# Given two int values, return their sum. Unless the two values are the same,
# then return double their sum.

def sum_double(a, b):
  if a != b:
    return a + b
  else:
  	return 2 * (a + b)

if __name__ == "__main__":
	print(f"{sum_double(1, 2)} → 3")
  	print(f"{sum_double(3, 2)} → 5")
  	print(f"{sum_double(2, 2)} → 8")
