# import csv and os
import csv
import os

# path to budget_data.csv
budget_data_csv = os.path.join("Resources","budget_data.csv")

# path to the text file that will be created with the financial analysis
financialAnalysis = os.path.join("analysis","financial_analysis.txt")

# open the csv file and read it
with open(budget_data_csv, 'r') as csvFile:

    # use the reader() function (delimiter should be set as ',')
    budgetDataReader = csv.reader(csvFile, delimiter=',')

    # parse out the header and store the header as budgetDataHeader
    budgetDataHeader = next(budgetDataReader)

    # create empty variables for the analysis
    totalMonths = 0 # variable for the total number of months included in the data set
    totalAmount = 0 # variable for the net total amount of "Profit/Losses" over the entire period
    monthAmount = 0 # variable to hold the monthly amount of 'Profit/Losses'
    lastMonthAmount = 0 # variable to hold the last month's amount
    monthName = [] # an empty list to hold the names of the months
    monthlyChanges = [] # an empty list to hold the changes of 'Profit/Losses' for each month

    # create a for loop to run through every row in the csv file
    for row in budgetDataReader:

        # add 1 to the number of total months
        totalMonths += 1

        # add the "Profit/Losses" amount to the running total
        totalAmount += int(row[1])

        # conditional to create a list of the changes in 'Profit/Losses'
        if lastMonthAmount == 0:
            lastMonthAmount = int(row[1]) # stores the 'Profit/Loss' amount in the last month variable if there is no previous month
        else:
            monthAmount = int(row[1]) # stores the current month amount in the correct variable
            monthName.append(row[0]) # stores the current month's name in a list
            monthlyChanges.append(int(monthAmount - lastMonthAmount)) # finds the change in this month's amount and last month's amount and stores it in a list
            lastMonthAmount = int(row[1]) # stores the current month in the last month variable

    # Calculate the average change of the monthly changes
    averageChange = round(sum(monthlyChanges) / len(monthlyChanges), 2)

    # Find the greatest increase in profits
    greatestIncrease = max(monthlyChanges)

    #Find the greatest decrease in profits
    greatestDecrease = min(monthlyChanges)

    monthlyChangesWithNames = list(zip(monthName, monthlyChanges)) # creates a list that associates month names and changes

    # create a loop that goes through every entry in the zip list
    for months in monthlyChangesWithNames:
        # conditional that finds the month associated with the greatest increase
        if months[1] == greatestIncrease:
            greatestIncreaseMonth = months[0]

    # create a loop that goes through every entry in the zip list
    for months in monthlyChangesWithNames:
        # conditional that finds the month associated with the greatest decrease
        if months[1] == greatestDecrease:
            greatestDecreaseMonth = months[0]
    
    # print out the financial analysis
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${totalAmount}")
    print(f"Average Change: ${averageChange}")
    print(f"Greatest Increase in Profits: {greatestIncreaseMonth} (${greatestIncrease})")
    print(f"Greatest Decrease in Profits: {greatestDecreaseMonth} (${greatestDecrease})")

# open the analysis file in writing mode
with open(financialAnalysis, 'w') as textFile:

    # the output that should be written in the analysis file
    output = "Financial Analysis\n"
    output += "----------------------------\n"
    output += f"Total Months: {totalMonths}\n"
    output += f"Total: ${totalAmount}\n"
    output += f"Average Change: ${averageChange}\n"
    output += f"Greatest Increase in Profits: {greatestIncreaseMonth} (${greatestIncrease})\n"
    output += f"Greatest Decrease in Profits: {greatestDecreaseMonth} (${greatestDecrease})\n"

    # write the data in the analysis file
    textFile.write(output)