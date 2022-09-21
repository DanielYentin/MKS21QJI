# Given an int n, return the absolute difference between n and 21,
# except return double the absolute difference if n is over 21.

def diff21(n):
  if n <= 21:
    return 21 - n
  else:
   return  2 * (n - 21)

if __name__ == "__main__":
	print(f"{diff21(19)} → 2")
	print(f"{diff21(10)} → 11")
	print(f"{diff21(21)} → 0")
