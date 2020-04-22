#import Library
import os
import csv

#Read csv files
csvpath = os.path.join("02-Homework", "03-Python", "Instructions", "Pybank", "Resources", "budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#Define Variables 
mcount = 0; total = 0; PreValue = 0; Diff = 0; DiffMax = 0; DiffMin = 0

#Print Title 
print(f'Financial Analysis')
print(f'____________________________________________________________')
print(f'')
#Find Total Months 
print(f'Total Months : {mcount}')
#The total net amount of "Profit/Losses" over the entire period
print(f'Total: $ {total}')
# Greatest increase in profit
print(f'Greatest Increase in Profits: {DiffMax} : ($ {DiffMax})')
# Greatest increase in profit
print(f'Greatest Decrease in Profits: {DiffMin} : ($ {DiffMin})')