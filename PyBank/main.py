# Import os module 
import os
# Import module for reading CSV files
import csv

# Get current working directory
cwkdir = os.getcwd()
print(cwkdir)
# Join File Path
filepath = os.path.join(cwkdir,"/Users/osedjan/Desktop/Homework/python-challenge/PyBank/budget_data.csv")

# Initialize variables
mcount = 0; total = 0; PreValue = 0; Diff = 0; DiffMax = 0; DiffMin = 0

# Open and read CSV file
with open(filepath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     print(f'Financial Analysis'+'\n')
     print(f'----------------------------'+'\n')
     for i in csvreader:
         month = i[0]
         Amount = i[1]
         iAmount = int(Amount)
         Diff =  iAmount - PreValue
         #Placeholder to track greatest increase in profits (financial analysis)
         if DiffMax < Diff:
            DiffMax = Diff
            DiffMaxDate = month
         #Placeholder to track greatest decrease in profits (financial analysis)
         if DiffMin > Diff:
            DiffMin = Diff
            DiffMinDate = month

         PreValue = iAmount   
         # Get total months (financial analysis)
         mcount = mcount + 1
         total += int(Amount) 

                            ## Display Results ##      
# The total number of months included in the dataset
print(f'Total Months : {mcount}')
# The total net amount of "Profit/Losses" over the entire period
print(f'Total: $ {total}')
# Greatest increase in profit
print(f'Greatest Increase in Profits: {DiffMaxDate} : ($ {DiffMax})')
# Greatest increase in profit
print(f'Greatest Decrease in Profits: {DiffMinDate} : ($ {DiffMin})')


#Exporing to .txt file
output = open("Pybank.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(mcount)}")
line4 = str(f"Total: ${str(total)}")
line5 = str(f"Average Change: ${str(round(PreValue))}")
line6 = str(f"Greatest Increase in Profits: (${str(DiffMax)})")
line7 = str(f"Greatest Decrease in Profits: (${str(DiffMin)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))