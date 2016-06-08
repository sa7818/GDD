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
    data=pd.read_csv(file_name, skiprows=25,usecols=(0,6,8),encoding='ISO-8859-1')
    data=data[data!='E']
    data=data.dropna(how='any')
    Date=data['Date/Time']
    Max_Temp=data['Max Temp Flag']
    Min_Temp=data['Min Temp Flag'] 
    return Date,Max_Temp, Min_Temp
def read_weather2(file_name):
    data=pd.read_csv(file_name, skiprows=25,usecols=(0,6,8),encoding='ISO-8859-1')
    Date=data['Date/Time']
    Max_Temp=data['Max Temp Flag']
    Min_Temp=data['Min Temp Flag'] 
    return Date,Max_Temp, Min_Temp
def read_weather3(file_name):
    data=pd.read_csv(file_name, skiprows=25,usecols=(0,6,8),encoding='ISO-8859-1')
    
    Date=data['Date/Time']
    Max_Temp=data['Max Temp Flag']
    Min_Temp=data['Min Temp Flag']
    Min_Temp=Min_Temp[Min_Temp!='M']
    Min_Temp=Min_Temp.dropna(how='any')
    return Date,Max_Temp,Min_Temp




date_cal2015,max_cal2015,min_cal2015=read_weather('C:/Users/Sharon/Documents/GitHub/GDD/csv_data/calgary/2015.csv')
max_cal2015=max_cal2015.astype(float)
min_cal2015=min_cal2015.astype(float)
date_cal2015=pd.to_datetime(date_cal2015)
maxy_cal2015,=plt.plot_date(date_cal2015,max_cal2015,'ro-',label="max temp")
mint_cal2015,=plt.plot_date(date_cal2015,min_cal2015,'cx-',label="min temp")
plt.legend(handles=[maxy,mint])
plt.title("Calgary 2015 temp")
plt.ylabel("temp")
plt.savefig("Calgary 2015 temp",format="png")
plt.show()


date_st2015,max_st2015,min_st2015=read_weather2('c:/Users/Sharon/Documents/GitHub/GDD/csv_data/st_johns/2015.csv')
max_st2015=max_st2015.astype(float)
min_st2015=min_st2015.astype(float)
date_st2015=pd.to_datetime(date_st2015)
maxy_st2015,=plt.plot_date(date_st2015,max_st2015,'ro-',label="max temp")
mint_st2015,=plt.plot_date(date_st2015,min_st2015,'cx-',label="min temp")
plt.legend(handles=[maxy_st2015,mint_st2015])
plt.title("Stjohns 2015 temp")
plt.ylabel("temp")
plt.xlabel("date")
plt.savefig("Stjohns 2015 temp",format="png")
plt.show()

date_tor2015,max_tor2015,min_tor2015=read_weather2('c:/Users/Sharon/Documents/GitHub/GDD/csv_data/toronto/2015.csv')
max_tor2015=max_tor2015.astype(float)
min_tor2015=min_tor2015.astype(float)
date_tor2015=pd.to_datetime(date_tor2015)
maxy_tor2015,=plt.plot_date(date_tor2015,max_tor2015,'ro-',label="max temp")
mint_tor2015,=plt.plot_date(date_tor2015,min_tor2015,'cx-',label="min temp")
plt.legend(handles=[maxy_tor2015,mint_tor2015])
plt.title("Toronto 2015 temp")
plt.ylabel("temp")
plt.xlabel("date")
plt.savefig("Toronto 2015 temp",format="png")
plt.show()

date_cal2016,max_cal2016,min_cal2016=read_weather('c:/Users/Sharon/Documents/GitHub/GDD/csv_data/calgary/2016.csv')
max_cal2016=max_cal2016.astype(float)
min_cal2016=min_cal2016.astype(float)
date_cal2016=pd.to_datetime(date_cal2016)
maxy_cal2016,=plt.plot_date(date_cal2016,max_cal2016,'ro-',label="max temp")
mint_cal2016,=plt.plot_date(date_cal2016,min_cal2016,'cx-',label="min temp")
plt.legend(handles=[maxy_cal2016,mint_cal2016])
plt.title("Calgary 2016 temp")
plt.ylabel("temp")
plt.xlabel("date")
plt.savefig("Calgary 2016 temp",format="png")
plt.show()

date_tor2016,max_tor2016,min_tor2016=read_weather2('c:/Users/Sharon/Documents/GitHub/GDD/csv_data/toronto/2016.csv')
max_tor2016=max_tor2016.astype(float)
min_tor2016=min_tor2016.astype(float)
date_tor2016=pd.to_datetime(date_tor2016)
maxy_tor2016,=plt.plot_date(date_tor2016,max_tor2016,'ro-',label="max temp")
mint_tor2016,=plt.plot_date(date_tor2016,min_tor2016,'cx-',label="min temp")
plt.legend(handles=[maxy_tor2016,mint_tor2016])
plt.title("Toronto 2016 temp")
plt.ylabel("temp")
plt.xlabel("date")
plt.savefig("Toronto 2016 temp",format="png")
plt.show()

date,max_temp,min_temp=read_weather3('C:/Users/Sharon/Documents/GitHub/GDD/csv_data/st_johns/2016.csv')
date=date[1:156]
max_temp=max_temp[1:156]
min_temp=min_temp[1:156]
max_temp=max_temp.astype(float)
min_temp=min_temp.astype(float)
date=pd.to_datetime(date)
maxy,=plt.plot_date(date,max_temp,'ro-',label="max temp")
mint_,=plt.plot_date(date,min_temp,'cx-',label="min temp")
plt.legend(handles=[maxy_tor2016,mint_tor2016])
plt.title("St.johns 2016 temp")
plt.ylabel("temp")
plt.xlabel("date")
plt.savefig("St.johns 2016 temp",format="png")
plt.show()
