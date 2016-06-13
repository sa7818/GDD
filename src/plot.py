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
    This function is used for read data(Date/Time,Max_Temp,Min_Temp) from csv file
    args:
        file_name (csv data file)
    output:
        Date/Time,Max_Temp, Min_Temp
    """
    #Read csv file
    data=pd.read_csv(file_name, usecols=(1,5,6),encoding='ISO-8859-1') 
    #replcae E to NAN in csv data file
    data.replace('E', np.nan,inplace=True)
    #replace M to NAN in csv data file
    data.replace('M', np.nan,inplace=True)
    #Remove NAN in csv data file
    data = data.dropna(how='any')
    Date=data['Date/Time']
    Max_Temp=data['Max_Temp']
    Min_Temp=data['Min_Temp']
    return Date,Max_Temp, Min_Temp

def plot_maxmin(css_file):
    """
    This is function for plot Max and Min temp
    The data read from the above function(read_weather(filename)) 
    and get the value of Date/Time,Max_Temp, Min_Temp.
    Based on the Max_Temp, Min_Temp to plot max and min temp
    argv :
        filename (csv data file)
    output:
        max and min plot, and save the plot into .png format
    """
    date,max_temp,min_temp=read_weather(css_file)
    #print (max_temp)
    #max_temp=max_temp.astype(float)
    #min_temp=min_temp.astype(float)
    date=pd.to_datetime(date)
    maxy,=plt.plot_date(date,max_temp,'ro-',label="max temp")
    mint,=plt.plot_date(date,min_temp,'cx-',label="min temp")
    plt.legend(handles=[maxy,mint])
    plt.ylabel("temp")
    plt.xlabel("date")
    plt.title("Min & Max Temp") 
    max_plot=plt.savefig(css_file[:-3] + "png",format="png")
    #return plt.savefig("min_max_temp.png",format="png")
    return max_plot

try:
    file_name = sys.argv[1]
    #file_name = "50089_2015.csv"
    plot_maxmin(file_name)
except Exception as e:
    raise e
    print (e)
    

