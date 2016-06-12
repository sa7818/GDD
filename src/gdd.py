import sys
import os.path
import csv
import pandas as pd

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
    t_base = int(t_base)
    t_upper = int(t_upper)
    if os.path.isfile(filename):
        print("~ Filename: {} exists!".format(filename))
        csv = fetch_csv(filename)
    # Iterate through the fetched file and calculate gdd
    mean_col = csv['Mean_Temp']
    date_cols = csv[['Year', 'Month','Day']]
    columns = ['Year', 'Month','Day', 'GDD', 'Acc_GDD']
    df = pd.DataFrame(columns = columns)
    df['Year'] = date_cols['Year']
    df['Month'] = date_cols['Month']
    df['Day'] = date_cols['Day']
    i = 0
    # calculating GDD column
    for m in  mean_col:
        gdd = int(m) - t_base
        if gdd < 0:
            gdd = 0
        elif gdd > t_upper:
            gdd = t_upper
        df['GDD'][i] = gdd
        i+=1
    # Calculating ACC_GDD column
    j = 0
    for g in df['GDD']:
        if j == 0:
            df['Acc_GDD'][j] = df['GDD'][0]
        else:
            df['Acc_GDD'][j] = int(g) + df['Acc_GDD'][j - 1] 
        j+=1
    # create a csv out of a dataframe

    df = df.fillna(0)
    f_name = filename[:-4]
    f_name = f_name + ".gdd"
    try:
        df.to_csv("../csv_data/" + f_name)
    except:
        print("Something went wrong!")
    print("{0} is created.".format(f_name))
    return f_name
    #print(df)

# Entry point of gdd functionality:
try:
    filename = sys.argv[1]
    tbase = sys.argv[2]
    tupper = sys.argv[3]
    generate_gdd(filename, tbase,tupper)
except:
    print("Enter the parameters correctly")

