#import os to be able to traverse directories no matter the OS
import os

#import csv to be able to work with CSV file in a more streamlined manner
import csv

#import array library to streamline working with multidimensional arrays
import array

#Variable to store the total number of votes
total_votes = 0

#Variable for lists of candidates and the votes each candidate won
cand_dictionary = {}

#Winner of the election
winner = ""
winner_votes = 0

#create variable that is used as locator for where the data will reside
inpath = os.path.join("Resources", "election_data.csv")

#create variable that is used as a lcoator where the output will be stored
outpath = os.path.join("Resources", "election_data_output.txt")

#Open file and point the interator to the file to start working with the data
with open(inpath) as csvfile:

    #save the file to a variable
    csvdata = csv.reader(csvfile)

    #store the CSV header information so that you dont include it in any calculations
    csv_header = next(csvdata)

    #For loop to iterate through the file
    for data in csvdata:

        #Count the total number of votes
        total_votes += 1

        #If statement to see if a candidate is already in the candidates dictionary 
        #and if not add the candidate to the dictionary and increase the count of votes
        #the received
        if data[2] not in cand_dictionary.keys():
            cand_dictionary.update({data[2]: 1})
        elif data[2] in cand_dictionary.keys():
            cand_dictionary[data[2]] += 1

    #print election total to command line
    print("\nElection Results")
    print("------------------------")
    print(f"Total votes: {total_votes}")
    print("------------------------\n")

#Open file to write to it while printing to the command line
with open(outpath, 'w') as outfile:
    
    #print election total to file
    outfile.write("Election Results\n")
    outfile.write("------------------------\n")
    outfile.write(f"Total votes: {total_votes}\n")
    outfile.write("------------------------\n")
    
    #for loop to go through dictionary and calculate the results of the votes and print
    for key, value in cand_dictionary.items():
        print(f"{key}: {round(value/total_votes*100, 2)}% ({value})")
        outfile.write(f"{key}: {round(value/total_votes*100, 2)}% ({value})\n")

        #if conditional to determine who has the most votes
        if value > winner_votes:
            winner_votes = value
            winner = key
    
    #write the winner results to the file. Have to put it out here so that it doesnt
    #print this winner line for each calculation
    outfile.write("\n------------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("------------------------")

#print the winner results to command line
print("\n------------------------")
print(f"Winner: {winner}")
print("------------------------")