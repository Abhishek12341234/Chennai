# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 15:06:47 2022

@author: NESAC
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np





##################### Reading the original file ########################################################
#ds = pd.read_csv("C:/ABHISHEK/E/Trivandrum_new/new/al17-181_core.csv",encoding= 'unicode_escape')
ds = pd.read_csv("C:/ABHISHEK/E/2022/TVM22_Modified_Program_core.csv",encoding= 'unicode_escape')
list(ds.keys())

################################### Convertin date and time  into  datetime formate ####################
ds['Date']=pd.to_datetime(ds['Date'])
ds['Time']=pd.to_datetime(ds['Time'])
################################### Reshaping the dataframe using pivot table ###########################
################################### such that each date as columns and time as rows #####################
table = pd.pivot_table(ds, index =['Date', 'Time'])
tab1 = pd.pivot_table(table,index=['Time'],columns=['Date'])
tab1.to_csv("C:/ABHISHEK/E/Trivandrum_new/new/piot2020.csv")
#################################### Now after taking out the percentage mean deviation  ################
#################################### make the cs file in same order as previous csv file generated  by pivot table ###########
#################################### read the file>transpose it #######################################################
pvt =  pd.read_csv("C:/ABHISHEK/E/Trivandrum_new/new/piot2020_pdf.csv",encoding= 'unicode_escape')
pvt_t = pvt.T

#################################### save the transpose file and deleate the index header################################
#################################### such that it Datetime can be the new index> then read the file ####################################
pvt_t.to_csv("C:/ABHISHEK/E/Trivandrum_new/new/pivot_t.csv")
pvt_1 =  pd.read_csv("C:/ABHISHEK/E/Trivandrum_new/new/pivot_t_cr1.csv",encoding= 'unicode_escape')

####################################### Group the file  with monthly mean ##############################
#a = pvt.pivot(index="Date",columns="Time")
pvt_1['Date']=pd.to_datetime(pvt_1['Date'])
pvt_1['Time']=pd.to_datetime(ds['Time'])
pvdm = pvt_1.pivot_table(index= ['Variables',pd.Grouper(freq='M',key='Date')])

###################################### Insert a new column of season to group by season ####################
season=['W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W',
        'W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W',
        'W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W',
        'W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W',
        'W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W','W','W','PM','PM','PM','M','M','M','PSM','PSM','PSM','W']
pvdm['Seasons']= season


##################################### Now group by season> with aggfunc mean and standard deviation #################################################
pvsm = pvdm.pivot_table(index= ['Variables',pd.Grouper(key='Seasons')],aggfunc='mean')
pvssd = pvdm.pivot_table(index= ['Variables',pd.Grouper(key='Seasons')],aggfunc='std')
pvsmt = pvsm.T
pvssdt = pvssd.T

######################################## Storing the Variables ##############################
list(pvsmt.keys())
mxco_w = pvsmt['CO(ppm)']['W']
mxco_pm = pvsmt['CO(ppm)']['PM']
mxco_m = pvsmt['CO(ppm)']['M']
mxco_psm = pvsmt['CO(ppm)']['PSM']

sxco_w = pvssdt['CO(ppm)']['W']
sxco_pm = pvssdt['CO(ppm)']['PM']
sxco_m = pvssdt['CO(ppm)']['M']
sxco_psm = pvssdt['CO(ppm)']['PSM']


mxo_w = pvsmt['Ozone(ppb)']['W']
mxo_pm = pvsmt['Ozone(ppb)']['PM']
mxo_m = pvsmt['Ozone(ppb)']['M']
mxo_psm = pvsmt['Ozone(ppb)']['PSM']

sxo_w = pvssdt['Ozone(ppb)']['W']
sxo_pm = pvssdt['Ozone(ppb)']['PM']
sxo_m = pvssdt['Ozone(ppb)']['M']
sxo_psm = pvssdt['Ozone(ppb)']['PSM']

mxno2_w = pvsmt['NO2(ppb)']['W']
mxno2_pm = pvsmt['NO2(ppb)']['PM']
mxno2_m = pvsmt['NO2(ppb)']['M']
mxno2_psm = pvsmt['NO2(ppb)']['PSM']

