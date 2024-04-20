
import math
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

from copy import deepcopy
import tqdm

from tsp_func import *

plt.rc('animation', html='html5')

csv_path = './ro.csv'
romania = pd.read_csv(csv_path)
ro = parse_latlng(csv_path)
x = [c.x for c in ro]
y = [c.y for c in ro]

minx , maxx = min(x) , max(x)
miny , maxy = min(y) , max(y)

lat = romania['lat'].values
lon = romania['lng'].values
pop = romania['population'].values



fig = plt.figure(figsize=(6, 6))
m = Basemap(projection='lcc', resolution='l', 
            lat_0=46, lon_0=25,
            width=0.8E6, height=0.8E6)

m.drawmapscale(47, 26, lon0=25, lat0=46, length=100)
# m.shadedrelief(scale=0.5)
m.drawcoastlines(color='gray')
m.drawcountries(color='black')

# 2. scatter city data
m.scatter(lon, lat, latlon=True, c='red', s=20, alpha=0.6)

plt.show()



