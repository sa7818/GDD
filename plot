import numpy as np
import matplotlib.pyplot as pyplot
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as dt
import pandas as pd

#data_url = "1.csv"
#df = pd.read_csv(data_url)
def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter



def read_weather(file_name):

    dtypes = np.dtype({ 'names' : ('date','max temp', 'min temp'),
                        'formats' : ['S9', np.float,np.float] })

    dates,max_temp,min_temp = np.loadtxt(file_name, delimiter=',', skiprows=1,
            usecols=(0,1,2),dtype=dtypes,unpack=True,converters={0:dt.bytespdate2num('%m/%d/%Y')})    
    return dates,max_temp,min_temp
    

#Toronto_city 2015 temp plot   
dates,max_temp,min_temp=read_weather('TORONTO _CITY.csv')
maxy,=plt.plot_date(dates,max_temp,'ro-',label="max temp")
mint,=plt.plot_date(dates,min_temp,'cx-',label="min temp")
plt.legend(handles=[maxy,mint])
plt.title("Toronto_city 2015 temp")
plt.ylabel("temp")
plt.xlabel("date")
plt.show()

#Alberta 2015 temp plot   
dates,max_temp,min_temp=read_weather('ALBERTA.csv')
maxy,=plt.plot_date(dates,max_temp,'ro-',label="max temp")
mint,=plt.plot_date(dates,min_temp,'cx-',label="min temp")
plt.legend(handles=[maxy,mint])
plt.title("Alberta 2015 temp")
plt.ylabel("temp")
plt.xlabel("date")
plt.show()

#St.john's 2015 temp plot   
dates,max_temp,min_temp=read_weather('ST.JOHNS.csv')
maxy,=plt.plot_date(dates,max_temp,'ro-',label="max temp")
mint,=plt.plot_date(dates,min_temp,'cx-',label="min temp")
plt.legend(handles=[maxy,mint])
plt.title("St.john's 2015 temp")
plt.ylabel("temp")
plt.xlabel("date")
plt.show()

# Three City's 2015 temp showed in three sub-plot
plt.subplot(3,1,1)
dates,max_temp,min_temp=read_weather('TORONTO _CITY.csv')
maxy=plt.plot_date(dates,max_temp,'ro-',label="max temp")
mint=plt.plot_date(dates,min_temp,'cx-',label="min temp")
plt.title("Toronto_city 2015 temp")

plt.subplot(3,1,2)
dates2,max_temp2,min_temp2=read_weather('ALBERTA.csv')
maxy2=plt.plot_date(dates2,max_temp2,'ro-',label="max temp")
mint2=plt.plot_date(dates2,min_temp2,'cx-',label="min temp")
plt.title("Alberta 2015 temp")
plt.ylabel("temp")


dates3,max_temp3,min_temp3=read_weather('ST.JOHNS.csv')
maxy3=plt.plot_date(dates3,max_temp3,'ro-',label="max temp")
mint3=plt.plot_date(dates3,min_temp3,'cx-',label="min temp")
plt.title("St.john's 2015 temp")
plt.ylabel("temp")
plt.subplot(3,1,3)

plt.show()
