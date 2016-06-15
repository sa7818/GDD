from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# define Lambert Conformal basemap.
m = Basemap(llcrnrlon=-147.9927,llcrnrlat=45.49,urcrnrlon=-36.4459,urcrnrlat=72.8125,
            projection='lcc',resolution='c', area_thresh = 10000.0,width=12000,height=9000,lat_0=54.2812865,lon_0=-116.,lat_1=-4.)

m.drawcoastlines()

m.drawmapboundary(fill_color='#88cfff')

m.fillcontinents(color='#dd9966',lake_color='#77cfff')
m.drawcountries()
m.drawcoastlines()
meridians = np.arange(180.,360.,10.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)


raw_data = {'Year': [2001, 2002, 2003, 2004, 2005],
            'St John\s': [644.6, 549.8, 708.5, 575.8, 616.8],
            'ON Kanata': [1375.5, 1315, 1285, 1150, 1426],
            'Montreal': [1481, 1370, 1374, 1246, 1473],
            'Calgary': [729.4, 624.89, 782.6, 584.9, 501.5],
            'Vancouver': [1002, 1030, 1135, 1240, 1087],
            'Saskatoon': [342.4, 298, 365.1, 352.9, 235.7],
            'Saint John': [783.2, 689.9, 761.3, 602.7, 708.5],
            'Charlettetown': [1024, 820, 1002, 817.4, 903],
            'Halifax': [1087, 904, 1070, 875.3, 1013]}
df = pd.DataFrame(raw_data, columns = ['Year', 'St John\s', 'ON Kanata', 'Montreal', 'Calgary', 'Vancouver', 'Saskatoon', \
                                       'Saint John', 'Charlettetown', 'Halifax'])
df.to_csv('../csv_data/canData.csv')

columns=[2, 3, 4, 5, 6, 7 ,8 ,9, 10]
data = pd.read_csv('../csv_data/canData.csv', sep=',', encoding='ISO-8859-1')
data = data[columns]
NL = data['St John\s']
ON = data['ON Kanata']
MN = data['Montreal']
CG = data['Calgary']
VC = data['Vancouver']
SK = data['Saskatoon']
NB = data['Saint John']
PE = data['Charlettetown']
NS = data['Halifax']


Eff_GDD = []
#for r in sj:
Eff_GDD.append(sum(NL)/len(NL))
Eff_GDD.append(sum(ON)/len(ON))
Eff_GDD.append(sum(MN)/len(MN))
Eff_GDD.append(sum(CG)/len(CG))
Eff_GDD.append(sum(VC)/len(VC))
Eff_GDD.append(sum(SK)/len(SK))
Eff_GDD.append(sum(NB)/len(NB))
Eff_GDD.append(sum(PE)/len(PE))
Eff_GDD.append(sum(NS)/len(NS))

lons = [-127.6476, -116.5765, -106.4509, -98.8139,-85.3232, -73.5491, -63.7443, - 63.4168, -66.4619, -57.6604]
lats = [53.7267, 53.9333, 52.9399, 53.7609, 51.2538, 52.9399, 44.6820, 46.5107, 46.5653, 53.1355]
x,y = m(lons, lats)
m.plot(x, y, 'ro', markersize=10)
 
    
labels = ['BC', 'Alberta', 'Sask', 'Manitoba', 'Ontario', 'Quebec', 'Nova Scotia', 'P. Edward', 'NB', 'NL']
x_offsets = [-10000, -30000, 25000, 10000, -25000, -20000, 35000, 25000, 45000, 15000]
y_offsets = [10000, -50000, -35000, 5000, -25000, 5000, 35000, - 15000, -20000, 15000]

for label, xpt, ypt, x_offset, y_offset in zip(labels, x, y, x_offsets, y_offsets):
    plt.text(xpt+x_offset, ypt+y_offset, label, zorder=4)
 
plt.title("EFFECTIVE DEGREE MAP FOR CANADA and NL")
plt.savefig("../output/effec_degreeCanada",format="png")

