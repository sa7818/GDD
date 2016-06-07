import os
import urllib
import requests

def download_file():
#takes id and year of a station as argument and download weather file from the url.
	station_Ids=[50089,5051,27211]
	years=[2015,2016]
	city=""
	for id in station_Ids:
		if(id==50089):
			city="st_johns"
		elif(id==5051):
			city="toronto"
		else:
			city="calgary"
		for year in years:
			fname= "../csv_data/{}/{}.CSV".format(city,year)
			url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="+str(id)+"&Year="+str(year)+"&Month=8&Day=1&timeframe=2&submit=Download+Data"
			urllib.request.urlretrieve(url,fname)   
        
		
	return
	
download_file()
