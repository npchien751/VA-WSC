# -*- coding: utf-8 -*-
"""
wellmining.py

Goal: Scrape through the wells that are under the purview of the GW study 
section for any interesting patterns.

Created on Fri Aug 10 07:56:08 2018

@author: nchien
"""

# To-Do
"""
- Add functionality that incorporates field verified values
- Need to clean up plot_rcnt() method and better format date axis
- Add method that finds closest precipitation gage and overlays that information
- Modify plot_rcnt to plot any record based on if it is given some trigger
- 
"""

# Import relevant packages
import numpy as np
import pandas as pd
import urllib.request
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class Well:
    """
    Well class used to pull well data from nwis site and format for analysis
    """
    def __init__(self, site_id):
        self.site_id = site_id
        
        # Pull recent (last 7 days) record using todays date
        t_now = dt.datetime.now()
        end_date = str(t_now.year) + '-' + str(t_now.month) + '-' + str(t_now.day)
        t_then = t_now - dt.timedelta(days=7)
        start_date = str(t_then.year) + '-' + str(t_then.month) + '-' + str(t_then.day)
        self.rcntRecord = self.pull_record(start_date, end_date)
    def __repr__(self):
        return 'Well: ' + self.site_id
    def pull_record(self, start_date, end_date):
        """
        Method to retrieve individual well site data from public nwis server.
        Example input
         - w48u13.pull_record(2018-08-01,2018-08-03)
         - start_date/end_date '2018-08-03'
        Example output
         - ('site_id', list of dates & times, list of water lvls)
        """
        # This URl only works for VA sites
        page = urllib.request.urlopen('https://nwis.waterdata.usgs.gov/va/nwis/uv/?cb_72019=on&format=rdb&site_no=' + 
                                      self.site_id + '&period=&begin_date=' + start_date + '&end_date=' + end_date)
        lines = page.readlines()
        lines = [line.decode('utf-8') for line in lines]
        lines = [line.rstrip('\n') for line in lines] 
        count = 0 
        dates = []
        lvls = []
        for line in lines:
            if line[0] == 'U':
                contents = line.split('\t')
                dates.append(contents[2])
                lvls.append(float(contents[4]))
                count += 1
        lvls = np.array(lvls)
        site_info = {'Dates':dates,'Levels':lvls}
        site_info = pd.DataFrame(data=site_info)
        return site_info
    def plot_rcnt(self):
        """
        Method to visualize the last seven days of this well record.
        Can expand this function to plot all kinds of records if want
        """

class Extens:
    """
    Extens class used to pull extensometer data from nwis site and format for 
    analysis
    """
    def __init__(self, site_id, start_date, end_date):
        # Pull site data from interwebs
        import urllib.request
        page = urllib.request.urlopen('https://waterdata.usgs.gov/va/nwis/dv?format=rdb&period=&begin_date=' + 
                                      start_date + '&end_date=' + end_date + 
                                      '&referred_module=sw&cb_50012=on&site_no=' + site_id)
        lines = page.readlines()
        lines = [line.decode('utf-8') for line in lines]
        lines = [line.rstrip('\n') for line in lines] 
        count = 0 
        dates = []
        cmpct = []
        for line in lines:
            if line[0] == 'U':
                contents = line.split('\t')
                date, lvl = contents[2], contents[3]
                dates.append(date)
                cmpct.append(lvl)
            count += 1
        # Set main init variables
        self.site_id = site_id
        self.PoR = dates
        self.cmpct = cmpct
    def __repr__(self):
        return 'Extensometer:' + self.site_id





