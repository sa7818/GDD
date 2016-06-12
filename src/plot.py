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
file_name = sys.argv[1]

def read_weather(file_name):
    #Read csv file
    data=pd.read_csv(file_name, skiprows=25,usecols=(0,6,8),encoding='ISO-8859-1') 
    #replcae E to NAN in csv data file
    data.replace('E', np.nan,inplace=True)
    #replace M to NAN in csv data file
    data.replace('M', np.nan,inplace=True)
    #Remove NAN in csv data file
    data = data.dropna(how='any')
    Date=data['Date/Time']
    Max_Temp=data['Max Temp Flag']
    Min_Temp=data['Min Temp Flag']
    return Date,Max_Temp, Min_Temp

def plot_maxmin(csv_file):
    date,max_temp,min_temp=read_weather(css_file)
    #print (max_temp)
    #max_temp=max_temp.astype(float)
    #min_temp=min_temp.astype(float)
    date=pd.to_datetime(date)
    maxy,=plt.plot_date(date,max_temp,'cx-',label="max temp")
    mint,=plt.plot_date(date,min_temp,'ro-',label="min temp")
    plt.legend(handles=[maxy,mint])
    plt.ylabel("temp")
    plt.xlabel("date")
    plt.title("Min & Max Temp")
    return plt.savefig("Min & Max Temp.png",format="png")