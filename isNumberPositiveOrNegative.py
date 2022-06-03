# find out whether a number is positive, negative or zero.
#
# ESP:
# eksciu ĉu nombro estas pozitiva, negativa aŭ nula.

inum = int(input("Please enter a number:"))

if (inum > 0):
     print("The number is positive.")
elif (inum < 0):
     print("The number is negative.")
elif (inum == 0):
     print("The number is zero.")
else:
     pass


