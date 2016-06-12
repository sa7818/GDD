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

plt.show()
