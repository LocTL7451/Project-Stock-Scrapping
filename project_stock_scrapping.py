import datetime 
import matplotlib.pyplot
from matplotlib import style 
import pandas 
import pandas_datareader.data

"""
    AUTHORS NOTE:

    The base content of this project has taken inspiration from:
        https://www.youtube.com/watch?v=2BrpKpWwT2A&list=LL&index=2&t=195s&ab_channel=sentdex

    Other concepts and functions explored are entirely my own work.
"""

# Style.use defines the types of visual representations of data possible from:
# https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html 
# For the sake of this implementation, I will be using the ggplot design     
style.use("ggplot")

# The function used here, web.Datareader, requires a universal formatted time and date for the start and end periods of the data we will be grabbing
# To tackle this, I will be using datetime to generate a uniform yyyy/mm/dd date and time input for the scrap function
startDate = datetime.datetime(2001,2,6)
endDate = datetime.datetime(2021/6/27)

# 
rawDataBody = pandas_datareader.data.DataReader("AMZN","yahoo",startDate,endDate)

def main(ticker,api,start,end)

    style.use("ggplot")

    rawDataBody = pandas_datareader.data.DataReader(ticker, api, start, end)



def arrayStringsToInt(inputArray):
    for i in range(inputArray):
        inputArray[i] = int(inputArray[i])
    return inputArray



if __name__ == '__main__':
     
    if len(sys.argv) == 5:
 
        stockTicker = sys.argv[1]
        api = sys.argv[2]
        
        startDateArray = arrayStringsToInt(sys.argv[3].split("/"))
        startDate = datetime.datetime(startDateArray[2],startDateArray[1],startDateArray[0])


        endDateStringArray = arrayStringsToInt(sys.argv[4].split("/"))
        endDate = datetime.datetime(endDateStringArray[2],endDateStringArray[1],endDateStringArray[0])
        
        result = main(stockTicker, api, startDate, endDate)
        print(result)
 
    else:
        print("Incorrect usage, please pass through a stock ticker, api base, start and end dates")
