import pandas as pd
import matplotlib.pyplot as plt

# Dataframes
df1 = pd.read_excel('./dataset.xlsx', sheet_name='PieSheet')
df2 = pd.read_excel('./dataset.xlsx', sheet_name='BarSheet')
df3 = pd.read_excel('./dataset.xlsx', sheet_name='LineSheet')

pie_chart_data = df1.loc[:, ['Cheese Type','Number of People']]
bar_graph_data = df2.loc[:, ['Item', 'UK', 'France', 'USA', 'Germany']]
line_chart_data = df3.loc[:, ['Day', 'Pounds']]

# Pie Chart graph
def show_pie():
    pie_data = pie_chart_data['Number of People'].to_list()
    pie_labels = pie_chart_data['Cheese Type'].to_list()

    plt.pie(pie_data, labels=pie_labels, autopct='%1.1f%%')
    plt.title('Favorite Cheese Type')
    plt.show()

# Bar Graph
def show_bar():
    bar_graph_data.set_index('Item', inplace=True)

    bar_graph_data.plot(kind='bar', figsize=(10, 6), rot=40, fontsize=5)

    plt.xlabel('Item')
    plt.ylabel('Values')
    plt.title('Bar Graph of Preferred Chocolate by Country')

    plt.show()

# Line Chart
def show_line():
    plt.plot(line_chart_data['Day'], line_chart_data['Pounds'], marker='o', linestyle='-', color='b', label='Pounds')

    plt.xlabel('Day')
    plt.ylabel('Pounds')
    plt.title('Pounds per Day')

    plt.legend()
    plt.show()



### Menu
user_inp = int(input("""
    Select the number that you want to generate
      
    [1] Pie Chart
    [2] Bar Graph
    [3] Line Chart
      
    Enter the number: """))

### Switch statement
match(user_inp):
    case 1:
        show_pie()
    case 2:
        show_bar()
    case 3:
        show_line()
    case _:
        print()
        print("You entered an invalid input. Please try again.")