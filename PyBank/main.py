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

#The greatest increase in losses (date and amount) over the entire period
gdpd = ""
gdpa = 0

#create variable that is used as locator for where the data will reside
inpath = os.path.join("Resources", "budget_data.csv")

#create variable that is used as a lcoator where the output will be stored
outpath = os.path.join("Resources", "budget_data_output.txt")

#Open file and point the interator to the file to start working with the data
with open(inpath) as csvfile:

    #save the file to a variable
    csvdata = csv.reader(csvfile)

    #store the CSV header information so that you dont include it in any calculations
    csv_header = next(csvdata)

    #For loop to iterate through the file
    for data in csvdata:

        #Count the total number of months or rows depending on what you are counting
        total_months += 1
        profit_loss = (int(data[1]))

        #if statement to track the greatest increase in profits, losses, and their corresponding month
        if int(data[1]) < 0 and int(data[1]) < gdpa:
            gdpa = int(data[1])
            gdpd = data[0]
        elif int(data[1]) >= 0 and int(data[1]) > gipa:
            gipa = int(data[1]) 
            gipd = data[0]

    avg_change = round(profit_loss / total_months, 2)

#Open the file to input the calculations
with open(outpath, 'w') as outfile:
    
    #Writing to the file
    outfile.write("Financial Analysis\n")
    outfile.write("------------------------------\n")
    outfile.write(f"Total months: {total_months}\n")
    outfile.write(f"Total: ${profit_loss}\n")
    outfile.write(f"Average change: ${avg_change}\n")
    outfile.write(f"Greatest Increase in Profit: ${gipa} on {gipd}\n")
    outfile.write(f"Greatest Decrease in Profits: ${gdpa} on {gdpd}\n")

#Print statements below to check the accuracy of the data
print("Financial Analysis")
print("------------------------------")
print(f"Total months: {total_months}\n")
print(f"Total: ${profit_loss}\n")
print(f"Average change: ${avg_change}\n")
print(f"Greatest Increase in Profit: ${gipa} on {gipd}\n")
print(f"Greatest Decrease in Profits: ${gdpa} on {gdpd}\n")

    

