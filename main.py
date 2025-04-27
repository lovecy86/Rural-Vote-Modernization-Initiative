
##Pypoll
# Import necessary modules
import csv #csv module is imported for reading/writing/handling csv files
import os  #os module makes the file path compatible with any operating system

# File to load data from
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
#File to write the output in txt form
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes casted

# Define lists and dictionaries to track candidate names and vote counts
Candidate_vote_count = {} # This dictionary keeps track of the candidate name and the number of votes that each candidate acquired
winner = " "      #This is an empty string variable to hold the winner name
highest_vote_percentage = 0  #Initializing the highest vote percentage to 0
election_outcome = [] #This is the list to hold the candidate name, total nunmeber of votes earned by each candidate and percentage of votes each candidate won

# Open the CSV file and process it
with open(file_to_load) as election_data: #The file is opened as election_data
    reader = csv.reader(election_data)    # csv.reader reads and parses CSV files.

# Stres the header row in a variable
    header = next(reader) 

# Loop through each row of the dataset and process it
    for row in reader: #Iteration is done through the rows of the CSV file.

# Print a loading indicator (for large datasets)
        print(". ", end="")

# Increment  total_votes variable for each row iteration
        total_votes += 1           #Everytime a row is accessed, total_votes variable is incremented. This gives the total number of votes casted.

#Creating a dictionary for storing candidate name and their respective total number of votes won.
        if row[2] in Candidate_vote_count: #Each time a row is accessed, the candidate name in the CSV file is compared with the current empty Dictionary 
            Candidate_vote_count[row[2]] += 1 #If the candidate name(column2) in csv file matches, then the count for that candidate is incremented and
        else:
            Candidate_vote_count[row[2]] = 1    #the name and the vote count for that candidate is saved in the dictionary, else no change happens in the count

#To compute percentage of votes each candidate won
    for candidate, count in Candidate_vote_count.items(): #for each candidate name in the Candidate_vote_count dictionary, percentage of votes that each candidate earned is computed
        Won_Vote_percentge= (count/total_votes)*100  #Percentage of votes won = (total number of votes earned by a candidata/total number of votes casted)*100
        Won_Vote_percentge = round(Won_Vote_percentge,3) # the percentage is rounded upto 3 decimals
        election_outcome.append((candidate,Won_Vote_percentge,count))  # candidate name, percentage of votes won and number of votes earned by each candidate are together saved in a list 
     # this is to find the winner  
        if Won_Vote_percentge > highest_vote_percentage: #the vote percentage of each canddate is compared and the highest vote percentage candidate name is stoes in winner variable.
            highest_vote_percentage = Won_Vote_percentge
            winner = candidate

#Print results in the terminal
print(f"\nElection Results")
print("-----------------------")
print(f"Total Votes : {total_votes}")
print("------------------------")
for candidate, Vote_percentge,count in election_outcome:
    print(f"{candidate}: {Vote_percentge}% ({count})")
print("-----------------------")
print(f"Winner : {winner}")
print("-----------------------")


# Open a file and write the results in that file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write(f"-----------------------\n")
    txt_file.write(f"Total Votes : {total_votes}\n")
    txt_file.write(f"-----------------------\n")
    for candidate, Vote_percentge,count in election_outcome:
       txt_file.write(f"{candidate}: {Vote_percentge}% ({count})\n")
    txt_file.write(f"-----------------------\n")
    txt_file.write(f"Winner : {winner}\n")
    txt_file.write(f"-----------------------\n")
