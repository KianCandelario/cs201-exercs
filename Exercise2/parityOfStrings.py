import operator

def parityOfString(word):
    # Sort the word
    alphabetical_order = sorted(word)
    lst = []

    for i in range(0, len(alphabetical_order)):
        # Counts every occurence of the character 
        # then appends it to the list
        lst.append(operator.countOf(alphabetical_order, alphabetical_order[i]))
    return lst

word = input("Enter the word: ")

checker = set(parityOfString(word))
convertedLst = list(checker)

evenFlag = False
oddFlag = False
for i in range(len(convertedLst)):
    if (convertedLst[i] % 2 == 0):
        evenFlag = True
    elif (convertedLst[i] % 2 != 0):
        oddFlag = True

if (evenFlag == True and oddFlag == True):
    print("Output: 2")
elif (evenFlag == True and oddFlag == False):
    print("Output: 0")
elif (evenFlag == False and oddFlag == True):
    print("Output: 1")