sxno2_w = pvssdt['NO2(ppb)']['W']
sxno2_pm = pvssdt['NO2(ppb)']['PM']
sxno2_m = pvssdt['NO2(ppb)']['M']
sxno2_psm = pvssdt['NO2(ppb)']['PSM']

mxso2_w = pvsmt['SO2(ppb)']['W']
mxso2_pm = pvsmt['SO2(ppb)']['PM']
mxso2_m = pvsmt['SO2(ppb)']['M']
mxso2_psm = pvsmt['SO2(ppb)']['PSM']

sxso2_w = pvssdt['SO2(ppb)']['W']
sxso2_pm = pvssdt['SO2(ppb)']['PM']
sxso2_m = pvssdt['SO2(ppb)']['M']
sxso2_psm = pvssdt['SO2(ppb)']['PSM']

mxpm25_w = pvsmt['PM2.5(µg/m3)']['W']
mxpm25_pm = pvsmt['PM2.5(µg/m3)']['PM']
mxpm25_m = pvsmt['PM2.5(µg/m3)']['M']
mxpm25_psm = pvsmt['PM2.5(µg/m3)']['PSM']

sxpm25_w = pvssdt['PM2.5(µg/m3)']['W']
sxpm25_pm = pvssdt['PM2.5(µg/m3)']['PM']
sxpm25_m = pvssdt['PM2.5(µg/m3)']['M']
sxpm25_psm = pvssdt['PM2.5(µg/m3)']['PSM']

mxpm10_w = pvsmt['PM10(µg/m3)']['W']
mxpm10_pm = pvsmt['PM10(µg/m3)']['PM']
mxpm10_m = pvsmt['PM10(µg/m3)']['M']
mxpm10_psm = pvsmt['PM10(µg/m3)']['PSM']

sxpm10_w = pvssdt['PM10(µg/m3)']['W']
sxpm10_pm = pvssdt['PM10(µg/m3)']['PM']
sxpm10_m = pvssdt['PM10(µg/m3)']['M']
sxpm10_psm = pvssdt['PM10(µg/m3)']['PSM']

##################################### Figure ##############################################

time = ['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00',
        '14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00']
tm = ['00:00','','02:00','','04:00','','06:00','','08:00','','10:00','','12:00','',
        '14:00','','16:00','','18:00','','20:00','','22:00','','24:00']
fig, ax = plt.subplots(6,1,figsize=(12,18),constrained_layout=True)

ax[0].errorbar(x = time, y=mxco_w,yerr=sxco_w,marker='s', mfc='black',ms=5, capsize=2,linestyle = '-',color='black',label='Winter')
ax[0].errorbar(x = time, y=mxco_pm,yerr=sxco_pm,marker='o', mfc='blue',ms=5, capsize=2,linestyle = '-',color='blue',label='Pre-Monsoon')
ax[0].errorbar(x = time, y=mxco_m,yerr=sxco_m,marker='x', mfc='red',ms=5, capsize=2,linestyle = '-',color='red',label='Monsoon')
ax[0].errorbar(x = time, y=mxco_psm,yerr=sxco_psm,marker='o', mfc='green',ms=5, capsize=2,linestyle = '-',color='green',label='Post-Monsoon')
x_coordinates = [-1, 24]
y_coordinates = [0, 0]
ax[0].plot(x_coordinates, y_coordinates,label='_nolegend_')
ax[0].set_xticklabels(tm,fontsize=12,rotation= 45)
ax[0].set_xlim(0, 24)
ax[0].set_ylim(-0.4, 0.4)
ax[0].grid(True)
ax[0].set_ylabel('Percentage Deviation(%)',fontsize=13)
ax[0].legend(loc='upper left')
ax[0].title.set_text(' (a)\n CO')
ax[0].set_xticklabels([])



