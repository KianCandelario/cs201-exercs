# Kian Candelario
def palindrome(word):
    inp_word = word.lower()
    reversed_word = word[::-1].lower()

    if (reversed_word == inp_word):
        return True
    else:
        return False

word = input("Input word: ")

if (palindrome(word) == True):
    print("")
    print("The word is a palindrome :)")
else:
    print("")
    print("The word is not a palindrome :(")