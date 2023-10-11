'''
    MAIN TASK:
        Create a program that will implement CRUD using MySQL in Python
    FURTHER DETAILS:
        - CRUD (Create, Read, Update, Delete)

    Leader: Candelario, Kian I.
    Member: Antanoy, Vincent C.
'''


####### IMPORT MODULES
import mysql.connector as connector # mysql connector
from prettytable import PrettyTable # for aesthetic purposes of table printing :D



####### SETTING PROJECT CONFIGURATION
configs = {
    # Parameters
    "user": "root",
    "host": "localhost",
    "database_name": "inventory_db",
    "table_name": "inventory",
    "column1": "ProductID",
    "column2": "ProductName",
    "column3": "UnitPrice",
    "column4": "CostPrice",
    "column5": "StockQuantity",
    "column6": "DateAdded"
}

####### CONSTANT VARIABLES
DATABASE = connector.connect(
    host = configs["host"],
    user = configs["user"],
    database = configs["database_name"]
)
CURSOR = DATABASE.cursor()

### FIRST AND FOREMOST. Here's how I created the database and table: 
    # Database
        # query = f"CREATE DATABASE {configs['database_name']}"

        # CURSOR.execute(query)
    # Table
        # query = f"CREATE TABLE {configs['table_name']} ({configs['column1']} INT NOT NULL AUTO_INCREMENT, {configs['column2']} VARCHAR(255) NOT NULL, {configs['column3']} INT UNSIGNED NOT NULL, {configs['column4']} INT UNSIGNED NOT NULL, {configs['column5']} INT UNSIGNED NOT NULL, PRIMARY KEY({configs['column1']}))"

        # CURSOR.execute(query)

        # I also added the 6th column (DateAdded) by altering the table (directly in mysql, not in Python):
            # ALTER TABLE inventory ADD COLUMN DateAdded date NOT NULL DEFAULT CURDATE() AFTER StockQuantity



####### FUNCTIONS 
#### (CRUD)
# Create record (C)
def createRecord(value2, value3, value4, value5):
    query = f"INSERT INTO {configs['table_name']} ({configs['column2']}, {configs['column3']}, {configs['column4']}, {configs['column5']}) VALUES (%s, %s, %s, %s)"

    CURSOR.execute(query, (value2, value3, value4, value5))
    DATABASE.commit()
    print("\tRecord was successfully created!")
    print()

# Read table (R)
def readTable():
    TABLE = PrettyTable([configs['column1'], configs['column2'], configs['column3'], configs['column4'], configs['column5'], configs['column6']])

    query = f"SELECT * FROM {configs['table_name']}"
    CURSOR.execute(query)

    ROWS = CURSOR.fetchall()
    for row in ROWS:
        TABLE.add_row(row)

    print()
    print()
    print("\t\t\t  --- YOUR INVENTORY ---")
    print(TABLE)
    print()

# Update table (U)
def updateRecord():
    print()
    print()
    print("\t\t——————————————— YOU'RE UPDATING A RECORD ———————————————")
    validCols = [configs["column2"], configs["column3"], configs["column4"], configs["column5"], configs["column6"]]
    intCols = [configs["column3"], configs["column4"], configs["column5"]] # columns with int data type
    newValue = ""

    readTable()

    prodId = int(input("\tEnter the ProductID of the product you wish to [UPDATE]: "))
    while True:
        print()
        print("\tNOTE: Case Sensitive")
        colToUpdate = input("\tEnter the column you wish to update: ")
        if (colToUpdate in validCols):
            if (colToUpdate in intCols):
                print()
                newValue = int(input("\tEnter the new value: "))
                print()

                update(colToUpdate, newValue, prodId)
                break

            elif (colToUpdate == configs["column6"]):
                print()
                print("\tINPUT IN THIS FORMAT: YYYY-MM-DD")
                newValue = input("\tEnter the new value: ")
                print()

                update(colToUpdate, newValue, prodId)
                break

            elif (colToUpdate == configs["column2"]):
                print()
                newValue = input("\tEnter the new value: ")
                print()

                update(colToUpdate, newValue, prodId)
                break
        else:
            print()
            print("Can't change the column. Please try again.")
            print()
            continue
    print()
    print("\tThe inventory was updated successfully. Here's the updated inventory.")
    readTable()

# Delete table (D)
def deleteRecord():
    print()
    print()
    print("\t\t——————————————— YOU'RE DELETING A RECORD ———————————————")
    readTable()

    prodId = int(input("\tEnter the ProductID of the product you wish to [DELETE]: "))

    query=f"DELETE FROM {configs['table_name']} WHERE {configs['column1']} = {prodId}"
    CURSOR.execute(query)
    DATABASE.commit()

    print()
    print("\tThe record was deleted successfully. Here's the updated inventory.")
    readTable()

#### Other functions
def inputVerifier(userInput):
    validInput = ["c", "r", "u", "d", "e"]
    if (userInput in validInput):
        return True
    else:
        return False

def update(colUpdate, newValue, prodId):
    if colUpdate == configs["column6"]:
        query = f"UPDATE {configs['table_name']} SET {colUpdate} = '{newValue}' WHERE ProductID = {prodId}"
        CURSOR.execute(query)
        DATABASE.commit()
    else:
        query = f"UPDATE {configs['table_name']} SET {colUpdate} = %s WHERE ProductID = %s"
        CURSOR.execute(query, (newValue, prodId))
        DATABASE.commit()

def create():
    print()
    print()
    print("\t\t——————————————— YOU'RE CREATING A RECORD ———————————————")
    productName = ""
    unitPrice = 0
    costPrice = 0
    stockQuantity = 0

    print()
    productName = str(input("Enter the product name: "))
    unitPrice = int(input("Enter the unit price: "))
    costPrice = int(input("Enter the cost price: "))
    stockQuantity = int(input("Enter the current quantity: "))
    ## NOTE:
    # The default value of the DateAdded field is the current date. 
    # That's why I did not include it in the user inputs :).
    # But the user can manually change it by UPDATING it.
    print()

    return productName, unitPrice, costPrice, stockQuantity

def programRun(userInp):
    match userInp:
        case "c":
            productName, unitPrice, costPrice, stockQuantity = create()
            createRecord(productName, unitPrice, costPrice, stockQuantity)
        case "r":
            readTable()
        case "u":
            updateRecord()
        case "d":
            deleteRecord()



####### Taking user inputs
welcomeUser = input('''
            --- Inventory Database ---
                        
    Press the following key to perform an activity...
        
            [C] Create a Record
            [R] Read/Print the Table
            [U] Update a Record
            [D] Delete a Record
            [E] Exit the program 
                            
            Enter your choice: ''').lower()
    
    # Verify if the input is valid
if ((inputVerifier(welcomeUser) == True) and (welcomeUser == "e")):
    print()
    print("Exiting the program...")
    print()

elif (inputVerifier(welcomeUser) == True): 
    programRun(welcomeUser)

else:
    print()
    print("————————————————————————————————")
    print("Invalid Input. Please try again")
    print("————————————————————————————————")
    print()