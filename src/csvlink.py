import os
import urllib
import requests
import pandas as pd

def download_file():
#Download CSV file from the url provided in the code
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
            fname= "../CSV_data/{}/{}_{}.csv".format(city,city,year)
            url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="+str(id)+"&Year="+str(year)+"&Month=8&Day=1&timeframe=2&submit=Download+Data"
            urllib.request.urlretrieve(url,fname)   
            
#Column extraction below
            data_frame = pd.read_csv(fname, skiprows=25, sep=",", encoding="ISO-8859-1")
        #df = pandas.DataFrame("../GDD/CSV_data/"+str(i)+"_"+str(year)+r"_gdd.csv")
            columns = [0,1,2,3,5,7,9]
            df = data_frame[columns]
            new_fname =  "../CSV_data/{}/{}_{}_extract.csv".format(city,city,year)
            df.to_csv(new_fname)
    return

download_file()   
