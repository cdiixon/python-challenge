PyBank Breakdown:

•	Import both the os and csv to be used in the python script

•	Designate the file path for our resources files (budget_data_csv = os.path.join("C:\\Users\\cdiix\\OneDrive\\Desktop\\python-challenge\\PyBank\\Resources\\budget_data.csv"). I know I should be able to designate the file path without using the entire pathway but for some reason it wouldn’t work for me I apologize and hope that is okay!

•	Set and define all variables

•	Direct the script to open the csv file and ensure it loops all rows of data

•	Calculate the Total Months/Total Value

•	Calculate the change in profit/losses by month and calculate the average change. (For some reason my formula to calculate average change gives out a different value then the example on the module challenge. As far as I can tell the formula should be correct: Average_Value = sum(List_Of_Value_Change)/len(List_Of_Value_Change).Plus all the other data is accurate so I couldn’t figure out how to fix it/where I went wrong my apologies)

•	Calculate the greatest increase/decrease in profits

•	Print the results to the active terminal as well as exporting the results into a txt.file

•	In conclusion the:
  	     
Total Months: 86

Total: $22564198

Average Change: $4448 (as mentioned previously different than the example for some reason)

Greatest Increase in Profit: Aug-16 ($1862002)

Greatest Decrease in Profit: Feb-14 ($-1825558)




PyPoll Breakdown:

•	Import both the os and csv to be used in the python script

•	Designate the file path for our resources files (election_data_csv = os.path.join("C:\\Users\\cdiix\\OneDrive\\Desktop\\python-challenge\\PyPoll\\Resources\\election_data.csv"). I know I should be able to designate the file path without using the entire pathway but for some reason it wouldn’t work for me I apologize and hope that is okay!

•	Set and define all variables

•	Direct the script to open the csv file and ensure it loops all rows of data

•	Calculate the total votes

•	Create a dictionary to hold all relevant data within our resource file

•	Take key values from new dictionary and append them into the created lists for candidates and votes by candidate

•	Calculate the vote percent in another new list and round to the 3rd decimal place

•	Clean up the data from our lists to store all 3 in a single tuple (Data_Cleanup)

•	Calculate the winner from the new tuple

•	Print the results to the active terminal as well as exporting the results into a txt.file

•	In conclusion the:

Total Votes: 369711

Charles Casper Stockham: 23.049% (85213)

Diana DeGette: 73.812% (272892)

Raymon Anthony Doane: 3.139% (11606)

Winner: Diana Degette

