#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as pyplot
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as dt
from pandas import Series, DataFrame
import pandas as pd
import csv
import sys

def read_weather(file_name):
    """
    This function is just used for read data(Date/Time,Max_Temp,Min_Temp) from file_name.
    The file_name can be the .csv file
    args:
        file_name (csv data file)
    output:
        Date/Time,Max_Temp, Min_Temp
    """
    #Read csv file the second column-Date/Time, the sixth column-Max_Temp and the seventh column-Min_Temp
    data=pd.read_csv(file_name, usecols=(1,5,6),encoding='ISO-8859-1') 
    #The data has missing data in csv data file, to replcae E to NAN in csv data file
    data.replace('E', np.nan,inplace=True)
    #The data has estimated data in csv data file, to replace M to NAN in csv data file
    data.replace('M', np.nan,inplace=True)
    #Then Remove all the 'NAN' data in csv data file
    data = data.dropna(how='any')
    #Get the value of second column-Date/Time
    Date=data['Date/Time']
    #Get the value of sixth column -Max_Temp
    Max_Temp=data['Max_Temp']
    #Get the value of seventh column- Min-Temp
    Min_Temp=data['Min_Temp']
    return Date,Max_Temp, Min_Temp #return date(m/dd/yyyy),max_temp and min_temp

def plot_maxmin(css_file):
    """
    This is function for plot Max and Min temp for task 2
    The data read from the above function(read_weather(filename)) 
    and get the value of Date/Time,Max_Temp, Min_Temp.
    Based on the Max_Temp, Min_Temp to plot max and min temp
    argv :
        filename (csv data file)
    output:
        max and min plot, and save the plot into .png format
    """
    #get the data value, max_temp value and min_temp value based on the read_weather()function
    date,max_temp,min_temp=read_weather(css_file)
    #Convert date into  datetime format
    date=pd.to_datetime(date)
    #To plot max temp graph 
    maxy,=plt.plot_date(date,max_temp,'ro-',label="max temp")
    #To plot min temp graph
    mint,=plt.plot_date(date,min_temp,'cx-',label="min temp")
    #Add legend to the above two plot
    plt.legend(handles=[maxy,mint])
    #Add y-axis's label
    plt.ylabel("temp")
    #Add x-axis's label
    plt.xlabel("date")
    #Add title to the graph
    plt.title("Min & Max Temp") 
    #To save the plot with the argument's name 
    max_plot=plt.savefig(css_file[:-3] + "png",format="png")
    #return plt.savefig("min_max_temp.png",format="png")
    return max_plot
"""
    Use try-catch to handling exception.
"""
try:
    file_name = sys.argv[1]
    plot_maxmin(file_name)
except Exception as e:
    raise e
    print (e)
    

