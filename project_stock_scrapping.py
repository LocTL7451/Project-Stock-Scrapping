import datetime
import matplotlib.pyplot
from matplotlib import style
import pandas
import pandas_datareader.data
import sys
import plotly.graph_objects

"""
=====================================================================================================================
    -=={AUTHORS NOTES}==-

    The base content of this project has taken inspiration from:
        https://www.youtube.com/watch?v=2BrpKpWwT2A&list=LL&index=2&t=195s&ab_channel=sentdex

    Other concepts and functions explored are entirely my own work

    - Loc Lien
=====================================================================================================================
"""

"""
    Base function for getting the data frame body of the stock data. This version of the function is hard coded to ensure that all the imported packages 
    are set up correctly and the data extraction is working correctly. 
"""
def hardCodedExample():
    # Style.use defines the types of visual representations of data possible from:
    # https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
    # For the sake of this implementation, I will be using the ggplot design
    style.use("ggplot")

    # The function used here, pandas_datareader.data.Datareader, requires a universal formatted time and date for the start and end periods of the data we will be grabbing
    # To tackle this, I will be using datetime to generate a uniform yyyy/mm/dd date and time input for the scrap function
    startDate = datetime.datetime(2001, 2, 6)
    endDate = datetime.datetime(2021, 6, 27)

    # We will be using Datareader from pandas data reader to create a request for stock information about the stock represented by the ticker.
    # The raw output of this api call will then be stored within a variable for further usage.
    rawDataFrame = pandas_datareader.data.DataReader(
        "AMZN", "yahoo", startDate, endDate)
    print(rawDataFrame.head())


"""
    An alteration of the hardcoded version of the function, allowing the user to pass through a stock ticker, api, start and end dates. 
    This version of the function will return the data frame as oppposed to a string version of the data frame/a section of the data frame.
"""
def basicDF(ticker, api, start, end):
    # Style.use defines the types of visual representations of data possible from:
    # https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
    # For the sake of this implementation, I will be using the ggplot design
    style.use("ggplot")
    # We will be using Datareader from pandas data reader to create a request for stock information about the stock represented by the ticker.
    # The raw output of this api call will then be stored within a variable for further usage.
    rawDataFrame = pandas_datareader.data.DataReader(ticker, api, start, end)
    return(rawDataFrame)


"""
    The most complicated version of the base data frame grabber function, taking in the same parameters as the previous functions, except this time outputting the dataframe
    as a csv file, which allows for manual viewing and plotting capabilities.
"""
def CSVDF(ticker, api, start, end):
    # Style.use defines the types of visual representations of data possible from:
    # https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
    # For the sake of this implementation, I will be using the ggplot design
    style.use("ggplot")
    # We will be using Datareader from pandas data reader to create a request for stock information about the stock represented by the ticker.
    # The raw output of this api call will then be stored within a variable for further usage.
    rawDataFrame = pandas_datareader.data.DataReader(ticker, api, start, end)

    #del rawDataFrame["Adj Close"]
    
    """
    columns = {"High": "HighPrice",
    "Low": "LowPrice",
    "Open": "OpenPrice",
    "Close": "ClosePrice"}
    rawDataFrame.rename(columns = columns, inplace = True)
    """

    rawDataFrame.to_csv("raw_df_output.csv")


"""
    Function that allows the user to specify a csv file as input, as well as key to display data by and plots a graph of the csv file. This is the basic
    function that allows us to visualize data, of which will be built further upon with adding more functionality, encompassing common stock indicators.
"""
def visDF(dataFrameName, displayKey):

    # Creates and formats the data frame from the specified CSV file, using the first column's data as the index for the dataframe (x values)

    dataFrame = pandas.read_csv(dataFrameName, parse_dates=True, index_col=0)

    """    # Specific case for calculating rolling window moving average.
        if displayKey == "ma":
            
            dataFrame["Moving Average"] = dataFrame["Adj Close"].rolling(window=100, min_periods = 0).mean()
            dataFrame["Moving Average"].plot()
            matplotlib.pyplot.show()


        else:
    """
        # Plots the data frame onto a graph, displaying the requested data based on the display key
    dataFrame[displayKey].plot()
    #dataFrame.plot()
    matplotlib.pyplot.show()



def visCandleStick(dataFrameName):
    dataFrame = pandas.read_csv(dataFrameName, parse_dates=True, index_col=0)

    del dataFrame["Adj Close"]
    del dataFrame["Volume"]


    dataFrame = dataFrame.reset_index()

    candleGraph = plotly.graph_objects.Figure(data=[plotly.graph_objects.Candlestick(x=dataFrame['Date'],
                open=dataFrame['Open'],
                high=dataFrame['High'],
                low=dataFrame['Low'],
                close=dataFrame['Close'])])
    candleGraph.show()


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
    if sys.argv[1] == "basic":

        # Sets the value of the stock ticker to the first input value from the sytem script call
        stockTicker = sys.argv[2]

        # Sets the API used to the second input value from the system script call
        api = sys.argv[3]

        # Takes the start and end dates given by the user in DD/MM/YYYY format and transforms it into datetime format
        startDateArray = arrayStringsToInt(sys.argv[4].split("/"))
        startDate = datetime.datetime(
            startDateArray[2], startDateArray[1], startDateArray[0])
        endDateStringArray = arrayStringsToInt(sys.argv[5].split("/"))
        endDate = datetime.datetime(
            endDateStringArray[2], endDateStringArray[1], endDateStringArray[0])

        # Calls the main function, passing through the data as gathered above
        result = basicDF(stockTicker, api, startDate, endDate)
        stringResult = result.to_string()
        # If the output file already exists, write the output to the file, else create the file and write the output
        # data into it.
        outputFile = open("stock_scrapping_output.txt", "w")
        outputFile.write(stringResult)
        outputFile.close

    elif sys.argv[1] == "csv":
        # Sets the value of the stock ticker to the first input value from the sytem script call
        stockTicker = sys.argv[2]

        # Sets the API used to the second input value from the system script call
        api = sys.argv[3]

        # Takes the start and end dates given by the user in DD/MM/YYYY format and transforms it into datetime format
        startDateArray = arrayStringsToInt(sys.argv[4].split("/"))
        startDate = datetime.datetime(
            startDateArray[2], startDateArray[1], startDateArray[0])
        endDateStringArray = arrayStringsToInt(sys.argv[5].split("/"))
        endDate = datetime.datetime(
            endDateStringArray[2], endDateStringArray[1], endDateStringArray[0])

        # Calls the main function, passing through the data as gathered above
        CSVDF(stockTicker, api, startDate, endDate)

    elif sys.argv[1] == "visSpecific":

        csvFileName = sys.argv[2]
        displayKey = sys.argv[3]
        # HIGH LOW OPEN CLOSE VOLUME
        visDF(csvFileName, displayKey)

    elif sys.argv[1] == "Candle":
        csvFileName = sys.argv[2]
        visCandleStick(csvFileName)

    """  
    elif sys.argv[1] == "viz":
        csvFileName = sys.argv[2]
        for i in range(3,len(sys.argv)):
    """
    