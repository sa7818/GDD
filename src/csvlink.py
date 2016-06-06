import urllib.request
import re

list = [50089,5051,27211]
Year = [2015,2016]
#dataset = []
#count = 0
for i in list:
    for year in Year:
        url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="+str(i)+"&Year="+str(year)+"&Month=8&Day=1&timeframe=2&submit=Download+Data"
        #    datafile = urllib.request.urlopen(url)
        datafile = urllib.request.urlretrieve(url, "/home/tosicky/GDD/CSV_data/"+str(i)+"_"+str(year)+r"_gdd.csv")
