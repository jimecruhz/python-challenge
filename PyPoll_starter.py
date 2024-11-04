# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

candidates = []  #list that holds the candidates in the election
candidates_votes = {} #dictionairy that will load the votes each candidate recieved 
winner_count = 0 #variable hold for winner
winning_cand = "" #variable to hold the winning candidate 
# Define lists and dictionaries to track candidate names and vote counts


# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        #add to total votes 
        total_votes += 1 

        #check to see if the candidates is in the list of candidates 
        if row[2] not in candidates:
            candidates.append(row[2])

            candidates_votes[row[2]] = 1

        else: 
            candidates_votes[row[2]] += 1
#print(candidates_votes)

voter_output = ""

for candidates in candidates_votes:
    #get the vote count and percentage of the votes
    votes = candidates_votes.get(candidates)
    votes_pct = (float(votes)/ float (total_votes)) * 100.00
    voter_output += f"\t{candidates}: {votes_pct: .3f}% ({votes: ,}) \n"

    #compare the votes to the winner count
    if votes > winner_count:
        #update votes to be the new winner count
        winner_count = votes
        #update the winning candidate 
        winning_cand = candidates

winning_cand_output = f"Winner: {winning_cand}\n-----------------------------"

    #print(voter_output)
    #print(votes)

    # Print a loading indicator (for large datasets)
print(". ", end="")


output = (
    f"\n\n Election Results\n"
    f"-----------------------------\n"
    f"\tTotal Votes: {total_votes:,}\n"
    f"-----------------------------\n"
    f"{voter_output}"
    f"-----------------------------\n"
    f"{winning_cand_output}"
)
#print to terminal 
print(output)


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    #write the output to the text file
    txt_file.write(output)