ax[1].errorbar(x = time, y=mxo_w,yerr=sxo_w,marker='s', mfc='black',ms=5, capsize=2,linestyle = '-',color='black',label='Winter')
ax[1].errorbar(x = time, y=mxo_pm,yerr=sxo_pm,marker='o', mfc='blue',ms=5, capsize=2,linestyle = '-',color='blue',label='Pre-Monsoon')
ax[1].errorbar(x = time, y=mxo_m,yerr=sxo_m,marker='x', mfc='red',ms=5, capsize=2,linestyle = '-',color='red',label='Monsoon')
ax[1].errorbar(x = time, y=mxo_psm,yerr=sxo_psm,marker='v', mfc='green',ms=5, capsize=2,linestyle = '-',color='green',label='Post-Monsoon')
x_coordinates = [-1, 24]
y_coordinates = [0, 0]
ax[1].plot(x_coordinates, y_coordinates,label='_nolegend_')
ax[1].set_xticklabels(tm,fontsize=12,rotation= 45)
ax[1].set_xlim(0, 24)
ax[1].set_ylim(-0.5, 0.5)
ax[1].grid(True)
ax[1].set_ylabel('Percentage Deviation(%)',fontsize=13)
ax[1].legend(loc='upper left')
ax[1].title.set_text(' (b)\n Ozone')
ax[1].set_xticklabels([])
ax[2].errorbar(x = time, y=mxno2_w,yerr=sxno2_w,marker='s', mfc='black',ms=5, capsize=2,linestyle = '-',color='black',label='Winter')
ax[2].errorbar(x = time, y=mxno2_pm,yerr=sxno2_pm,marker='o', mfc='blue',ms=5, capsize=2,linestyle = '-',color='blue',label='Pre-Monsoon')
ax[2].errorbar(x = time, y=mxno2_m,yerr=sxno2_m,marker='x', mfc='red',ms=5, capsize=2,linestyle = '-',color='red',label='Monsoon')
ax[2].errorbar(x = time, y=mxno2_psm,yerr=sxno2_psm,marker='v', mfc='green',ms=5, capsize=2,linestyle = '-',color='green',label='Post-Monsoon')
x_coordinates = [-1, 24]
y_coordinates = [0, 0]
ax[2].plot(x_coordinates, y_coordinates,label='_nolegend_')
ax[2].set_xticklabels(tm,fontsize=12,rotation= 45)
ax[2].set_xlim(0, 24)
ax[2].set_ylim(-1.2, 1.2)
ax[2].grid(True)
ax[2].set_ylabel('Percentage Deviation(%)',fontsize=13)
ax[2].legend(loc='upper left')
ax[2].title.set_text(' (c)\n NO2')
ax[2].set_xticklabels([])
ax[3].errorbar(x = time, y=mxso2_w,yerr=sxso2_w,marker='s', mfc='black',ms=5, capsize=2,linestyle = '-',color='black',label='Winter')
ax[3].errorbar(x = time, y=mxso2_pm,yerr=sxso2_pm,marker='o', mfc='blue',ms=5, capsize=2,linestyle = '-',color='blue',label='Pre-Monsoon')
ax[3].errorbar(x = time, y=mxso2_m,yerr=sxso2_m,marker='x', mfc='red',ms=5, capsize=2,linestyle = '-',color='red',label='Monsoon')
ax[3].errorbar(x = time, y=mxso2_psm,yerr=sxso2_psm,marker='v', mfc='green',ms=5, capsize=2,linestyle = '-',color='green',label='Post-Monsoon')
x_coordinates = [-1, 24]
y_coordinates = [0, 0]
ax[3].plot(x_coordinates, y_coordinates,label='_nolegend_')
ax[3].set_xticklabels(tm,fontsize=12,rotation= 45)
ax[3].set_xlim(0, 24)
ax[3].set_ylim(-0.5, 0.5)
ax[3].grid(True)
ax[3].set_ylabel('Percentage Deviation(%)',fontsize=13)

ax[3].legend(loc='upper left')
ax[3].title.set_text(' (d)\n SO2')
ax[3].set_xticklabels([])

