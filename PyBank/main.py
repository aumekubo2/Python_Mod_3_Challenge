
#Your analysis should look similar to the following:

  
#Financial Analysis
#  ----------------------------
  #Total Months: 86
  #Total: $22564198
  #Average Change: $-8311.11
  #Greatest Increase in Profits: Aug-16 ($1862002)
  #Greatest Decrease in Profits: Feb-14 ($-1825558)
 # ```

# -------------------------------------------
  #the results requires a 'read'/input and 'write'/outuput file
import os
import csv

# The next line is doing: file_to_read = '.\\Resources\\budget_data.csv'
file_to_read = os.path.join('..', 'Git_Personnal_Rep','Python_Challenge','Python_Mod_3_Challenge', 'PyBank', 'Resources', 'budget_data.csv')
file_to_write = os.path.join('Python_Challenge', 'Python_Mod_3_Challenge', 'PyBank', 'Analysis', 'PyBankAnalysis.txt')

  #Assign value to the variables we are going to calculate

# The total number of months included in the dataset (start from month zero and code will add the months)
total_months = 0


 #The changes in "Profit/Losses" over the entire period, and then the average of those changes - to calculate the changes you need to compare current vs. prior period // create a list to append the changes in the months and the P&L amounts for each of those months
previous_profit_losses = 0
month_of_change = []
change_profit_losses_list = []
Average_change = 0

# The net total amount of "Profit/Losses" over the entire period - the calculated net PL will be added to the list below
total = 0

# The greatest increase in profits (date and amount) over the entire period (the " " will be a placeholder for the month and year of the change, the number starts from a low value and move to a higher value)
greatest_increase = [' ',0]

#The greatest decrease in profits (date and amount) over the entire period (the " " will be a placeholder for the month and year of the change, the number starts from a higher value and move to a lower value)
greatest_decrease = [' ',999999999999999999999]

# read the file to open (open with dictonary reader as it will pick up the 1st column header (keys) and add the correspondent values related to the keys (headers))
with open(file_to_read) as budget_data:
  reader = csv.DictReader(budget_data, delimiter=",")  
  # after read the file header, read the rows (check the csv.file for the header names to determine the row to read)
  for row in reader:
    total_months = total_months + 1 #start with month 0 and add 1 as it goes through the for loop
    total =  total + int(row['Profit/losses'])

#calculate the profit-loss change by comparing the total rev. and append [] to the list above

change_profit_losses=int(row['Profit/Losses'])-previous_profit_losses
previous_profit_losses= int(row['Profit/Losses'])
change_profit_losses_list= int(row['Profit/Losses'])+change_profit_losses_list
month_of_change=month_of_change+(row("Date"))

#calculate the greatest increase Date and Amount by using an IF stmt

if(change_profit_losses > greatest_increase[1]):
  greatest_increase[0]= row["Date"]
  greatest_increase[1]=change_profit_losses


#calculate the greatest decrease Date and Amount by using an IF stmt and append index

if(change_profit_losses < greatest_decrease[1]):
  greatest_decrease [0]= row["Date"]
  greatest_decrease[1]=change_profit_losses


#calculate the greatest increase Date and Amount by using an IF stmt

Average_change = sum(change_profit_losses_list/len(change_profit_losses_list))

#create the output file
output =(
  f"nAnalysis\n"
  f"Total Months:{total_months}\n"
  f"total:(${total})\n"
  f"Average Profit Change: ${Average_change}\n"
  f"Greatest Increase in Profit: {greatest_increase[0]} (${greatest_increase[1]})\n"
  f"Greatest Decrease in Profit: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
 )

print(output)

with open(file_to_write,'w') as txt_file:
  txt_file.write(output)
