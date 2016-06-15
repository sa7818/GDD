import numpy as np
import matplotlib.pyplot as pyplot
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as dt
import pandas as pd
import csv
import sys
from scipy import stats
import numpy as np
import pylab
 
def read_weather_analyze(file_name):
    """
        This is function is to read data for analyze gdd for optional task 6
    The data read from the above function(read_weather_analyze(file_name)),
    the argv is .csv data file  and the return value are year,month,day and mean_temp
    argv :
        filename (csv data file)
    output:
        data,year,month,day,mean_temp
    """
    #Read gdd file the the third column-year,fourth column-Month, the fifth column-day and the eighth column- mean_temp
    data=pd.read_csv(file_name, usecols=(2,3,4,7),encoding='ISO-8859-1',delimiter =',') 
    #To make sure there hasn't missing data in the data file, if it has replace E to NAN in csv data file
    data.replace('E', np.nan,inplace=True)
    #To make sure there hasn't estimated data in the data file, if it has replace M to NAN in csv data file
    data.replace('M', np.nan,inplace=True)
    #Then Remove all the 'NAN' data in csv data file
    data = data.dropna(how='any')
    #Get the value of thrid column-year
    year=data['Year']
    #Get the value of fourth column-month
    month=data['Month']
    #Get the value of fifth column-day
    day=data['Day']
    #Get the value of eighth column-mean temp
    mean_temp=data['Mean_Temp']
    #return data,year,month,day,mean_temp
    return data,year,month,day,mean_temp

def analyze_gdd(filename1, filename2, filename3):
    
    """
    This is function for analyze at most three year's GDD variation,
    and plot linear regression to saw the GDD tendency gdd which is optional task 6
    The data read from the above function(analyze_gdd(filename1, filename2, filename3)),
    the argv of input can be one, two at most three.
    eg: analyze_gdd(filename1,None,None) or analyze_gdd(filename1,filename2,None) 
    or analyze_gdd(filename1,filename2,filename3) 
    the argv is .csv data file  and the return value is image with .png format
    argv :
        filename (csv data file), argv at most three
    output:
        image with .png format
    """
    #To list all the argv 
    data_to_plot2=[filename1,filename2,filename3]
    #To remove None from the argv
    data_to_plot = [x for x in data_to_plot2 if x is not None]
    #To iterate each file_name in the function analyze_gdd
    for i in data_to_plot:
    #get data, year, month,day and mean_temp from read_weather_analyze() function
        data,year,month,day,mean_temp=read_weather_analyze(i)
        #To replace data has 0 to NAN, because we do not need 0 data to plot gdd
        data.replace('0',np.nan,inplace=True)
        #To remove all the NAN data
        data=data.dropna(how='any')
        #To convert date type into integer data type for linear regression
        x=10000*year + 1000*month + day
        #To put the x into frames_x list
        frames_x= [x]
        #In this case, the t-base is 10,then gdd would be mean_temp-10, and save the gdd into frames_y list
        frames_y= [mean_temp-10]
    #To takes frames_x list and concatenates them to x 
    x = pd.concat(frames_x)
    #To takes frames_y list and concatenates them to y 
    y=  pd.concat(frames_y)
    #To remove NaNs in the data using a mask:
    mask = ~np.isnan(x) & ~np.isnan(y)
    #Calculate a linear least-squares regression for two sets of measurements and remove all NAN in x and y
    #and to get estimates of the slope and intercept parameters.
    slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x[mask], y[mask])
    #To get predict_y by the following function
    predict_y = intercept + slope * x  
    fig,ax1=plt.subplots()
    #To set x-axis label
    ax1.set_xlabel('Time')
    #To set y-axis label
    ax1.set_ylabel('Expected Result')
    #To set the title in the linear regression plot graph
    ax1.set_title('linear regression')
    #first to plot x and y
    pylab.plot(x, y, 'o')
    #second to plot liner regression
    pylab.plot(x, predict_y, 'k-')
    analyze_gdd=plt.savefig("analyze_gdd.png",format="png")
    #To save the fig with .png format
    return analyze_gdd

"""
Try statement can handle exception.
The input is .csv file, it will run analyze_gdd(filename1, filename2, filename3) to plot linear regression
Before run the plot_gdd() function, it will first check the number of input. 
eg: it can be analyze_gdd(filename1, None  , None) or analyze_gdd(filename1, filename2, None),
or analyze_gdd(filename1, filename2, filename3)
In this case, it allows at most three input into the function of analyze_gdd()
"""
try:
    file_name = sys.argv[1]
    #file_name = "50089_2015.csv"

    try:
        filename2 = sys.argv[2]
    except:
        analyze_gdd(file_name, None, None)
    else:            
        try:
            filename3 = sys.argv[3]
        except:
            analyze_gdd(file_name, filename2, None)
        else:
            analyze_gdd(file_name, filename2, filename3)
                
except Exception as e:
    raise e
    print (e)
    
