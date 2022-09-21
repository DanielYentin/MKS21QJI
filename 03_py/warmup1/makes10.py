# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

def makes10(a, b):
  if (a == 10 or b == 10) or a + b == 10:
    return True
  else:
    return False

if __name__ == "__main__":
	print(f"{makes10(9, 10)} → True")
	print(f"{makes10(9, 9)} → False")
	print(f"{makes10(1, 9)} → True")
