from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
# setup Lambert Conformal basemap.
m = Basemap(width=12000000,height=9000000,projection='lcc',
            resolution='c',lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
# draw a boundary around the map, fill the background.
# this background will end up being the ocean color, since
# the continents will be drawn on top.
m.drawmapboundary(fill_color='aqua')
# fill continents, set lake color same as ocean color.
m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
# label parallels on right and top
# meridians on bottom and left
parallels = np.arange(0.,81,10.)
# labels = [left,right,top,bottom]
m.drawparallels(parallels,labels=[False,True,True,False])
meridians = np.arange(10.,351.,20.)
m.drawmeridians(meridians,labels=[True,False,False,True])
# plot blue dot on Boulder, colorado and label it as such.
lon, lat = -104.237, 40.125 # Location of Boulder
# convert to map projection coords.
# Note that lon,lat can be scalars, lists or numpy arrays.
xpt,ypt = m(lon,lat)
# convert back to lat/lon
lonpt, latpt = m(xpt,ypt,inverse=True)
m.plot(xpt,ypt,'bo')  # plot a blue dot there
# put some text next to the dot, offset a little bit
# (the offset is in map projection coordinates)
plt.text(xpt+100000,ypt+100000,'Boulder (%5.1fW,%3.1fN)' % (lonpt,latpt))
plt.show()


#
# from mpl_toolkits.basemap import Basemap
# import matplotlib.pyplot as plt
# import numpy as np
# # set up orthographic map projection with
# # perspective of satellite looking down at 45N, 100W.
# # use low resolution coastlines.
# map = Basemap(projection='ortho',lat_0=45,lon_0=-100,resolution='l')
# # draw coastlines, country boundaries, fill continents.
# map.drawcoastlines(linewidth=0.25)
# map.drawcountries(linewidth=0.25)
# map.fillcontinents(color='coral',lake_color='aqua')
# # draw the edge of the map projection region (the projection limb)
# map.drawmapboundary(fill_color='aqua')
# # draw lat/lon grid lines every 30 degrees.
# map.drawmeridians(np.arange(0,360,30))
# map.drawparallels(np.arange(-90,90,30))
# # make up some data on a regular lat/lon grid.
# nlats = 73; nlons = 145; delta = 2.*np.pi/(nlons-1)
# lats = (0.5*np.pi-delta*np.indices((nlats,nlons))[0,:,:])
# lons = (delta*np.indices((nlats,nlons))[1,:,:])
# wave = 0.75*(np.sin(2.*lats)**8*np.cos(4.*lons))
# mean = 0.5*np.cos(2.*lats)*((np.sin(2.*lats))**2 + 2.)
# # compute native map projection coordinates of lat/lon grid.
# x, y = map(lons*180./np.pi, lats*180./np.pi)
# # contour data over the map.
# cs = map.contour(x,y,wave+mean,15,linewidths=1.5)
# plt.title('contour lines over filled continent background')
# plt.show()