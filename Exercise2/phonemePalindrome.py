# NOTE:
# There is one (1) minor revision and one (1) block of code added.
# 1.) replaced the ".split()" with ".replace()" at line 34
# 2.) added the codes from line 19 to line 25

def phonemePalindrome(words, soundpairs):
    stringify_lst = ''.join(soundpairs)
    phoneme = ""

    if (words == words[::-1]):
        return True
    elif (words != words[::-1]):
        for i in range(len(words)):
            for pair in soundpairs:
                if words[i] in pair:
                    phoneme += words[i]
    
    # Added (from here)
    if (len(phoneme) >= 2):
        if all(chars in sorted(stringify_lst) for chars in sorted(phoneme)):
            return True
        else:
            return False
    else:
        return False
    # (to here)

while True:
    print()

    inp1 = int(input("Enter a number: "))
    # Store the inputted characters into a string (List comprehension for shorter syntax)
    # Used '_' as throwaway variable
    soundpairs = [input().replace(" ", "") for _ in range(inp1)]   # Revised

    print()

    inp2 = int(input("Enter another number: "))
    # Store the inputted characters into a string (List comprehension for shorter syntax)
    # Used '_' as throwaway variable
    stringsToCheck = [input() for _ in range(inp2)]

    print()

    for i in stringsToCheck:
        isPhoneme = phonemePalindrome(i, soundpairs)
        print(f"{i} {' YES' if isPhoneme == True else ' NO'}")