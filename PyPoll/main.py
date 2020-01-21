import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    row_count = sum(1 for row2 in csvreader) 

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    candidate = []
    votes = []
    
    for row in csvreader:
        votes.append(row[2])
        if row[2] not in candidate:
            candidate.append(row[2])
   

outputfile= open("results.txt","w+")
outputfile= open("results.txt","a")

outputfile.write("Election Results\n")
outputfile.write("-------------------------\n")
outputfile.write(f"Total Votes: {row_count}\n")
outputfile.write("-------------------------\n")


print ("Election Results")
print ("-------------------------")
print (f"Total Votes: {row_count}")
print ("-------------------------")



memory = 0

for name in candidate:
    vote_count = votes.count(name)
    
    percentage = ((vote_count/row_count)*100)
    percentage = format(percentage, '.3f')
    print(f"{name}: {percentage}% ({votes.count(name)})")
    outputfile.write(f"{name}: {percentage}% ({votes.count(name)})\n")
    
    if vote_count > memory:
        winner = name
        memory = vote_count
    else:
        memory = vote_count
    
print ("-------------------------")
print (f"Winner: {winner}")
print ("-------------------------")    

outputfile.write("-------------------------\n")
outputfile.write(f"Winner: {winner}\n")
outputfile.write("-------------------------")   
    
outputfile.close()