import datetime 
import matplotlib.pyplot
from matplotlib import style 
import pandas 
import pandas_datareader.data
import sys

"""
=====================================================================================================================
    -=={AUTHORS NOTES}==-

    The base content of this project has taken inspiration from:
        https://www.youtube.com/watch?v=2BrpKpWwT2A&list=LL&index=2&t=195s&ab_channel=sentdex

    Other concepts and functions explored are entirely my own work.


    - Loc Lien
=====================================================================================================================
"""




def hardCodedExample():
    # Style.use defines the types of visual representations of data possible from:
    # https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html 
    # For the sake of this implementation, I will be using the ggplot design  
    style.use("ggplot")

    # The function used here, pandas_datareader.data.Datareader, requires a universal formatted time and date for the start and end periods of the data we will be grabbing
    # To tackle this, I will be using datetime to generate a uniform yyyy/mm/dd date and time input for the scrap function
    startDate = datetime.datetime(2001,2,6)
    endDate = datetime.datetime(2021,6,27)

    # We will be using Datareader from pandas data reader to create a request for stock information about the stock represented by the ticker.
    #The raw output of this api call will then be stored within a variable for further usage. 
    rawDataFrame = pandas_datareader.data.DataReader("AMZN","yahoo",startDate,endDate)
    print(rawDataFrame.head())



def main(ticker,api,start,end):
    # Style.use defines the types of visual representations of data possible from:
    # https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html 
    # For the sake of this implementation, I will be using the ggplot design   
    style.use("ggplot")
    # We will be using Datareader from pandas data reader to create a request for stock information about the stock represented by the ticker.
    #The raw output of this api call will then be stored within a variable for further usage. 
    rawDataFrame = pandas_datareader.data.DataReader(ticker, api, start, end)
    return(rawDataFrame.to_string())




"""
Simple helper function that iterates through an array and changes the string value in each position 
into an acceptable integer input (to be used in the datetime function)

Time Complexity: O(n), where n represents the length of the input array
Auxiliary Space Complexity: O(1), as the function is "technically" an in place function
"""
def arrayStringsToInt(inputArray):
    for i in range(len(inputArray)):
        inputArray[i] = int(inputArray[i])
    return inputArray



if __name__ == '__main__':


    # Checks to see if the correct number of input variables has been provided to the script 
    if len(sys.argv) == 5:
 
        # Sets the value of the stock ticker to the first input value from the sytem script call
        stockTicker = sys.argv[1]

        # Sets the API used to the second input value from the system script call
        api = sys.argv[2]
        
        # Takes the start and end dates given by the user in DD/MM/YYYY format and transforms it into datetime format
        startDateArray = arrayStringsToInt(sys.argv[3].split("/"))
        startDate = datetime.datetime(startDateArray[2],startDateArray[1],startDateArray[0])
        endDateStringArray = arrayStringsToInt(sys.argv[4].split("/"))
        endDate = datetime.datetime(endDateStringArray[2],endDateStringArray[1],endDateStringArray[0])
        
        # Calls the main function, passing through the data as gathered above 
        result = main(stockTicker, api, startDate, endDate)

        # If the output file already exists, write the output to the file, else create the file and write the output
        # data into it.
        outputFile = open("stock_scrapping_output.txt", "w")
        outputFile.write(result)
        outputFile.close


    else:
        print("Incorrect usage, please pass through a Stock Ticker, API Base, Start and End dates")
