 #PyPool Analysis - expected results:

#```text
 # Election Results
 # -------------------------
 # Total Votes: 369711
#  -------------------------
 # Charles Casper Stockham: 23.049% (85213)
 # Diana DeGette: 73.812% (272892)
 # Raymon Anthony Doane: 3.139% (11606)
#  -------------------------
 # Winner: Diana DeGette
#-------------------------
#  ```


import os
import csv

 #the results requires a 'read'/input and 'write'/outuput file
pyfile_to_read= os.path.join("Resources","election_data.csv")
pyfile_to_write= os.path.join("Analysis","PyPoll_Analysis.txt")

#assing variables and place holders for values
# 1st variable is to count for total member of votes cast
# 2nd variable is to create a list for caditates who received votes - if stmt 
# 3rd variable is to determine the % of votes for the list on step 2 (len)
# 4th is to determine the total number of votes of each candidate won - also to be used in the calc. above
# last the winner of the election based on popular vote - max function

Total_vote_cast = 0
List_of_Candidates = [] 
Votes_by_candidate = {} 
Winner_name = " "
Winner_votes_count = 0


#open the file to read the data
with open(pyfile_to_read) as election_data: 
    csvreader = csv.DictReader(election_data, delimiter ="," )

    first_row = next (csvreader)
    Total_vote_cast += 1

    for row in csvreader:
#loop through the rows, so, for each row it loops through, it will add 1 row to the total vote casted
        Total_vote_cast += 1
#loop through the rows and find the candidate name and store under the candidate name
        Candidate_name = row["Candidate"]
       
#now go through the candidates name and see if candidate is already in the list, if not...
        if Candidate_name not in List_of_Candidates:
     #add the candidate that is not in the list
         List_of_Candidates.append(Candidate_name)
    #trigger the count the votes for the candidates added to the list
         Votes_by_candidate[Candidate_name] = 0
        
    #add the votes by candidate, note, we are still under the row reader, but not under the if stmt
        Votes_by_candidate[Candidate_name] += 1

#create the output file - .txt
with open(pyfile_to_write,'w') as txt_file:
  
  #information to show in the output file
    Election_results = (
        f"\n\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes:  {Total_vote_cast}\n"
        f"-----------------------\n"
    )

    print(Election_results)

    #save the output file
    txt_file.write(Election_results)


#determine the vote count and the percentage
    for Candidate in Votes_by_candidate:
        votes = Votes_by_candidate.get(Candidate)
        vote_percentage = round((float(votes) / float(Total_vote_cast) * 100),3)
    
    #determine the winning vote and the winner
        if (votes> Winner_votes_count):
            Winner_votes_count = votes
            Winner_name = Candidate
        voter_output = f"{Candidate}: {vote_percentage}% ({votes})\n"
        print(voter_output)
        txt_file.write(voter_output)

    # print the winner candidate name
    Winner_candidate_Summary = (
            f"----------------------\n"
            f"Winner: {Winner_name}\n"
            f"----------------------\n"
    )
    print(Winner_candidate_Summary)

    txt_file.write(Winner_candidate_Summary)