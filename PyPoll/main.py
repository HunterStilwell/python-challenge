# import csv and os
import csv
import os

# path to election data
election_data_csv = os.path.join("Resources", "election_data.csv")

# open/read the csv file
with open(election_data_csv, 'r') as csvFile:

    # use reader(); delimiter should be set as ','
    electionDataReader = csv.reader(csvFile, delimiter=',')

    # parse out the header and store it in a variable
    electionDataHeader = next(electionDataReader)

    totalVotes = 0
    candidates = []
    candidate1Votes = 0
    candidate2Votes = 0
    candidate3Votes = 0

    for row in electionDataReader:

        totalVotes += 1
        
        candidateName = row[2]

        if candidateName in candidates:
            candidates = candidates
        else:
            candidates.append(candidateName)
        
        if candidateName == candidates[0]:
            candidate1Votes += 1
        elif candidateName == candidates[1]:
            candidate2Votes += 1
        elif candidateName == candidates[2]:
            candidate3Votes += 1

    print("Election Results")
    print('------------------------')
    print(f"Total Votes: {totalVotes}")
    print('------------------------')
    print(f"{candidates[0]}: ({candidate1Votes})")
    print(f"{candidates[1]}: ({candidate2Votes})")
    print(f"{candidates[2]}: ({candidate3Votes})")
    print('------------------------')
    print(f"Winner: ")
    print('------------------------')