# -*- coding: utf-8 -*-
"""
FauqClarke.py

Goal: Script for analyzing Fauquier and Clarke County well data
Created on Fri Aug 17 15:10:25 2018

@author: nchien
"""

# Import classes and functions from 'wellmining.py'
from wellmining_v2 import Well

"""Update/Initiate wells"""
# Find todays date
import datetime as dt
t_now = dt.datetime.now()
end_date = str(t_now.year) + '-' + str(t_now.month) + '-' + str(t_now.day)
# Fauquier County wells
w48U32 = Well('385207077493301')            # North Fauq Comm Park-Fauquier, record starts '2016-09-08'
w49U81 = Well('384348077405401')            # Kettle Run HS-Fauquier, record starts '2017-01-06'
w48S38 = Well('383455077463101')            # Behind Houses-Fauquier, record starts '2017-02-15'
w48T07 = Well('384122077462601')            # Near Education Farm-Fauquier, record starts '2016-11-18'
w48U26SOW215 = Well('384957077481701')      # DEP Site-Fauquier, record starts '2007-10-01'
# Clarke County wells
w46W175 = Well('390348078035501')           # Blandy Exp. Farm-Clarke, record starts '2007-10-01'
w46X125 = Well('390948078001601')           # Clark Rec Area-Clarke, record starts '2008-04-19'
w48X20 = Well('390743077504501')            # Rockwood Farm-Clarke, record starts '2007-10-01'

# Plot all Fauquier County Wells
import matplotlib.pyplot as plt
plt.figure(1)
# North Fauq Comm Park
plt.subplot(511)
plt.plot(w48U32.rcntRecord.Levels)
plt.grid(True)
plt.ylabel('Water Level (ft)')
plt.title('Fauquier County Wells')
# Kettle Run HS
plt.subplot(512)
plt.plot(w49U81.rcntRecord.Levels)
plt.grid(True)
plt.ylabel('Water Level (ft)')
# Behind Houses
plt.subplot(513)
plt.plot(w48S38.rcntRecord.Levels)
plt.grid(True)
plt.ylabel('Water Level (ft)')
# Near Education Farm
plt.subplot(514)
plt.plot(w48T07.rcntRecord.Levels)
plt.grid(True)
plt.ylabel('Water Level (ft)')
# DEP Site
plt.subplot(515)
plt.plot(w48U26SOW215.rcntRecord.Levels)
plt.grid(True)
plt.ylabel('Water Level (ft)')
plt.xlabel('Date-Time')

# Plot all Clarke County Wells
plt.figure(2)
# Blandy Experimental Farm
plt.subplot(311)
plt.plot(w46W175.rcntRecord.Levels)
plt.grid(True)
plt.ylabel('Water Level (ft)')
plt.title('Clarke County Wells')
# Clark Rec Area
plt.subplot(312)
plt.plot(w46X125.rcntRecord.Levels)
plt.grid(True)
plt.ylabel('Water Level (ft)')
# Rockwood Farm
plt.subplot(313)
plt.plot(w48X20.rcntRecord.Levels)
plt.grid(True)
plt.ylabel('Water Level (ft)')
plt.xlabel('Date-Time')



