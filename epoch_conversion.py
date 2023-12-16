import time
import math

# Functions for getting currents days epoch Beginning of day
def unixDay(time = time.time()):
    start_of_day = math.floor(time / 86400)*86400
    end_of_day = start_of_day + 86399
    output = f'\nStart of Day: {start_of_day}\nEnd of Day: {end_of_day}\n'
    return output
  
# User input get Epoch from queried date and time
def getUnixTime(queryTime):
    for i in range(len(queryTime)):
        return time.mktime(time.strptime(queryTime[i], "%m %d %Y %H:%M:%S"))
    
    
# Daylight saving time always starts on the second Sunday in March 
# and ends on the first Sunday in November for the United States    
def daylightSavingsUs():
    pass

# User input and delimiter
queryTime = input('\nEnter time as DD MM YYYY HH:MM:SS: ')
userInput = queryTime.split(': ')      
      

print(f'\nEpoch in Local Time: {getUnixTime(userInput)}\n')

print(unixDay(getUnixTime(userInput)))





