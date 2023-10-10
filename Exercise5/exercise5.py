##### Functions
# Read
def readFile(path, method):
    # Open file
    file = open(path, method)
    fileContents = file.read()
    print("----- FILE CONTENTS -----")
    print(fileContents)
    print()

# Write
def writeFile(path, method, data):
    # Open file
    file = open(path, method)
    file.write(data)
    file.close()
    
    print()
    readFile(path, "r")
    print()

# Append
def appendFile(path, method, data):
    # Open file
    file = open(path, method)
    file.write('\n' + data)
    file.close()
    
    print()
    readFile(path, "r")
    print()



PATH = "C:/Users/acer/Desktop/Intelligent Systems/Exercise5/file.txt"
method = input('''
    Select your method
    
    [R] for Read
    [W] for Write
    [A] for Append: ''').lower()

match method:
    case "r":
        print()
        readFile(PATH, method)
    case "w":
        print()
        print("--- You're overwriting a file ---")
        data = input("Enter your data: ")
        writeFile(PATH, method, data)
    case "a":
        print()
        print("--- You're appending a file ---")
        data = input("Enter your data: ")
        appendFile(PATH, method, data)
    case _:
        print("————————————————————————————————")
        print("Invalid Input. Please try again")
        print("————————————————————————————————")