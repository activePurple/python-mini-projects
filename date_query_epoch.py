# epoch_conversion.py
# By Tyler O'Neil aka Ner0x42
# Date: 12/16/2023

import time
import math


def unixDay(time = time.time()):
  start_of_day = math.floor(time / 86400)*86400
  current_epoch = time
  end_of_day = start_of_day + 86399
  return start_of_day

def getUnixTime(queryTime):
    for i in range(len(queryTime)):
        return time.mktime(time.strptime(queryTime[i], "%m %d %Y %H:%M:%S")) 

def userQuery():
  userQuery = input('\nEnter a + or -, years as int: ')
  return userQuery

def pastDate(userQuery):
  epochYearSeconds =  31556926
  splitter = userQuery.split(', ')
  currentEpoch = unixDay()
  def getEpoch(splitter):
    if splitter[0] == '+':
      addYears = currentEpoch + (int(splitter[1]) * epochYearSeconds)
      return addYears
    elif splitter[0] == '-':
      subYears = currentEpoch - (int(splitter[1]) * epochYearSeconds)
      return subYears
    else:
      print("Invalid Parameters plea check your input")
  convertDate = time.localtime(getEpoch(splitter))
  realDate = time.strftime("%m-%d-%Y", convertDate)
  return realDate
  
print(pastDate(userQuery()))