import itertools
import pandas as pd
import numpy as np
import math

# Compare first and second timestamps
def compareTwoSingleDates(sourceDate, targetDate):
    print('sourceDate:', sourceDate)
    print('targetDate:', targetDate)
    if sourceDate > targetDate:
        print('sourceDate is greater than targetDate')
    else:
        print('sourceDate is lower than targetDate')

# Return a list of timestamps that are bigger that target timestamp
def validateBiggerTimestamps(dateList, targetTime):
    invalidEventDate = []
    for date in dateList:  
        if date > targetTime:
            invalidEventDate.append()
    print('Number of invalid timestamps: ' + str(len(invalidEventDate)))
    return invalidEventDate

# Return a list of timestamps that are smaller that target timestamp
def validateSmallerTimestamps(dateList, targetTime):
    invalidEventDate = []
    for date in dateList:  
        if date < targetTime:
            invalidEventDate.append()
    print('Number of invalid timestamps: ' + str(len(invalidEventDate)))
    return invalidEventDate

# Compare start and event dates from two seperate lists
def compareDatesFromList(startTimeList, eventTimeList):
    invalidEventDate = []
    # if len(startTimeList) != len(eventTimeList):
    #     return "Invalid data. Make sure start and event data lists have same length"
    for (startTime, eventTime) in itertools.zip_longest(startTimeList, eventTimeList):
        if startTime != startTime or eventTime != eventTime:
            invalidEventDate.append(None)
            continue
        if startTime > eventTime:
            invalidEventDate.append(eventTime)
    print('Number of invalid timestamps: ' + str(len(invalidEventDate)))
    return invalidEventDate
  
# Compare start and event dates from two seperate lists
def checkTimestampInRange(startTimeList, endTimeList, eventTimeList, ):
    invalidEventDate = []
    # if len(startTimeList) != len(eventTimeList):
    #     return "Invalid data. Make sure start and event data lists have same length"
    for (startTime, endTime, eventTime) in itertools.zip_longest(startTimeList, endTimeList, eventTimeList):
        if startTime != startTime or eventTime != eventTime or endTime != endTime:
            invalidEventDate.append(None)
            continue
        if startTime > eventTime or endTime < eventTime:
            invalidEventDate.append(eventTime)
    print('Number of invalid timestamps: ' + str(len(invalidEventDate)))
    return invalidEventDate

# Return number of null values in a list
def numberOfNullValues(timeStampsList):
    # applying the method
    count_nan = timeStampsList.isnull().sum()
    # printing the number of values present in the column
    print('Number of NaN values present: ' + str(count_nan))

def findSmallTimeDifferences(eventA, eventB):
    invalidEventDate = []
    counter = 0
    # if len(eventA) != len(eventB):
    #     return "Invalid data. Make sure start and event data lists have same length"
    for (eventATimestamp, eventBTimestamp) in itertools.zip_longest(eventA, eventB):
        if eventATimestamp != eventATimestamp or eventBTimestamp != eventBTimestamp:
            invalidEventDate.append(None)
            continue
        if (eventATimestamp - eventBTimestamp) / pd.Timedelta(seconds=1) < 420:
            invalidEventDate.append(eventBTimestamp)
            counter = counter + 1
    print('Number of invalid timestamps: ' + str(counter))
    return counter