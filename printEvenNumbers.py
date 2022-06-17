# PYTHON PROGRAMMING (FOR SPEAKERS OF ESPERANTO)
#
# Write a Python program to print the even numbers from a given list.
#
# Source: https://www.w3resource.com/python-exercises/python-functions-exercise-10.php
#
# ESPERANTO:
#
#
# PITONA PROGRAMADO ( POR ESPERANTOPAROLANTOJ )
#
# Skribu Python-programon por presi la parajn nombrojn de donita listo.
#
# Fonto: https://www.w3resource.com/python-exercises/python-functions-exercise-10.php
#


def printEvenNumbers(inList):
    # find the length of the list
    inListLen = len(inList)

    if(inListLen == 0):
        return

    print("Printing the even numbers in the list....\n")
    for index in range(inListLen):
        listItem = inList[index]
        if((listItem % 2) == 0):
            print(inList[index], end = " ")

    print("\n\n~\n")
    return


def print_even_numbers_comp(l):

    print("\n\nPrinting the even numbers in the list....\n")
    for elem in l:
        if(elem % 2 == 0):
            print(elem, end = " ")





# test cases
list1 = [5,6,7,54,34,6,7,8,4,3,10]
list2 = [7, 98, 56, 45, 33, 2, 11]

list3 = list1 + list2

# non-compact version

printEvenNumbers(list1)
printEvenNumbers(list2)
printEvenNumbers(list3)

# compact version

print_even_numbers_comp(list1)
print_even_numbers_comp(list2)
print_even_numbers_comp(list3)
