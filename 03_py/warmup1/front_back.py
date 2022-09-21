# Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
  if len(str) <= 1:
      return str
  return str[-1] + str[1:-1] + str[0]

if __name__ == "__main__":
	print(f"{front_back('code')} → 'eodc'")
	print(f"{front_back('a')} → 'a'")
	print(f"{front_back('ab')} → 'ba'")

