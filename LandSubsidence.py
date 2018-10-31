# -*- coding: utf-8 -*-
"""
LandSubsidence.py

Goal: Code used to analyze well data for land subsidence extensometers and 
wells. Preliminary plotting mechanisms in place
Created on Fri Aug 17 15:04:50 2018

@author: nchien
"""

# Import classes and functions from 'wellmining.py'
from wellmining import Well
from wellmining import Extens

"""Update/Initiate wells"""
# Land Subsidence wells
w55B16 = Well('364059076544901')            # Potomac-Franklin, record starts '2007-10-01'
print(1)
w58C56SOW162D = Well('365337076251601')     # Potomac-Suffolk, record starts at '2017-05-26'
print(2)
w59D34 = Well('365337076251601')            # Potomac1775ft-Nansemond, record starts at '2017-05-26'
print(3)
w59D35 = Well('365337076251602')            # Potomac930ft-Nansemond, record starts at '2017-05-26'
print(4)
w59D36 = Well('365337076251603')            # Potomac500ft-Nansemond, record starts at '2017-05-26'
print(5)
w59D37 = Well('365337076251604')            # PineyPt380ft-Nansemond, record starts at '2018-02-15'
print(6)
w59D40 = Well('365337076251607')            # Surficial26ft-Nansemond, record starts at '2017-04-26'
print(7)
# Extensometers
e55B60 = Extens('364101076544802', '2016-02-02', '2018-08-25')      # Franklin Extensometer, record starts at '2016-02-02'
e58C52 = Extens('364512076343701', '2016-02-19', '2018-08-25')      # Suffolk Extensometer, record starts at '2017-02-19'
e59D39 = Extens('365337076251606', '2018-03-28', '2018-08-25')      # Nansemond Extensometer, record starts at '2018-03-28'


"""Land Subsidence Comparison"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

## This is out of data, no longer have PoR fxn
## Determine indices for matching start dates
#start_date = '2018-03-28'
#end_date = '2018-08-15'
#iFrankStrt = e55B60.PoR.index(start_date) 
#iFrankEnd = e55B60.PoR.index(end_date)
#iSuffStrt = e58C52.PoR.index(start_date)
#iSuffEnd = e58C52.PoR.index(end_date)
#iNansStrt = e59D39.PoR.index(start_date)
#iNansEnd = e59D39.PoR.index(end_date)
#
## Convert arrays to numpy arrays
#cmpctFrank = np.array(e55B60.cmpct[iFrankStrt:iFrankEnd])
#cmpctSuff = np.array(e58C52.cmpct[iSuffStrt:iSuffEnd])
#cmpctNans = np.array(e59D39.cmpct[iNansStrt:iNansEnd])
#date_range = np.array(e55B60.PoR[iFrankStrt:iFrankEnd])
## Plot and compare
#plt.figure()
#axes = plt.axes()
#plt.plot(date_range, cmpctFrank)
#plt.plot(cmpctSuff)
#plt.plot(cmpctNans)
##axes.xaxis.set_major_locator(plt.MaxNLocator(20))
##axes.yaxis.set_major_locator(plt.MaxNLocator(20))
#plt.xlabel('Date')
#plt.ylabel('Daily Compaction (ft)')
#plt.title('Extensometer Records')
#plt.legend(['Franklin', 'Suffolk', 'Nansemond'])
#
#

