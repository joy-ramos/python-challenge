import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
total = 0
month_count = 0
monthlychange = []
months = []
profits = []
months_profits = {}
months_profits_values = []

with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        
        months_profits.update( {row[0] : row[1]} )
        months.append(row[0])
        profits.append(int(row[1]))
        
{k: v for k, v in sorted(months_profits.items(), key=lambda item: item[0])}
        
memory = 0

for key in months_profits.keys():
    months_profits_values.append(months_profits[key])
    
    if memory != 0:
            change = int(months_profits[key]) - int(memory)
            monthlychange.append(change)
            memory = months_profits[key]
    else:
        memory = months_profits[key]
        
total = sum (profits)
month_count = len(months)
    
average_change = (sum(monthlychange)) / (month_count - 1)
average_change = str(round(average_change, 2))     
            
greatestprofit = max(profits)
index1 = profits.index(max(profits))

greatestloss = min(profits)
index2 = profits.index(min(profits))
   
print ("Financial Analysis")
print ("----------------------------")
print (f"Total months: {month_count}")
print (f"Total: ${total}")
print (f"Average change: ${average_change}")
print (f"Greatest Increase in Profits: {months[index1]} (${greatestprofit})")
print (f"Greatest Decrease in Profits: {months[index2]} (${greatestloss})")



outputfile= open("results.txt","w+")
outputfile= open("results.txt","a")

outputfile.write ("Financial Analysis\n")
outputfile.write ("----------------------------\n")
outputfile.write (f"Total months: {month_count}\n")
outputfile.write (f"Total: ${total}\n")
outputfile.write (f"Average change: ${average_change}\n")
outputfile.write (f"Greatest Increase in Profits: {months[index1]} (${greatestprofit})\n")
outputfile.write (f"Greatest Decrease in Profits: {months[index2]} (${greatestloss})")

outputfile.close()