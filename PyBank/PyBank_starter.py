# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0 #initialize total months to 0
total_net = 0 #initialize the net revenue to 0
monthly_changes = [] #initialize the list of monthly changes
months = []


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read header row
    header = next(reader)
    #move to the first row
    first_row = next(reader)

    total_months += 1
    # Track the net change
    total_net += float(first_row[1])
    #establish previous revenue
    prev_revenue = float(first_row[1])

   

    
    for row in reader:

        # Track the total
        total_months += 1

        # Track the total profit
        total_net += float(row[1])

        #track the avg change 
        net_change = float(row[1]) - prev_revenue

        #add on to the list of monthly changes
        monthly_changes.append(net_change)

        #add the first month that a change occured\
            #month is in index 0
        months.append(row[0])

        # update previous revenue
        prev_revenue = float(row[1])

#calculate the avg net change per month
average_changes_per_month = sum(monthly_changes) / len(monthly_changes)

greatest_increase = [months[0], monthly_changes[0]] #holds the month and the value of our biggest increase
greatest_decrease = [months[0], monthly_changes[0]] #holds the month and the value of our biggest decrease

#use loop to calculate the index of the greatest and least monthly changes
for m in range(len(monthly_changes)):
    #calc the gratest inc and decr
    if(monthly_changes[m]> greatest_increase[1]):
        #if value is greater than the greatest_increase, that value replaces the old value and becomes the new greatest_increase value
        greatest_increase[1] = monthly_changes[m]
        #update the month
        greatest_increase[0] = months[m]

    if(monthly_changes[m] < greatest_decrease[1]):
        #if value is greater than the greatest_increase, that value replaces the old value and becomes the new greatest_increase value
        greatest_decrease[1] = monthly_changes[m]
        #update the month
        greatest_decrease[0] = months[m]    

#start generating the output
output = (
    f"\nFinancial Analysis \n"
    f"--------------------------\n"
    f"\tTotal Months : {total_months}\n"
    f"\tTotal Revenue: ${total_net:,.2f}\n"
    f"\tAverage Change: ${average_changes_per_month:,.2f}\n"
    f"\tGreatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]:,.2f}) \n"
    f"\tGreatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]:,.2f}) \n"
)
#printed output in the terminal/console
print (output)

# Write the results to a text file is alos exporting the output to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
