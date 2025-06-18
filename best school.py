# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'best_schools.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

menu_choice = ''
while menu_choice != 'Z':    
    menu_choice = input('Welcome to the school database\n\n'
                        'Type the letter for the information you want:\n'
                        'A: Show all the schools in the database\n'
                        'B: How many schools are private\n'
                        'C: Show all public schools\n'
                        'D: Which schools are composite schools\n'
                        'E: Which schools are only for boys\n'
                        'F: Shows all schools with more than 2000 students\n'
                        'G: Shows all the schools name and year established before 1900/n'
                        'H: Show all girls private schools\n'
                        'I: Shows all the schools from newest to oldest\n'
                        'J: Show all the schools that are for girls\n'
                        'K: Show schools with fewer than 1000 students\n'
                        'L: Which schools are public and for boys only\n'
                        'M: Which schools are private and have under 800 students\n'
                        'Z: Exit\n\nType option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice =='A':
        print_query('All schools')
    elif menu_choice == 'B':
        print_query('Private schools')
    elif menu_choice == 'C':
        print_query('Public schools')
    elif menu_choice == 'D':
        print_query('Composite schools')
    elif menu_choice == 'E':
        print_query('Gender')
    elif menu_choice == 'F':
        print_query('Population')
    elif menu_choice == 'G':
        print_query('Year established')
    elif menu_choice == 'H':
        print_query('Girls private schools')
    elif menu_choice == 'I':
        print_query('Newest to oldest')
    elif menu_choice == 'J':
        print_query('Girls school')
    elif menu_choice == 'K':
        print_query('Fewer than 1000 students')
    elif menu_choice == 'L':
        print_query('Public schools for boys')
    elif menu_choice == 'M':
        print_query('Private school have less than 800 students')