ax[4].errorbar(x = time, y=mxpm25_w,yerr=sxpm25_w,marker='s', mfc='black',ms=5, capsize=2,linestyle = '-',color='black',label='Winter')
ax[4].errorbar(x = time, y=mxpm25_pm,yerr=sxpm25_pm,marker='o', mfc='blue',ms=5, capsize=2,linestyle = '-',color='blue',label='Pre-Monsoon')
ax[4].errorbar(x = time, y=mxpm25_m,yerr=sxpm25_m,marker='x', mfc='red',ms=5, capsize=2,linestyle = '-',color='red',label='Monsoon')
ax[4].errorbar(x = time, y=mxpm25_psm,yerr=sxpm25_psm,marker='o', mfc='green',ms=5, capsize=2,linestyle = '-',color='green',label='Post-Monsoon')
x_coordinates = [-1, 24]
y_coordinates = [0, 0]
ax[4].plot(x_coordinates, y_coordinates,label='_nolegend_')
ax[4].set_xticklabels(tm,fontsize=12,rotation= 45)
ax[4].set_xlim(0, 24)
ax[4].set_ylim(-0.5, 0.5)
ax[4].grid(True)
ax[4].set_ylabel('Percentage Deviation(%)',fontsize=13)
ax[4].legend(loc='upper left')
ax[4].title.set_text(' (e)\n PM2.5')
ax[4].set_xticklabels([])

ax[5].errorbar(x = time, y=mxpm10_w,yerr=sxpm10_w,marker='s', mfc='black',ms=5, capsize=2,linestyle = '-',color='black',label='Winter')
ax[5].errorbar(x = time, y=mxpm10_pm,yerr=sxpm10_pm,marker='o', mfc='blue',ms=5, capsize=2,linestyle = '-',color='blue',label='Pre-Monsoon')
ax[5].errorbar(x = time, y=mxpm10_m,yerr=sxpm10_m,marker='x', mfc='red',ms=5, capsize=2,linestyle = '-',color='red',label='Monsoon')
ax[5].errorbar(x = time, y=mxpm10_psm,yerr=sxpm10_psm,marker='o', mfc='green',ms=5, capsize=2,linestyle = '-',color='green',label='Post-Monsoon')
x_coordinates = [-1, 24]
y_coordinates = [0, 0]
ax[5].plot(x_coordinates, y_coordinates,label='_nolegend_')
ax[5].set_xticklabels(tm,fontsize=12,rotation= 45)
ax[5].set_xlim(0, 24)
ax[5].set_ylim(-0.5, 0.5)
ax[5].grid(True)
ax[5].set_ylabel('Percentage Deviation(%)',fontsize=13)
ax[5].legend(loc='upper left')
ax[5].title.set_text(' (f)\n PM10')
ax[5].set_xlabel('Local Time (Hrs)',fontsize=13)#ax[5].set_xticklabels([])





fig.suptitle('Trivandrum(8.5,76.9) \n',fontsize = 15)






# pvt['Time']=pd.to_datetime(pvt['Time'])
# tab2 = pd.pivot_table(pvt,index=['Time'],columns=['Date'])





# #pivot table
# ds['Date']=pd.to_datetime(ds['Date'])
# ds['Time']=pd.to_datetime(ds['Time'])
# da = ds.pivot_table(index="Time",columns="Date",values="CO\n(mg/m?",aggfunc="mean")

# ds['Date']=pd.to_datetime(ds['Date'])
# ds['Time']=pd.to_datetime(ds['Time'])
# db = ds.pivot_table(index= pd.Grouper(freq='M',key='Date'),columns='Time',values='PM10\n(µg/m?)',aggfunc="mean")
# npdb = np.array(db)
# #npdb = npdb.transpose()
# dfs = pd.DataFrame(npdb)


# xlab = [0,2,4,6,8,10,12,14,16,18,20,22]
# ylab = [0,1,2,3,4,5,6,7,8,9,10,11]
# fig, ax= plt.subplots(1,1, figsize= (8,5))
# plt.contourf(dfs, cmap='OrRd')
# plt.colorbar(label="$PM10(""\u03bc/m^3)""$", orientation="vertical")
# plt.xlabel('Hours', fontsize=13)
# plt.ylabel('Months', fontsize=13)
# plt.title('Trivandrum \n Diurnal and Seasonal Variation of surafacce level\n $PM10$ (2016-2018)')
# plt.xticks(xlab)
# plt.yticks(ylab)
# ax.set_yticklabels(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
  

# s = ds['Ozone(ppb)']
# n = 24
# mean = s.rolling(n, closed='right').mean()
# ds['Change1'] = (s - mean) / mean

