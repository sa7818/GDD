import urllib.request
import urllib.parse

list = ["6722"]

for i in list:
#	for j in range(1:13)
    url = ("http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=list[i]&Year=1996&Month=8" + 
      "&Day=1&timeframe=2&submit=Download+Data")

    value = {'stationID': 'list[i]',
             'Year': '1996', 
             'Month': '1',
             'Day': '1',
             'timeframe': '2',
             'submit': 'Download+Data'}
    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data)
    datafile = urllib.request.urlopen(req)
    dataset = datafile.read()
    dataset_str = dataset.decode()
print(dataset_str)
