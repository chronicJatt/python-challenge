# Create a python script that analyzes the records to calculate each of the following:
    # The total number of months included in the dataset,
    # The net total amount of "Profit/Losses" over the entire period,
    # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes,
    # The greatest increase in profits (date and amount) over the entire period,
    # The greatest decrease in profits (date and amount) over the entire period.
# Finally, print the analysis to terminal and export to text file.


# Module importation
import os
import csv

# Variables
total_months = 0
net_pl = 0
pl_monthly_change = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Path to csv file
budget_csv = os.path.join("Resources", "budget_data.csv")

# Open csv file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read header row
    csv_headerskip = next(csvreader)
    ## 1st row values only set with this line, but it skips 2 rows now
    row = next(csvreader)

    # 1st row values temp storage, so they aren't lost forever <3
    previous_pl = int(row[1])
    total_months += 1
    net_pl += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    greatest_decrease = int(row[1])
    greatest_decrease_month = row[0]

    # Begin loop to process csv data
    for row in csvreader:
        # The total number of months
        total_months += 1
        # The net total amount of "Profit/Losses" over the entire period
        net_pl += int(row[1])
        
        # Changes in "Profit/Losses" over the entire period
        month_to_month = int(row[1]) - previous_pl
        pl_monthly_change.append(month_to_month)
        previous_pl = int(row[1])

        # Month of greatest increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

        # Month of greatest decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]

    # Average Change equation
    change_average = sum(pl_monthly_change)/len(pl_monthly_change)

    # Highest & Lowest Month Value retrieval for final presentation
    highest_month = max(pl_monthly_change)
    lowest_month = min(pl_monthly_change)

    # Financial Analysis Results, using f print
    ## :.2f rounds to two decimal points
    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_pl}")
    print(f"Average Change: ${change_average:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${highest_month})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${lowest_month})")

    # Final output
    output_to = os.path.join("Analysis", "budget_data_processed.txt")

    ## "w" required to create file if it doesn't exist already
    ## \n to create new line as first file published all data to one line
    with open(output_to, "w",) as budget_report:
        budget_report.write(f"Financial Analysis\n")
        budget_report.write(f"----------------------------\n")
        budget_report.write(f"Total Months: {total_months}\n")
        budget_report.write(f"Total: ${net_pl}\n")
        budget_report.write(f"Average Change: ${change_average:.2f}\n")
        budget_report.write(f"Greatest Increase in Profits: {greatest_increase_month} (${highest_month})\n")
        budget_report.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${lowest_month})")