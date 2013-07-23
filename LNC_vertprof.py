# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:15:48 2013

@author: dashamstyr
"""

import os, sys
import numpy as np
import datetime as dt
import bisect
import matplotlib.pyplot as plt
import matplotlib.colors as clr
import pandas as pan
import LNC_tools as LNC
import LNC_plot as LNCplt

minalt = 500
maxalt = 8000

os.chdir('F:\Siberian Smoke Data\CORALNet Data\WHI\July3')

filepath = LNC.get_files('Select data file', filetype = ('.pickle','*.pickle'))
            
if filepath[0] == '{':
    filepath = filepath[1:-1]

[path, filename] = os.path.split(filepath)

os.chdir(path)
df = pan.load(filename)
daterange = df.index
ymin = df.columns[0]
ymax = df.columns[-1]
df = df.loc[:,:maxalt]

df.loc[:,:minalt] = 'nan'


exact_time = []
approx_time = []

#exact_time.append(dt.datetime(2012,7,7,12,0,0))
#exact_time.append(dt.datetime(2012,7,8,12,0,0))
#exact_time.append(dt.datetime(2012,7,10,12,0,0))

exact_time.append(dt.datetime(2012,7,17,12,0,0))
exact_time.append(dt.datetime(2012,7,18,12,0,0))
exact_time.append(dt.datetime(2012,7,20,03,0,0))

#exact_time.append(dt.datetime(2012,8,6,12,0,0))
#exact_time.append(dt.datetime(2012,8,11,12,0,0))
#exact_time.append(dt.datetime(2012,8,13,12,0,0))

for ts in exact_time:    
    i = bisect.bisect_left(daterange, ts)
    approx_time.append(min(daterange[max(0, i-1): i+2], key=lambda t: abs(ts - t)))

fig = plt.figure()

numprof = len(approx_time)

for n in range(numprof): 
    print approx_time[n]
    s = df.ix[approx_time[n]]
    s = s[s>0]
    alt = s.index
    print s.max()
    ax = fig.add_subplot(1,numprof,n+1)
    
    if 'BR' in filename:
        im = ax.plot(s,alt, linewidth = 4)
        plt.ylim([ymin,ymax])
        plt.xlim([1,8])
        plt.xlabel('Backscatter Ratio',fontsize = 21)
    
    if 'PR' in filename:
        im = ax.scatter(s,alt)
        plt.ylim([ymin,ymax])
        plt.xlim([0,0.5])
        plt.xlabel('Depolarization Ratio',fontsize = 21)
    
    plt.yticks(fontsize = 21)
    plt.ylabel('Altitude [m]', fontsize = 21)
    
    for line in ax.yaxis.get_ticklines():
        line.set_color('k')
        line.set_markersize(6)
        line.set_markeredgewidth(2)
        
    for line in ax.xaxis.get_ticklines():
        line.set_color('k')
        line.set_markersize(6)
        line.set_markeredgewidth(2)    
        
    plt.xticks(fontsize = 21)
    plt.title(approx_time[n], fontsize = 21)
    fig.subplots_adjust(wspace = 0.5)

plt.show()
    