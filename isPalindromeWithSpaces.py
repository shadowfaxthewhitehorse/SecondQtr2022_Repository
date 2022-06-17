# Python Program
#
# A program to check whether the string entered is a palindrome.
#
# ESPERANTO:
#
# Programo por kontroli ĉu la enigita ĉeno estas palindromo.

def isPalindrome(string):

    first_ptr = 0
    last_ptr = len(string) - 1

    if(last_ptr < 0):
        return False
    elif(last_ptr == 0):
        return True
    else:
        while(first_ptr < last_ptr):
            if(string[first_ptr] != string[last_ptr]):
                return False
            first_ptr += 1
            last_ptr -= 1

        return True

# test cases
print("tests for isPalindrome() - for a word")

print(isPalindrome('aza'))
print(isPalindrome('azza'))
print(isPalindrome('mazza'))
print(isPalindrome('mazzam'))

# more test cases
print(isPalindrome('ablewasiereisawelba'))

def isPalindromeWithSpace(string):
    string_sp1 = string.lower().split(" ")

    string_sp2 = ""
    for word in string_sp1:
        string_sp2 += word.strip("?.!")

#    string_sp1 = " ".join(string_sp2)

    return isPalindrome(string_sp2)

# test cases
print("tests for isPalindrome() - for a string")

print(isPalindromeWithSpace('aza'))
print(isPalindromeWithSpace('azza'))
print(isPalindromeWithSpace('mazza'))
print(isPalindromeWithSpace('mazzam'))

# more test cases
print(isPalindromeWithSpace('able was i ere i saw elba'))
print(isPalindromeWithSpace('Able was I ere I saw Elba.'))
print(isPalindromeWithSpace('Able was I ere I saw Elba. - Napoleon'))
