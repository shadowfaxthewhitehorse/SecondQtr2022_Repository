#
# find the first digit of a number (code in Python)
#
# -*- coding: utf-8 -*-
"""FindFirstDigit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ChzB9o_AUWOwy5PTakEN7KvnCuzV801N
"""

# find the first digit of a number (in Python)

number = int(input("Enter a number"))

if(number <= 0):
  number = - number

if(number < 10):
  first_digit = number
else:  
  while(number >= 10):
    number = number // 10
  first_digit = number

print(first_digit)