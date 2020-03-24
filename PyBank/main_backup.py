#import os to be able to traverse directories no matter the OS
import os

#import csv to be able to work with CSV file in a more streamlined manner
import csv

#Variable to store the total number months
total_months = 0

#Variable for total amount of profilt/loss
profit_loss = 0

#The average of the changes in "Profit/Losses" over the entire period
avg_change = 0

#The greatest increase in profits (date and amount) over the entire period
gipd = ""
gipa = 0

#The greatest decrease in losses (date and amount) over the entire period
gdld = ""
gila = 0

#create variable that is used as a locator for where the data will reside
inpath = os.path.join("..", "Resources", "budget_data.csv")

#Open file and point the interator to the file to start working with the data
with open(inpath) as csvfile:

    #save the file to a variable
    csvdata = csv.reader(csvfile)

    #store the CSV header information so that you dont include it in any calculations
    csv_header = next(csvdata)

    for data in csvdata:
        total_months += 1


    

