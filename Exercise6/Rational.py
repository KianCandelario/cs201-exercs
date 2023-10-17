from Fractions import Fractions

# Create instance
fraction = Fractions()
'''
    Methods inside Fractions:
        printFraction - for printing the fraction
        reduceToLowestTerm - for reducing the fraction to its lowest form
        multiply - for multiplying two fractions
        compare - returns true if the fractions are equal. Otherwise, returns false
'''

def takeUserInput():
    print()
    print("[FIRST FRACTION]")
    numerator1 = int(input("Enter the numerator: "))
    denominator1 = int(input("Enter the denominator: "))
    print(f"Your fraction: {fraction.printFraction(numerator1, denominator1)}")

    print()

    print()
    print("[SECOND FRACTION]")
    numerator2 = int(input("Enter the numerator: "))
    denominator2 = int(input("Enter the denominator: "))
    print(f"Your fraction: {fraction.printFraction(numerator2, denominator2)}")

    print()

    return numerator1, numerator2, denominator1, denominator2

while True:
    print()
    print()
    userInp = int(input('''
        --- Multiply or Compare Fractions ---
                Press [1] to Multiply
                Press [2] to Compare
                Press [0] to Exit
                Enter your choice: '''))

    if (userInp == 1):
        numerator1, numerator2, denominator1, denominator2 = takeUserInput()

        print(f"Final answer (in lowest form): {fraction.multiply(numerator1, denominator1, numerator2, denominator2)}")

    elif (userInp == 2):
        numerator1, numerator2, denominator1, denominator2 = takeUserInput()
        fraction1 = fraction.printFraction(numerator1, denominator1)
        fraction2 = fraction.printFraction(numerator2, denominator2)
        isEqual = fraction.compare(fraction1, fraction2)

        print(f"Comparing: {fraction.printFraction(numerator1, denominator1)} and {fraction.printFraction(numerator2, denominator2)}")

        if (isEqual == True):
            print("ANSWER: The fractions are equal.")
        else:
            print("ANSWER: The fractions are not equal")
    elif (userInp == 0):
        print()
        print("\tExiting the program...")
        break
    else:
        print()
        print("\tInvalid Input. Please try again.")
        print()
        continue