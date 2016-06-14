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
fig,ax1=plt.subplots()
ax2=ax1.twinx()


def read_weather(file_name):
    """
    This function is just used for read data(Date/Time,Max_Temp,Min_Temp) to plot max_min from file_name.
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

def read_weather_gdd(file_name):
    """
        This is function to read data for plot gdd for task 4
    The data read from the above function(read_weather_gdd(file_name)),
    the argv is .gdd data file get it from gdd.py 
    and the return value are month,GDD number and Accumulateed GDD
    argv :
        filename (gdd data file)
    output:
        month,GDD number and Accumulateed GDD
    """
    #Read gdd file the third column-Month, the fifth column-GDD and the sixth column-accumulated gdd number
    data=pd.read_csv(file_name, usecols=(2,4,5),encoding='ISO-8859-1',delimiter =',') 
    #To make sure there hasn't missing data in the data file, if it has replace E to NAN in gdd data file
    data.replace('E', np.nan,inplace=True)
    #To make sure there hasn't estimated data in the data file, if it has replace M to NAN in gdd data file
    data.replace('M', np.nan,inplace=True)
    #Then Remove all the 'NAN' data in gdd data file
    data = data.dropna(how='any')
    #Get the value of third column-month
    month=data['Month']
    #Get the value of fifth column-GDD
    gdd_num=data['GDD']
    #Get the value of sixth column-accumulated gdd
    accu_gdd_num=data['Acc_GDD']
    #return date,month,max_temp and min_temp
    return data,month,gdd_num, accu_gdd_num

def plot_gdd(filename1, filename2, filename3):
    """
    This  function is to plotting gdd, the function has at most three data file to plot gdd graph.
    All the data file are get from gdd.py and the data would be .gdd data file 
    argv :
        filename1 (gdd data file)
        filename2 (gdd data file)
        filename3 (gdd data file)
        The argv can be 1 to 3, and at most three data file
    output:
        The image of data_file gdd plot and long_term average gdd plot
        And the image format is .png
    """  

    #To put all the argv into a list, this list is used for caluclate long-term average gdd
    data_to_plot2=[filename1,filename2,filename3]
    #To remove none in the argv, the data_to_plot is the real argv and get it from user's input
    data_to_plot = [x for x in data_to_plot2 if x is not None]
    #To define a two-dimenstion list to caluclate long-term average gdd
    avg_yrs = np.ndarray(shape=(2,365), dtype=float)
    #To define a variable, which will be used in for loop
    cnt = 0
    #To get each file in the data_to_plot
    for i in data_to_plot:
        #To get data, month, gdd num and accumulated gdd number from function read_weather_gdd 
        data,month,gdd_num,accu_gdd_num=read_weather_gdd(i)
        #If the gdd or accumulated gdd's value is 0, then replace this value into nan.
        data.replace('0',np.nan,inplace=True)
        #To remove all the 0 value's column
        data=data.dropna(how='any')
        #To get all the accumulated gdd value.eg: the argv has two filename, 
        #then y_aver has two accumulated gdd number list
        y_aver=accu_gdd_num
        #To define a two_demension list to get accu_gdd_num,
        #then we can add the accumulated gdd num column by column
        avg_yrs[cnt] = accu_gdd_num
        cnt = cnt + 1
        #To define labels which will showed in x-axis
        labels=['June','July','August','Septeber','October','November','December']
        #To define x-axis with index
        index = np.arange(0, 365) 
        #To set x-tick-axis with the above labels
        ax1.set_xticklabels(labels)
        #To add grid to make plot more readable             
        grd = plt.grid(True)
        #To automatically update ylim of ax2 when ylim of ax1 changes. 
        ax1.callbacks.connect("ylim_changed", convert_ax_c_to_celsius)
        #To define the plot label
        l=i[6:10]+" year at "+i[0:5]
        #To plot gdd
        ax1.plot(index,convert_c_to_f(accu_gdd_num),label=l,linewidth=2.5, linestyle="-") 
        #To show the legend
        ax1.legend(loc=2,shadow=True)
        #To add x-axis-label with month
        ax1.set_xlabel('Month',fontsize=12)
        #To set left y-axis label
        ax1.set_ylabel('cumulative GDD based on Fahrenheit',fontsize=15, color='b')
        #To set right y-axis label
        ax2.set_ylabel('cumulative GDD based on celsius',fontsize=15, color='b')
        #To add title into the plot
        ax1.set_title('Accumulate Growing Degree Days Graph',fontsize=20, color='k')
    #To plot the long_term average gdd     
    ax1.plot(index,convert_c_to_f(np.sum(avg_yrs, axis=0)/len(data_to_plot)),label="Long-Term Average",linewidth=2.5, linestyle="-",color="black")
    #To show the legend
    ax1.legend(loc=2,shadow=True)
    gdd_plot=plt.savefig("plot_gdd_"+filename1[:-3] + "png",format="png")
    return gdd_plot   #Return the plot gdd image with .png format
    

    

def convert_c_to_f(accu_gdd_num):
    """
    This function is to Convert the temparature of celsius to Fahrenheit
    """
    f=accu_gdd_num*1.8+32
    return f #Returns temperature in Fahrenheit.
    
def convert_ax_c_to_celsius(ax1):
    """
    Update second axis according with first axis in which two scales on the left and right y axis.
    """
    
    y1, y2 = ax2.get_ylim()
    ax2.set_ylim(convert_c_to_f(y1), convert_c_to_f(y2))
    ax2.figure.canvas.draw()

"""
Try statement can handle exception.
If the input is .csv file, then it will run plot_maxmin(file_name) to plot max and min temp 
If the input is .gdd file, it will run plot_gdd() function to plot accumulated gdd and long-term average gdd 
Before run the plot_gdd() function, it will first check the number of input. 
In this case, it allows at most three input into the function of plot_gdd()
"""

try:
    file_name = sys.argv[1]
    #file_name = "50089_2015.csv"
    fileformat = file_name[-3:]
    #print("ff:" + fileformat)
    if fileformat == "csv":
        plot_maxmin(file_name)
    else:
        try:
            filename2 = sys.argv[2]
        except:
            plot_gdd(file_name, None, None)
        else:            
            try:
                filename3 = sys.argv[3]
            except:
                plot_gdd(file_name, filename2, None)
            else:
                plot_gdd(file_name, filename2, filename3)
                
except Exception as e:
    raise e
    print (e)
    
