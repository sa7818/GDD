import sys
import numpy as np
import matplotlib.pyplot as pyplot
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as dt
import pandas as pd
import pickle

def calculate_gdd(filename,t_base,t_upper):
    Date,Max_Temp, Min_Temp=read_weather(filename)
    Max_Temp=Max_Temp.astype(float)
    Min_Temp=Min_Temp.astype(float)
    Total=Max_Temp+Min_Temp
    average=Total/2
    calcu_gdd=average-t_base
    gdd=(Max_Temp+Min_Temp)/2-t_base
    accumu_gdd=accu_gdd(Date,gdd)
    #print (accumu_gdd)
    Date,accumu_gdd=accu_gdd(Date,gdd)
    new_csv=np.array([
            ('Date',Date),
            ('Max_Temp',Max_Temp),
            ('Min_Temp',Min_Temp),
            ('calcu_gdd',calcu_gdd),
            ('accumu_gdd',accumu_gdd),
            ])
    return Date,Max_Temp,Min_Temp,calcu_gdd,accumu_gdd
    #return new_csv
    

def fetch_csv(file_name):
	#Read csv file
   	try:
		data = pd.read_csv(file_name, usecols=(0,1,2),encoding='ISO-8859-1')
		return data
	except:
		print("Unexpected error:", sys.exc_info()[0])
		raise

def print_csv(data):
	print(data)

def accu_gdd(Date,gdd):
    gdd[gdd<0]=0
    #accu_gdd=range(1,Date)
    accu_gdd=0
    list_accu_gdd=np.array([])
    for i in gdd:        
        accu_gdd=accu_gdd+i       
        list_accu_gdd=np.append(list_accu_gdd,accu_gdd)  
        #list_accu_gdd=list_accu_gdd.astype(float)
    return Date,list_accu_gdd

def main(argv):
    # My code here
    pass

if __name__ == "__main__":
    main(sys.argv)


