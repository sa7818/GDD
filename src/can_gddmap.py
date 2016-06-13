from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# setup Lambert Conformal basemap.
m = Basemap(llcrnrlon=-147.9927,llcrnrlat=45.49,urcrnrlon=-36.4459,urcrnrlat=72.8125,
            projection='lcc',resolution='c', area_thresh = 10000.0,width=12000,height=9000,lat_0=30.83158,lon_0=-50.,lat_1=-4.)
# draw coastlines.
m.drawcoastlines()
# draw a boundary around the map, fill the background.
m.drawmapboundary(fill_color='#99ffff')

m.fillcontinents(color='#cc9966',lake_color='#99ffff')

lons = [-135.5334459, -123.9771791, -114.6620176, -104.4696027, -93.7388446, -77.412585, -69.2013865 ]
lats = [53.8330847, 54.1767615, 54.1780536, 54.1781594, 48.932973, 53.4633181, 53.1650697 ]
x,y = m(lons, lats)
m.plot(x, y, 'bo', markersize=10)
 
    
labels = ['BC', 'Alberta', 'Saskatchewan', 'Manitoba', 'Ontario', 'Quebec', 'Newfoundland']
x_offsets = [-25000, -30000, 25000, 10000, -25000, -20000, 15000]
y_offsets = [25000, -50000, -35000, 5000, -25000, 5000, 15000]

for label, xpt, ypt, x_offset, y_offset in zip(labels, x, y, x_offsets, y_offsets):
    plt.text(xpt+x_offset, ypt+y_offset, label)
 

plt.show()

plt.show()
