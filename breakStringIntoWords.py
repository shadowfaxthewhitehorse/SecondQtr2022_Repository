# Break up a string into its constituent words
# ESP:
# Disrompu ŝnuron en ĝiajn konsistigajn vortojn.
#
#
# PYTHON QUESTION.
# How do I print a string one word at a time?
#
# ESP:
# Demandoj por Python-programistoj.
# 
# Kiel mi presi ĉenon unu vorton samtempe?
#
str = "Here is a riddle. What can run but not walk?"

for word in str.split(" "):
	word = word.strip("+-*/?.!")
	print(word)

#done!
