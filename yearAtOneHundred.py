# Python code: "Year you will turn 100" problem
#
# Spot the bug in the code
#
# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old. 
# Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year).
#


def yearAt100():
	istr = str(input("Please enter your name: "))

	inum = int(input("Please enter your age: "))

	if((inum <= 0) or (inum > 200)):
		print("Please enter an age between 1 and 200.")
		return
	
	year_at_100 = 2032 - inum 
	
	print("In the year %s, you will be a hundred years old." % year_at_100)
	
	return

yearAt100()
