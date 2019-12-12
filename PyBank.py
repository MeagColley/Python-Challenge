import os
import csv
from collections import Counter
csvpath = os.path.join("Instructions","PyBank","Resources","budget_data.csv")

with open(csvpath, newline= "") as csvfile:
    csvreader= csv.reader(csvfile,delimiter=",")
    csv_header= next(csvreader)
    print(f'Header: {csvreader}')
    
    
    total_months= []
    net_total = []  
     
 for column in csvreader:
     total_months.append(column[0])

    # total_months = sum(1 for row in csvreader)
    # print(f" {total_months}")
# # Net Total of Profit/Losses
    # for row in csvreader:
        # net_total= net_total + int(row[1])
     
 
    # print (f' {net_total}')

