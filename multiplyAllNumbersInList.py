######
# from numbers import Number
#
#
# Write a Python function to multiply all the numbers in a list.
#
# Source: https://www.w3resource.com/python-exercises/python-functions-exercises.php
#
######
# ESPERANTO:
#
# Skribu Python-funkcion por multobligi ĉiujn nombrojn en listo.
#
# Fonto: https://www.w3resource.com/python-exercises/python-functions-exercises.php
#

def multiplyAllNumbersInList(l):

    product = 1
    for elem in l:
        if(isinstance(elem, (int, float, complex)) and not isinstance(elem, bool)):
#       if(isinstance(n, numbers.Number)):
            product *= elem

    return product

# test cases
list1 = [8, 2, 3, 1, 7]

print(multiplyAllNumbersInList(list1))

list1.append(20)

print(multiplyAllNumbersInList(list1))

list1.append(20)

print(multiplyAllNumbersInList(list1))

print(list1)
