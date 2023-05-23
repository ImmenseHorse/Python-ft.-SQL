
# The program allows users to input workers’ info: Name, DOB, StartDate, PayRate; and output a table displaying them.

import mysql.connector
from datetime import datetime

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Lkmmn1',
    database='k87'
)

my_cursor = my_db.cursor()

try:
    my_cursor.execute(
        'CREATE TABLE workers (id INT AUTO_INCREMENT PRIMARY KEY,`Name` VARCHAR(255), DOB DATE, StartDate DATETIME, PayRate FLOAT)')
except mysql.connector.errors.ProgrammingError:
    print()

lst_tuples = []

name = input("Please enter the new employee's name: ")

while name != '0':
    dob = input("Please enter the new employee's date of birth: ")
    my_dob = datetime.strptime(dob, "%Y-%m-%d")

    startDate = input("Please enter the new employee's start date: ")
    my_startDate = datetime.strptime(startDate, "%Y-%m-%d %H:%M")

    payRate = float(input("Please enter the new employee's pay rate: "))

    lst_tuples.append((name, my_dob, my_startDate, payRate))

    name = input("\nPlease enter the new employee's name: ")

my_cursor.executemany('INSERT INTO workers (`Name`, DOB, StartDate, PayRate) VALUES (%s, %s, %s, %s)', lst_tuples)

my_db.commit()

my_cursor.execute('SELECT * FROM workers')

lst = my_cursor.fetchall()

print()

for row in lst:
    print(row)
