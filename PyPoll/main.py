# import csv and os
import csv
import os

# path to election data
election_data_csv = os.path.join("Resources", "election_data.csv")

#path to the text file that will be created with the analysis results
electionAnalysis = os.path.join("analysis", "election_analysis.txt")

# open/read the csv file
with open(election_data_csv, 'r') as csvFile:

    # use reader(); delimiter should be set as ','
    electionDataReader = csv.reader(csvFile, delimiter=',')

    # parse out the header and store it in a variable
    electionDataHeader = next(electionDataReader)
    
    # set variables and lists to be used in the for loop
    totalVotes = 0 # variable for the total number of votes
    candidates = [] # an empty list to hold the names of the candidates
    candidate1Votes = 0 # variable for the votes for candidate 1
    candidate2Votes = 0 # variable for the votes for candidate 2
    candidate3Votes = 0 # variable for the votes for candidate 3

    # for loop to go through each row in the file
    for row in electionDataReader:

        # keep a running count of the total number of votes
        totalVotes += 1
        
        # set the candidate's name to be found in the third column
        candidateName = row[2]

        # a conditional to add each candidate's name to the list, without repeating candidates
        if candidateName in candidates:
            candidates = candidates # keeps the list the same if the name is not a new candidate
        else:
            candidates.append(candidateName) # adds the new candidate's name to the list
            # print(len(candidates)) showed that there were 3 candidates in the list
        
        # conditional to keep a running count of votes for each specific candidate
        if candidateName == candidates[0]:
            candidate1Votes += 1
        elif candidateName == candidates[1]:
            candidate2Votes += 1
        elif candidateName == candidates[2]:
            candidate3Votes += 1

    # Determine the percentage of votes each candidate won
    candidate1VotePercent = round(candidate1Votes / totalVotes * 100, 3)
    candidate2VotePercent = round(candidate2Votes / totalVotes * 100, 3)
    candidate3VotePercent = round(candidate3Votes / totalVotes * 100, 3)

    # create a list with the number of votes
    voteList = [candidate1Votes, candidate2Votes, candidate3Votes]

    # find the max amount of votes
    voteListMax = max(voteList)

    # zip the candidate list and vote list
    candidateVoteList = list(zip(candidates, voteList))

    
    # Determine the winner of the election\
    # for loop that goes through the list candidateVoteList
    for candidate in candidateVoteList:
        # conditional to find the max and place the candidate with the max amount of votes in the election winner variable
        if candidate[1] == voteListMax:
            electionWinner = candidate[0]
            


    # print the results in the terminal
    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {totalVotes}")
    print("------------------------")
    print(f"{candidates[0]}: {candidate1VotePercent}% ({candidate1Votes})")
    print(f"{candidates[1]}: {candidate2VotePercent}% ({candidate2Votes})")
    print(f"{candidates[2]}: {candidate3VotePercent}% ({candidate3Votes})")
    print("------------------------")
    print(f"Winner: {electionWinner}")
    print("------------------------")

# open the analysis file in writing mode
with open(electionAnalysis, 'w') as textFile:

    # the ouput that should be written in the analysis file
    output = "Election Results\n"
    output += "------------------------\n"
    output += f"Total Votes: {totalVotes}\n"
    output += "------------------------\n"
    output += f"{candidates[0]}: {candidate1VotePercent}% ({candidate1Votes})\n"
    output += f"{candidates[1]}: {candidate2VotePercent}% ({candidate2Votes})\n"
    output += f"{candidates[2]}: {candidate3VotePercent}% ({candidate3Votes})\n"
    output += "------------------------\n"
    output += f"Winner: {electionWinner}\n"
    output += "------------------------\n"

    # write the data in the analysis file
    textFile.write(output)