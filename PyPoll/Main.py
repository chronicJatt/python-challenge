# Create a Python script that analyzes the votes and calculates each of the following:
    # The total number of votes cast,
    # A complete list of candidates who received votes,
    # The percentage of votes each candidate won,
    # The total number of votes each candidate won,
    # The winner of the election based on popular vote.
# Finally, print the analysis to terminal and export to text file.

# Module importation
import os
import csv

# Variables, lists & dictionaries
total_votes = 0
candidates = []
poll_data = {}
vote_percentages = []
winner = []
winner_count = 0
i = 0

# Path to csv
poll_csv = os.path.join("Resources", "election_data.csv")

# Open csv file
with open(poll_csv) as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")

    # Begin loop
    for row in csvreader:
        # Total votes cast
        total_votes += 1
        # Grab candidate names and store in list, while also creating candidate vote tracking in dictionary
        if row["Candidate"] not in candidates:
            candidates.append(row["Candidate"])
            poll_data[row["Candidate"]] = 0
        # Begin vote tallies
        poll_data[row["Candidate"]] = poll_data[row["Candidate"]] + 1
    
    # Process dictionary for results
    for key in poll_data:
        # Calculate vote percentage
        vote_percent = poll_data.get(key) / total_votes * 100
        vote_percentages.append(round(vote_percent,2))

        # Decide winner
        if poll_data.get(key) > winner_count:
            winner_count = poll_data.get(key)
            winner = key


# Final Results
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
# Loop to print results
for key in poll_data:
    prnt_cand = candidates[i]
    prnt_cndttl = poll_data.get(key)
    prnt_percent = vote_percentages[i]
    print(f"{prnt_cand}: {prnt_percent}% ({prnt_cndttl})")
    i += 1
# Reset loop counter so it can be reused for output.txt
i = 0
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

# Final Output
output_to = os.path.join("Analysis", "election_data_processed.txt")

with open(output_to, "w",) as election_results:
    election_results.write(f"Election Results\n")
    election_results.write(f"-------------------------\n")
    election_results.write(f"Total Votes: {total_votes}\n")
    election_results.write(f"-------------------------\n")
    for key in poll_data:
        prnt_cand = candidates[i]
        prnt_cndttl = poll_data.get(key)
        prnt_percent = vote_percentages[i]
        election_results.write(f"{prnt_cand}: {prnt_percent}% ({prnt_cndttl})\n")
        i += 1
    election_results.write(f"-------------------------\n")
    election_results.write(f"Winner: {winner}\n")
    election_results.write(f"-------------------------")