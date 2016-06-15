import sys
import os.path
import csv
import pandas as pd
import numpy as np

""" A function to fetch a csv file.

Args:
	file_name (string): the relative path of a csv file 
			     which is downloaded from server.
Returns:
	DataFrame: this dataframe is returned when the csv file exists in
		   ../csv_data/ directory.

"""
def fetch_csv(file_name):
    #Read csv file
    try:
        data = pd.read_csv(file_name,encoding='ISO-8859-1')
        return data
    except OSError as err:
        print("OSError : {0}".format(err))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

""" A function to generate a  *.gdd file in the same directory of ../csv_data/

Args:
	filename (String): the file name that has be .csv
	t_base (int):	   this parameter has to be the base temp for gdd.
	t_upper (int):	   this parameter is as a threshold that 
			   we use in our calculation.

Returns:
	string: filename of a *.gdd file

"""

def generate_gdd(filename, t_base, t_upper):
    tbase = float(t_base)
    csv_df = pd.DataFrame()
    if(float(t_upper)  == 0):
    # We assign a high value beacuse a high value makes this parameter unimportant in our calculations.
        t_upper = 100
    else:
        t_upper = float(t_upper)

    if os.path.isfile(filename):
        print("~ Filename: {} exists!".format(filename))
        csv_df = fetch_csv(filename)
    else:
         print("~ Filename: {} does not exist!".format(filename))
         return

    # Iterate through the fetched file and calculate gdd
    mean_col = csv_df['Mean_Temp']
    date_cols = csv_df[['Year', 'Month','Day']]
    df = pd.DataFrame(columns=['Year', 'Month','Day', 'GDD', 'Acc_GDD'])
    df['Year'] = date_cols['Year']
    df['Month'] = date_cols['Month']
    df['Day'] = date_cols['Day']
    i = 0
    # calculating GDD column
    for m in  mean_col:
        if m == '':
            m = 0
        gdd = float(m) - tbase
        if gdd < 0:
            gdd = 0
        elif gdd > t_upper:
            gdd = t_upper
        df.loc[i,'GDD'] = gdd
        i+=1
    # Calculating ACC_GDD column
    j = 0
    for g in df['GDD']:
        if j == 0:
            df.loc[j,'Acc_GDD'] = df.loc[0,'GDD']
        else:
            df.loc[j,'Acc_GDD'] = float(g) + df.loc[j-1,'Acc_GDD'] 
        j+=1
    # create a csv out of a dataframe

    df = df.fillna(0)
    
    f_name = os.path.basename(filename[:-4])
    f_name = f_name + ".gdd"

    try:
        df.to_csv(os.path.dirname(os.path.realpath(__file__)) + "/../csv_data/" + f_name)
    except Exception as e:
        print("Something went wrong!")
        print(e)

    print("{0} is created.".format(f_name))
    return f_name


# Entry point of gdd functionality:
try:
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        n = len(sys.argv)
        if (n == 2):
            # default values for these two parameters
            tbase = 10
            tupper = 30
        elif (n == 3):
            tbase = sys.argv[2]
            tupper = 30
        else:
            tbase = sys.argv[2]
            tupper = sys.argv[3]
        generate_gdd(filename, tbase,tupper)  
except Exception as e:
    #raise e
    print("Exception!")
    print(e)

    
	
