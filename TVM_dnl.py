# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 21:48:20 2022

@author: NESAC
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


ds =pd.read_csv("C:/ABHISHEK/E/2022/TVM22_Modified_Program_core.csv",encoding= 'unicode_escape')
#ds =pd.read_csv("C:/ABHISHEK/E/2022/Bhubaneshwar/BHB_SO2_Hourly.csv",encoding= 'unicode_escape')
#C:/ABHISHEK/E/2022/Bhubaneshwar/BHB_SO2_Hourly.csv
list(ds.keys())
# reshaping the dataframe using pivot
#a = ds.pivot(index="Date",columns="Time")

############################################################################################################################################################
############################################################################################################################################################
########################  NOTE CHANGE THE YEARS IN DATE IN YOR CSV FILE TO ONE YEAR FOR GETTING SEASONAL PLOTS #############################################
############################################################################################################################################################
############################################################################################################################################################
#pivot table
ds['Date']=pd.to_datetime(ds['Date'])
ds['Time']=pd.to_datetime(ds['Time'])
da = ds.pivot_table(index="Time",columns="Date",aggfunc="mean")
ds['Date']=pd.to_datetime(ds['Date'])
ds['Time']=pd.to_datetime(ds['Time'])
db = ds.pivot_table(index= pd.Grouper(freq='M',key='Date'),columns='Time',values='PM10(µg/m3)')




Ms =['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov']
db['Mss']= Ms
db.reset_index(level=0, inplace=True)
db.set_index(["Date","Mss"],inplace = True)

#dbs = db.groupby(['Mss','Date']).mean()
dbm = db.pivot_table(index= ["Mss"],aggfunc="mean")
dbm['Marker']=['4','8','92','2','1','7','6','3','5','91','90','9']
dbm = dbm.sort_values(by=['Marker'], ascending=True)
dbm.set_index(["Marker"],inplace = True)
npdb = np.array(dbm)
dfs = pd.DataFrame(npdb)



# ylab = [1,3,5,7,9,11]
# fig, ax= plt.subplots(1,1, figsize= (7,3))
# plt.contourf(dfs, cmap='OrRd')
# plt.colorbar(label="Ozone(ug/m3)", orientation="vertical")
# plt.xlabel('Hours', fontsize=13)
# plt.ylabel('Months', fontsize=13)
# plt.title('Diurnal and Seasonal \n Variation of surafacce level CO (2016-2018)')
# plt.xticks(xlab)
# plt.yticks(ylab)

xlabelm = ["00:00","00:01","00:02","00:03","00:04","00:05","00:06","00:07","00:08","00:09","00:10","00:11","00:12","00:13","00:14","00:15","00:16","00:17","00:18","00:19","00:20","00:21","00:22","00:23"]
ylabelm = ["Jan","Feb","Mar","Apr","May", "Jun","Jul","Aug", "Sep", "Oct", "Nov", "Dec"]
xlab = [0,2,4,6,8,10,12,14,16,18,20,22]
ylab = [0,1,2,3,4,5,6,7,8,9,10,11]
fig, ax= plt.subplots(1,1, figsize= (7,4))
plt.contourf(dfs, cmap='OrRd')
plt.xticks(xlab)
plt.yticks(ylab)
#ax.set_xticklabels(xlabelm)
ax.set_yticklabels(ylabelm,fontsize=10)
plt.colorbar(label="PM10 (µg/m3)", orientation="vertical")
plt.title('Diurnal and Seasonal \n Variation of surafacce level PM10 (2016-2020)')
plt.xlabel('Hours', fontsize=13)
plt.ylabel('Months', fontsize=13)