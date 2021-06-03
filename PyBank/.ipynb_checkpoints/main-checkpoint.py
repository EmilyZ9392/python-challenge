# Dependencies
import os
import csv
    
 #  Pull in csv/ output text file
budget_path = os.path.join(os.getcwd(), 'PyBank' , 'resources','budget.csv')
    
pybank_output = os.path.join(os.getcwd(), 'PyBank' , 'analysis', 'pybank_output.txt')
    
 # Variables
total_months = 0
prev_pl = 0
month_of_change = []
pl_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_pl = 0
    
    # Read the csv & create dictionaries
with open(budget_path) as pl_data:
       reader = csv.DictReader(pl_data)
    
       for row in reader:
    
           # Total Months & total p/l
            total_months = total_months + 1
            total_pl = total_pl + int(row["Profit/Losses"])
    
            # Profit/Losses change month-to-month
            pl_change = int(row["Profit/Losses"]) - prev_pl
            prev_pl = int(row["Profit/Losses"])
            pl_change_list = pl_change_list + [pl_change]
            month_of_change = month_of_change + [row["Date"]]
    
            # Greatest increase
            if (pl_change > greatest_increase[1]):
                greatest_increase[0] = row["Date"]
                greatest_increase[1] = pl_change
   
            # Greatest decrease
            if (pl_change < greatest_decrease[1]):
                greatest_decrease[0] = row["Date"]
                greatest_decrease[1] = pl_change
   
 # Average P/L Change
pl_avg = sum(pl_change_list) / len(pl_change_list)
    
# Print financial analysis summary
    
print(f' Financial Analysis:')
print(f'---------------------')
print(f'Total Months: {total_months}')
print(f'Net Profit/Loss: ${total_pl}')
print(f'Average P/L Change: ${pl_avg}')
print(f'Greatest Increase in P/L: {greatest_increase[0]} (${greatest_increase[1]})')
print(f'Greatest Decrease in P/L: {greatest_decrease[0]} (${greatest_decrease[1]})')
    
    
#Export the results to text file
    
with open(pybank_output, 'w')as txt_file:
    txt_file.write(f' Financial Analysis')
    txt_file.write(f'---------------------\n')
    txt_file.write(f'Total Months: {total_months}\n')
    txt_file.write(f'Net Profit/Loss: ${total_pl}\n')
    txt_file.write(f'Average P/L Change: ${pl_avg}\n')
    txt_file.write(f'Greatest Increase in P/L: {greatest_increase[0]} (${greatest_increase[1]})\n')
    txt_file.write(f'Greatest Decrease in P/L: {greatest_decrease[0]} (${greatest_decrease[1]})\n')
