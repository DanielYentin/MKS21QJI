# Given a string, we'll say that the front is the first 3 chars of the string.
# If the string length is less than 3, the front is whatever is there.
# Return a new string which is 3 copies of the front.

def front3(str):
  return str[:3]*3

if __name__ == "__main__":
	print(f"{front3('Java')} → 'JavJavJav'")
	print(f"{front3('Chocolate')} → 'ChoChoCho'")
	print(f"{front3('abc')} → 'abcabcabc'")
