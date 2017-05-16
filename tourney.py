
from operator import itemgetter
import csv
data = []
with open ('fighters.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        for row in reader:
                data.append([row[0], 0, [], [], []])

with open ('fights.csv', 'rb') as csvfile:
        i = 0
        reader = csv.reader(csvfile, delimiter = ',')
        for row in reader:
                if (int(row[2]) == 0):
                #First Fighter won
                        data[int(row[0])][1] += 2 # Add 2 point per win
                        data[int(row[0])][2].append(data[int(row[1])][0]) #Add loser to winners beaten list
                        data[int(row[1])][3].append(data[int(row[0])][0]) #Add winner to losers lost to list
                elif (int(row[2]) == 1):
                        #Second Fighter won
                        data[int(row[1])][1] += 2 # Add 2 point per win
                        data[int(row[1])][2].append(data[int(row[0])][0]) #Add loser to winners beaten list
                        data[int(row[0])][3].append(data[int(row[1])][0]) #Add winner to losers lost to list
                elif (int(row[2]) == 2):
                        #If Draw
                        data[int(row[0])][1] += 1 # Add 2 point per win
                        data[int(row[1])][1] += 1 # Add 2 point per win
                        data[int(row[0])][4].append(data[int(row[1])][0]) #Add loser to winners beaten list
                        data[int(row[1])][4].append(data[int(row[0])][0]) #Add loser to winners beaten list


                        else:
                        #Error in data
                        print "Data Error in row " + str(i)
                i += 1
print "Current standings:", sorted(data,key=itemgetter(1), reverse=True) #Search by second value of 'data' list

###Test Drawing Functionality###
print data[0]
print data[1]
#test
