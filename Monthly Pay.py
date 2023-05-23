# Users can input workers’ name when they come to work. Total number of days working per month will be saved. 
# Double rate for working on Sat and Sun.

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
        'CREATE TABLE timesheet (id INT AUTO_INCREMENT PRIMARY KEY, `Name` VARCHAR(255), `Check-in` DATETIME, DayCount INT)')
except mysql.connector.errors.ProgrammingError:
    print()

lstOfTuples = []

name = input('Enter your name: ')
while name != '':
    check_in = input('Enter your check-in time: ')

    my_checkIn = datetime.strptime(check_in, '%d-%m-%Y %H:%M')

    dayOfWeek = my_checkIn.strftime('%a')

    dayCount = 1

    if dayOfWeek in ['Sat', 'Sun']:
        dayCount = 2

    lstOfTuples.append((name, my_checkIn, dayCount))

    name = input('Enter your name: ')

my_cursor.executemany('INSERT INTO timesheet (`Name`, `Check-in`, DayCount) VALUES (%s, %s, %s)', lstOfTuples)

my_db.commit()

my_cursor.execute(
    'SELECT timesheet.`Name`, MONTH(`Check-in`) AS Month, SUM(DayCount) AS TotalEquivalentDays, PayRate * 8 * SUM(DayCount) AS MonthlyPay FROM timesheet INNER JOIN workers ON timesheet.`Name` = workers.`Name` GROUP BY `Name`, Month')


# Bonus: Within 3 months of perfect attendance, 5% of standard salary will be awarded.

lstOfPays = my_cursor.fetchall()

pay_name = input("Enter your name to see your pay-cheque: ")
pay_month = int(input("Enter the month you want to see your pay-cheque: "))

if pay_month not in (3, 6, 9, 12):
    for z in lstOfPays:
        if pay_name in z and pay_month in z:
            print('You will get paid $', z[3], 'on the last Friday of this month.')
            break
else:
    pay1 = 0
    days3M = 0

    for z in lstOfPays:
        if pay_name in z and z[1] in (pay_month-2, pay_month-1, pay_month):
            days3M += z[2]
            if z[1] == pay_month:
                pay1 = z[3]

    if days3M >= 60:
        print('You will get paid $', pay1, 'with a bonus of', 5/100 * pay1, 'on the last Friday of this month.')
    else:
        print('You will get paid $', pay1, 'on the last Friday of this month.')
