import math
print('Welcome to the tip calculator.')
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage of tip you like to give? 10, 12, or 15? "))
split = int(input('How many people to splite the bill? '))
percentage = tip/100 * bill + bill
pay = str(round(percentage/split, 2))
print('Ech person should pay :'+pay)