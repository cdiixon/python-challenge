import os
import csv

#designate file path
budget_data_csv = os.path.join("C:\\Users\\cdiix\\OneDrive\\Desktop\\python-challenge\\PyBank\\Resources\\budget_data.csv")

#set and define all variables in the order they appear
Months = 0
Total_Value = 0
Change_In_Value = 0
Former_Value = 0
List_Of_Value_Change = []
Month_W_Change = []
Average_Value = 0
Greatest_Increase = [0, 0]
Greatest_Decrease = [0, 0]

#direct the script to the csv file
with open(budget_data_csv) as csvfile:
    csvreader = csv.DictReader(csvfile)

    #ensure all rows of data are being looped through
    for row in csvreader:

        #calculate the total # of months
        Months += 1

        #calculate total value of profit/losses
        Total_Value = Total_Value + int(row["Profit/Losses"])

        #calculate the changes in profit/losses
        Change_In_Value = float(row["Profit/Losses"])- Former_Value
        Former_Value = float(row["Profit/Losses"])
        List_Of_Value_Change = List_Of_Value_Change + [Change_In_Value]
        Month_W_Change = [Month_W_Change] + [row["Date"]]

        #calculate the average change in profit/losses
        Average_Value = sum(List_Of_Value_Change)/len(List_Of_Value_Change)

        #calculate the greatest increase in profit
        if Change_In_Value>Greatest_Increase[1]:
            Greatest_Increase[1] = Change_In_Value
            Greatest_Increase[0] = row['Date']

        #calculate the greatest decrease in profit
        if Change_In_Value<Greatest_Decrease[1]:
            Greatest_Decrease[1] = Change_In_Value
            Greatest_Decrease[0] = row['Date'] 

#print the results in the terminal
print('Financial Analysis:')
print('----------------------------------------------------')
print('Total Months:', Months)
print('Total:', '$',Total_Value)
print('Average Change:', "%.2f" % Average_Value)
print('Greatest Increase in Profits:', Greatest_Increase)
print('Greatest Decrease in Profits:', Greatest_Decrease)

#export results into a text file
Text_Path = os.path.join("C:\\Users\cdiix\\OneDrive\\Desktop\\python-challenge\\PyBank\\Analysis\\PyBankResults.txt")

with open(Text_Path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------------------------\n")
    file.write("Total Months: %d\n" % Months)
    file.write("Total: $%d\n" % Total_Value)
    file.write("Average Change: $%d\n" % Average_Value)
    file.write("Greatest Increase in Profits: %s ($%s)\n" % (Greatest_Increase[0], Greatest_Increase[1]))
    file.write("Greatest Decrease in Profits: %s ($%s)" % (Greatest_Decrease[0], Greatest_Decrease[1]))
    