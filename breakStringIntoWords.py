# Break up a string into its constituent words
#
#
# PYTHON QUESTION.
# Python question. How do I print a string one word at a time?
#
str = "Here is a riddle. What can run but not walk?"

for word in str.split(" "):
	word = word.strip("+-*/?.!")
	print(word)

#done!
