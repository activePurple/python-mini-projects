# epoch_conversion.py
# By Tyler O'Neil aka Ner0x42
# Date: 12/16/2023

import time
import math

# Functions for getting currents days epoch Beginning of day
def unixDay(time = time.time()):
    start_of_day = math.floor(time / 86400)*86400
    
    current_epoch = time
    
    end_of_day = start_of_day + 86399
    
    output = f'\nStart of Day: {start_of_day}\nEnd of Day: {end_of_day}\nCurrent Epoch: {current_epoch}'
    return output
    
    
# Daylight saving time always starts on the second Sunday in March 
# and ends on the first Sunday in November for the United States    
def daylightSavingsUs():
    pass

# User input as function
def userInput():
  queryTime = input('\nEnter time as DD MM YYYY HH:MM:SS: ')
  queryDate = queryTime.split(': ')
  def getUnixTime(queryDate):
    for i in range(len(queryDate)):
        return time.mktime(time.strptime(queryDate[i], "%m %d %Y %H:%M:%S"))
  return getUnixTime(queryDate)   


print(unixDay(userInput()))