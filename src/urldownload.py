import os
import urllib
import requests
import sys
import pandas as pd

#Download CSV file from the url provided in the code

file_name = sys.argv[1]
#year_value= sys.argv[2]
city, stationID, year = file_name[:-4].split('_')
#stationID = file_name
#year = year_value
#print(city,stationID, year)

def download(city,stationID,year):
#	file_name = sys.argv[1]
#	stationID, year = file_name[:-4].split('-')
#	print(stationID, year)
	fname= "../csv_data/{}_{}_{}.csv".format(city,stationID,year)
	url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="+str(stationID)+"&Year="+str(year)+"&Month=8&Day=1&timeframe=2&submit=Download+Data"
#	urllib.request.urlretrieve(url,fname)
	urllib.request.urlretrieve(url,fname)
#Column extraction below

#	data_frame = pandas.read_csv(fname, skiprows=25, sep=",", encoding="ISO-8859-1")
	data_frame = pd.read_csv(fname, skiprows=25, sep=",", encoding="ISO-8859-1")
	#df = pandas.DataFrame("../GDD/CSV_data/"+str(i)+"_"+str(year)+r"_gdd.csv")
	columns = [0,1,2,3,5,7,9]
	df = data_frame[columns]
	new_fname =  "../csv_data/{}_{}_{}_extracted.csv".format(city,stationID,year)
	df.to_csv(new_fname)

	return

download(city,stationID,year)
#	fname= "../GDD/CSV_data/{}_{}.csv".format(stationID,year)
#	url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?f$
#	csv_file = urllib.request.urlretrieve(url,fname)

