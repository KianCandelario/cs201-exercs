import pandas as pd

# Constant variable for the dataframe
DATAFRAME = pd.read_excel('./excel_dataset.xlsx')

####### Functions
def acc_n_disp():
    print()
    print(DATAFRAME)

def first_ten_rec():
    print()
    print(DATAFRAME.head(10))

def last_five_rec():
    print()
    print(DATAFRAME.tail(5))

def not_in_stock():
    print()
    print(DATAFRAME[DATAFRAME['In Stock'] == 'No'])

def asc_order_on_type():
    print()
    print(DATAFRAME.sort_values(by='Type', ascending=True))

def desc_order_on_categ():
    print()
    print(DATAFRAME.sort_values(by='Category', ascending=False))

def disp_avg_price_per_categ():
    print()
    print("Category || Average Price")
    print()
    print(DATAFRAME.groupby('Category')['Price'].mean().round(2))

def disp_num_color_per_type():
    print()
    print("Type || Number of Colours")
    print()
    print(DATAFRAME.groupby('Type')['Colour'].nunique())

####### Menu
user_inp = int(input("""
    Select the number that you want to perform
      
    [1] Access and display the data using Python
    [2] Display the first 10 records
    [3] Display the last 5 records
    [4] Show only the data that not In Stock
    [5] Display the data in ascending order based on Type
    [6] Display the data in descending order based on Category
    [7] Display the average Price per Category
    [8] Display the numbers of Colours per Type
    [0] Exit the program
      
    Enter the number: """))


### Switch statement
match(user_inp):
    case 1:
        acc_n_disp()
        print()
    case 2:
        first_ten_rec()
        print()
    case 3:
        last_five_rec()
        print()
    case 4:
        not_in_stock()
        print()
    case 5:
        asc_order_on_type()
        print()
    case 6:
        desc_order_on_categ()
        print()
    case 7:
        disp_avg_price_per_categ()
        print()
    case 8:
        disp_num_color_per_type()
        print()
    case 0:
        print()
        print("Thank you for using the program!!")
        print()
    case _:
        print()
        print("You entered an invalid input. Please try again.")
        print()