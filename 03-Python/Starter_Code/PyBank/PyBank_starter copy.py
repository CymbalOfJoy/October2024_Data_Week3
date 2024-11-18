# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data

# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    
    # Skip the header row
    header = next(reader)
    first_row = next(reader)

    # Extract first row to avoid appending to net_change_list
    total_net_change = 0

    # Track the total and net change
    total_months = 1
    total_profit = int(first_row[1])
    previous_profit_loss = int(first_row[1])
    highest_increase = -30000000
    highest_decrease = 30000000

    # Process each row of data
    for row in reader:
        current_profit = int(row[1])

        # Track the total
        total_months = total_months + 1
        total_profit = total_profit + current_profit
        # print(row, total_profit)

        # Track the net change
        net_change = current_profit - previous_profit_loss
        # print(net_change)
        total_net_change = total_net_change + net_change
        previous_profit_loss = int(first_row[1])

        # Calculate the greatest increase in profits (month and amount)
        if net_change > highest_increase:
            highest_increase = net_change

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < highest_decrease:
            highest_decrease = net_change


# Calculate the average net change across the months
average_net_change = total_net_change / (total_months - 1)

# Generate the output summary


# Print the output


# Write the results to a text file
# with open(file_to_output, "w") as txt_file:
    # txt_file.write(output)
