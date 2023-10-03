# import csv and os
import csv
import os

# path to budget_data.csv
budget_data_csv = os.path.join("Resources","budget_data.csv")

# open the csv file and read it
with open(budget_data_csv, 'r') as csvFile:

    # use the reader() function (delimiter should be set as ',')
    budgetDataReader = csv.reader(csvFile, delimiter=',')

    # parse out the header and store the header as budgetDataHeader
    budgetDataHeader = next(budgetDataReader)

    # create empty variables for the analysis
    totalMonths = 0 # variable for the total number of months included in the data set
    totalAmount = 0 # variable for the net total amount fo "Profit/Losses" over the entire period

    # create a for loop to run throuhg every row in the csv file
    for row in budgetDataReader:

        # add 1 to the number of total months
        totalMonths += 1

        # add the "Profit/Losses" amount to the running total
        totalAmount += int(row[1])


