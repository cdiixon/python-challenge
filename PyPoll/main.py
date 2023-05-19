import os
import csv

#designate file path
election_data_csv = os.path.join("C:\\Users\\cdiix\\OneDrive\\Desktop\\python-challenge\\PyPoll\\Resources\\election_data.csv")

#set and define all variables in the order they appear
Total_Votes = 0
Final_Votes = {}
Candidates = []
Votes_by_Candidate = []
Vote_Percent = []
Winner_List = []

#direct the script to the csv file
with open(election_data_csv) as csvfile:
    csvreader = csv.DictReader(csvfile)

    #ensure all rows are being looped through
    for row in csvreader:
       
       #calculate total votes
        Total_Votes += 1

        #creates a dictionary for all relevant data using each candidate once.
        if row["Candidate"] in Final_Votes.keys():
            Final_Votes[row["Candidate"]] = Final_Votes[row["Candidate"]] + 1
        else:
            Final_Votes[row["Candidate"]] = 1

    #takes keys/values from the created dictionary and stores them in the pre-created lists
    for key, value in Final_Votes.items():
        Candidates.append(key)
        Votes_by_Candidate.append(value)

    #calculate vote percent
    for n in Votes_by_Candidate:
        Vote_Percent.append(round(n/Total_Votes*100, 3))

    #store our 3 lists in a single tuple using list(zip)
    Data_Cleanup = list(zip(Candidates, Votes_by_Candidate, Vote_Percent))

    #calculate the winner of the vote using our newly created tuple
    for name in Data_Cleanup:
        if max(Votes_by_Candidate) == name[1]:
            Winner_List.append(name[0])
    
    #define the winner as a string for exporting to text file
    Winner = Winner_List[0]

#export results into a text file
Text_Path = os.path.join("C:\\Users\\cdiix\\OneDrive\\Desktop\\python-challenge\\PyPoll\\Analysis\\PyPollResults.txt")

with open(Text_Path, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(Total_Votes) + '\n-------------------------\n')
    for item in Data_Cleanup:
        txtfile.writelines(item[0] + ": " + str(item[2]) +'%  (' + str(item[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + Winner + '\n-------------------------')

#print file to terminal
with open(Text_Path, 'r') as readfile:
    print(readfile.read())
    


   

        



















 





    





    

