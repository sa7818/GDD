import os
import urllib.request
import sys
import pandas as pd


""" Script for downloading data """
def download(stationid, year):
	print("Started downloading ...")
	print("Data for station with id {} for year {}".format(stationid, year))
	
	fname = "{}_{}_t.csv".format(stationid, year)
	url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="+str(stationid)+"&Year="+str(year)+"&Month=8&Day=1&timeframe=2&submit=Download+Data"

	try:
	    urllib.request.urlretrieve(url, fname)
	except FileNotFoundError as fnfe:
		print("File not found error")
		print("%s" % fnfe)
		return ""
	except Exception as e:
		print("%s" % e)
		return ""
	
	print("Download completed...")
	print("Extracting required columns...")
	
	data_frame = pd.read_csv(fname, skiprows=25, sep=",", encoding="ISO-8859-1")
	columns = [0,1,2,3,5,7,9]
	df = data_frame[columns]
	df_rename = df.rename(columns={'Max Temp (°C)':'Max_Temp', 'Min Temp (°C)': 'Min_Temp', 'Mean Temp (°C)': 'Mean_Temp'})
	new_fname =  os.path.dirname(os.path.realpath(__file__)) + "/../csv_data/{}_{}.csv".format(stationid, year)
	df_rename.to_csv(new_fname)
	#print("File saved into: " + new_fname)

	# removing temporary saved file
	os.remove(fname)
	
	print("File saved.")

	return "{}_{}.csv".format(stationid, year)

try:
	file_name = sys.argv[1]
	file_name = file_name.split('.')[0]
	stationid, year = file_name.split('_')
	download(stationid, year)
except Exception as e:
	#raise e
	print (e)


