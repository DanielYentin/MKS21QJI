# The parameter weekday is True if it is a weekday, and the parameter vacation is True 
# if we are on vacation. We sleep in if it is not a weekday or we're on vacation. 
# Return True if we sleep in.

def sleep_in(weekday, vacation):
	return not weekday or vacation

if __name__ == "__main__":
	print(f"{sleep_in(False, False)} → True")
	print(f"{sleep_in(True, False)} → False")
	print(f"{sleep_in(False, True)} → True")
