#
# PYTHON CODING: Find the maximum of three numbers.
#
# Exercise: Write a Python function to find the Max of three numbers.
#
# Source: https://www.w3resource.com/python-exercises/python-functions-exercises.php
#
# ESPERANTO:
#
# Python-kodo: Trovu la maksimumon de tri nombroj.
#
# Ekzerco: Skribu programon por trovi la maksimumon de tri nombroj.
#
#

def findMaxOfThreeNumbers(a,b,c):

    max = a
    if(b > max):
        max = b
    if(c > max):
        max = c

#    print(max)
    return max

# test cases

findMaxOfThreeNumbers(1,2,4)
findMaxOfThreeNumbers(1,20,4)

findMaxOfThreeNumbers(1,24,4)
findMaxOfThreeNumbers(543,24,4)
