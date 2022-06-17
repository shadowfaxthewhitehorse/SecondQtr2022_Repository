# from numbers import Number
#
#
# Write a Python function to sum all the numbers in a list.
#
# Source: https://www.w3resource.com/python-exercises/python-functions-exercises.php
#
def sumAllNumbersInList(l):

    sum = 0
    for elem in l:
        if(isinstance(elem, (int, float, complex)) and not isinstance(elem, bool)):
#       if(isinstance(n, numbers.Number)):
            sum += elem

    return sum

# test cases
list1 = [8, 2, 3, 0, 7]

print(sumAllNumbersInList(list1))

list1.append(20)

print(sumAllNumbersInList(list1))

list1.append(20)

print(sumAllNumbersInList(list1))

print(list1)
