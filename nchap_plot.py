from netCDF4 import Dataset
import glob,os.path
import numpy as np
from scipy.interpolate import UnivariateSpline
from matplotlib import cm
import matplotlib.pyplot as plt
#import site
#site.addsitedir('/tera/phil/nchaparr/SAM2/sam_main/python')
#from Percentiles import *
from matplotlib.patches import Patch
import LNC_tools as LNC
from datetime import datetime, timedelta


"""
   To plot from lidar data files

"""

#set up plot
theFig = plt.figure(1)
theFig.clf()
theAx = theFig.add_subplot(111)
theAx.set_title('')
theAx.set_ylabel('height (meters)')
theAx.set_xlabel('hours from July 6 00:00:00')

df, product = LNC.lnc_reader('/home/datatmp/nchaparr/UBC_20120707_BR532.txt')
data, timestamps, altitudes = LNC.pandas_to_numpy(df)
print 'scattering limits', data.max(), data.min()

data = data[:,:1300]
xtick_ind = [int(i*1436.0/10) for i in range(10)]
ytick_ind = [int(i*1300.0/10) for i in range(10)]
xticks = [timestamps[ind] for ind in xtick_ind]
yticks = [altitudes[:1300][ind] for ind in ytick_ind]
yticks = list(reversed(yticks))

xticks1 = [int(1.0*(timestamps[ind] - np.datetime64('2012-07-06T00:00:00.000000000-0700'))/np.timedelta64(1, 'h')+7) for ind in xtick_ind]

print 'timestamps and durations from 0hrs', timestamps[1], timestamps[1430],  xticks, xticks1

im = theAx.imshow(data.T[::-1], aspect = .5, vmax=abs(data).max(), vmin=abs(data).min())
im.set_cmap('spectral')


plt.xticks(xtick_ind, xticks1)
plt.yticks(ytick_ind, yticks)
plt.colorbar(im, shrink = .5)
plt.show()

