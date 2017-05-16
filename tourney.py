
from operator import itemgetter
import csv
data = []
#fighters.csv contains a list of the names of fighters
with open ('fighters.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        for row in reader:
                #Add a fighter to data in the format [Fighter Name, Points, [Fighters Beaten], [Fighters Lost To], [Fighters Drawn To]
                data.append([row[0], 0, [], [], []])

#fights.csv contains the results in the format [Fighter1ID, Fighter2ID, W/L/D]
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
                        data[int(row[0])][1] += 1 # Add 1 point per draw
                        data[int(row[1])][1] += 1 # Add 1 point per draw
                        data[int(row[0])][4].append(data[int(row[1])][0]) #Add other fighter to drawn list
                        data[int(row[1])][4].append(data[int(row[0])][0]) #Add other fighter to drawn list


                else:
                        #Error in data
                        print "Data Error in row " + str(i)
                i += 1
print "Current standings:", sorted(data,key=itemgetter(1), reverse=True) #Sort by second value of 'data' list (points)

###Test Drawing Functionality###
print data[0]
print data[1]
#test
