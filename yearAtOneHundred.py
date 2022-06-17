# Python code: "Year you will turn 100" problem
#
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
