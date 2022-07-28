# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 18:16:39 2022

@author: NESAC
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pylab as pl
import matplotlib.gridspec as gridspec



##################### Reading the original file ########################################################
#ds = pd.read_csv("C:/ABHISHEK/E/Trivandrum_new/new/al17-181_core.csv",encoding= 'unicode_escape')
ds = pd.read_csv("C:/ABHISHEK/E/2022/TVM22_Modified_Program_core.csv",encoding= 'unicode_escape')
list(ds.keys())
################################### Convertin date and time  into  datetime formate ####################
ds['Date']=pd.to_datetime(ds['Date'])
ds['Time']=pd.to_datetime(ds['Time'])

#ds_months = ds.groupby("time.season")



def MonthToSeason(x):   
    global season
    if x == 6 or x == 7 or x == 8 :
         season = "Monsoon"
    elif x == 9 or x == 10 or x == 11:
         season = "Post-monsoon"
    elif x == 12 or x == 1 or x == 2:
         season = "Winter"
    elif x == 3 or x == 4 or x == 5:
         season = "Pre-monsoon"
    else:
         season = np.nan 
    return season

ds['Season'] = ds['Date'].dt.month.apply(lambda x : MonthToSeason(x))
GroupedData = ds.groupby(ds["Season"]).agg(['count','min','mean','max','std'])
    
win = ds.loc[ds['Season'] == 'Winter']
pm  = ds.loc[ds['Season'] == 'Pre-monsoon']
m   = ds.loc[ds['Season'] == 'Monsoon']
psm = ds.loc[ds['Season'] == 'Post-monsoon']


wx_co = win["CO(ppm)"]
wxnan_co = wx_co.dropna()
wl_co = len(wxnan_co)
pmx_co = pm["CO(ppm)"]
pmxnan_co = pmx_co.dropna()
pml_co = len(pmxnan_co)
mx_co = m["CO(ppm)"]
mxnan_co = mx_co.dropna()
ml_co = len(mxnan_co)
psmx_co = psm["CO(ppm)"]
psmxnan_co = psmx_co.dropna()
psml_co = len(psmxnan_co)
wx_co = win["CO(ppm)"]
wxnan_co = wx_co.dropna()
wl_co = len(wxnan_co)
pmx_co = pm["CO(ppm)"]
pmxnan_co = pmx_co.dropna()
pml_co = len(pmxnan_co)
mx_co = m["CO(ppm)"]
mxnan_co = mx_co.dropna()
ml_co = len(mxnan_co)
psmx_co = psm["CO(ppm)"]
psmxnan_co = psmx_co.dropna()
psml_co = len(psmxnan_co)


wx_o = win["Ozone(ppb)"]
wxnan_o = wx_o.dropna()
wl_o = len(wxnan_o)
pmx_o = pm["Ozone(ppb)"]
pmxnan_o = pmx_o.dropna()
pml_o = len(pmxnan_o)
mx_o = m["Ozone(ppb)"]
mxnan_o = mx_o.dropna()
ml_o = len(mxnan_o)
psmx_o = psm["Ozone(ppb)"]
psmxnan_o = psmx_o.dropna()
psml_o = len(psmxnan_o)
wx_o = win["Ozone(ppb)"]
wxnan_o = wx_o.dropna()
wl_o = len(wxnan_o)
pmx_o = pm["Ozone(ppb)"]
pmxnan_o = pmx_o.dropna()
pml_o = len(pmxnan_o)
mx_o = m["Ozone(ppb)"]
mxnan_o = mx_o.dropna()
ml_o = len(mxnan_o)
psmx_o = psm["Ozone(ppb)"]
psmxnan_o = psmx_o.dropna()
psml_o = len(psmxnan_o)

wx_no2 = win["NO2(ppb)"]
wxnan_no2 = wx_no2.dropna()
wl_no2 = len(wxnan_no2)
pmx_no2 = pm["NO2(ppb)"]
pmxnan_no2 = pmx_no2.dropna()
pml_no2 = len(pmxnan_no2)
mx_no2 = m["NO2(ppb)"]
mxnan_no2 = mx_no2.dropna()
ml_no2 = len(mxnan_no2)
psmx_no2 = psm["NO2(ppb)"]
psmxnan_no2 = psmx_no2.dropna()
psml_no2 = len(psmxnan_no2)
wx_no2 = win["NO2(ppb)"]
wxnan_no2 = wx_no2.dropna()
wl_no2 = len(wxnan_no2)
pmx_no2 = pm["NO2(ppb)"]
pmxnan_no2 = pmx_no2.dropna()
pml_no2 = len(pmxnan_no2)
mx_no2 = m["NO2(ppb)"]
mxnan_no2 = mx_no2.dropna()
ml_no2 = len(mxnan_no2)
psmx_no2 = psm["NO2(ppb)"]
psmxnan_no2 = psmx_no2.dropna()
psml_no2 = len(psmxnan_no2)

wx_so2 = win["SO2(ppb)"]
wxnan_so2 = wx_so2.dropna()
wl_so2 = len(wxnan_so2)
pmx_so2 = pm["SO2(ppb)"]
pmxnan_so2 = pmx_so2.dropna()
pml_so2 = len(pmxnan_so2)
mx_so2 = m["SO2(ppb)"]
mxnan_so2 = mx_so2.dropna()
ml_so2 = len(mxnan_so2)
psmx_so2 = psm["SO2(ppb)"]
psmxnan_so2 = psmx_so2.dropna()
psml_so2 = len(psmxnan_so2)
wx_so2 = win["SO2(ppb)"]
wxnan_so2 = wx_so2.dropna()
wl_so2 = len(wxnan_so2)
pmx_so2 = pm["SO2(ppb)"]
pmxnan_so2 = pmx_so2.dropna()
pml_so2 = len(pmxnan_so2)
mx_so2 = m["SO2(ppb)"]
mxnan_so2 = mx_so2.dropna()
ml_so2 = len(mxnan_so2)
psmx_so2 = psm["SO2(ppb)"]
psmxnan_so2 = psmx_so2.dropna()
psml_so2 = len(psmxnan_so2)

wx_pm2 = win["PM2.5(µg/m3)"]
wxnan_pm2 = wx_pm2.dropna()
wl_pm2 = len(wxnan_pm2)
pmx_pm2 = pm["PM2.5(µg/m3)"]
pmxnan_pm2 = pmx_pm2.dropna()
pml_pm2 = len(pmxnan_pm2)
mx_pm2 = m["PM2.5(µg/m3)"]
mxnan_pm2 = mx_pm2.dropna()
ml_pm2 = len(mxnan_pm2)
psmx_pm2 = psm["PM2.5(µg/m3)"]
psmxnan_pm2 = psmx_pm2.dropna()
psml_pm2 = len(psmxnan_pm2)
wx_pm2 = win["PM2.5(µg/m3)"]
wxnan_pm2 = wx_pm2.dropna()
wl_pm2 = len(wxnan_pm2)
pmx_pm2 = pm["PM2.5(µg/m3)"]
pmxnan_pm2 = pmx_pm2.dropna()
pml_pm2 = len(pmxnan_pm2)
mx_pm2 = m["PM2.5(µg/m3)"]
mxnan_pm2 = mx_pm2.dropna()
ml_pm2 = len(mxnan_pm2)
psmx_pm2 = psm["PM2.5(µg/m3)"]
psmxnan_pm2 = psmx_pm2.dropna()
psml_pm2 = len(psmxnan_pm2)

wx_pm10 = win["PM10(µg/m3)"]
wxnan_pm10 = wx_pm10.dropna()
wl_pm10 = len(wxnan_pm10)
pmx_pm10 = pm["PM10(µg/m3)"]
pmxnan_pm10 = pmx_pm10.dropna()
pml_pm10 = len(pmxnan_pm10)
mx_pm10 = m["PM10(µg/m3)"]
mxnan_pm10 = mx_pm10.dropna()
ml_pm10 = len(mxnan_pm10)
psmx_pm10 = psm["PM10(µg/m3)"]
psmxnan_pm10 = psmx_pm10.dropna()
psml_pm10 = len(psmxnan_pm10)
wx_pm10 = win["PM10(µg/m3)"]
wxnan_pm10 = wx_pm10.dropna()
wl_pm10 = len(wxnan_pm10)
pmx_pm10 = pm["PM10(µg/m3)"]
pmxnan_pm10 = pmx_pm10.dropna()
pml_pm10 = len(pmxnan_pm10)
mx_pm10 = m["PM10(µg/m3)"]
mxnan_pm10 = mx_pm10.dropna()
ml_pm10 = len(mxnan_pm10)
psmx_pm10 = psm["PM10(µg/m3)"]
psmxnan_pm10 = psmx_pm10.dropna()
psml_pm10 = len(psmxnan_pm10)

##################################################################

fig, [(ax0), (ax1), (ax2), (ax3),(ax4),(ax5)] = plt.subplots(nrows = 6,ncols = 1, figsize = (10,13),constrained_layout=True)     
x = plt.hist
ax0.hist(wxnan_co, 20, ec='red', fc='none', lw=1.5, histtype='step', label='Winter')
ax0.hist(pmxnan_co, 60, ec='green', fc='none', lw=1.5, histtype='step', label='Pre-monsoon')
ax0.hist(mxnan_co, 10, ec='blue', fc='none', lw=1.5, histtype='step', label='Monsoon')
ax0.hist(psmxnan_co, 10, ec='black', fc='none', lw=1.5, histtype='step', label='Post-Monsoon')
ax0.legend(loc='upper right')
ax0.set_yticks([0,1000,2000,3000,4000,5000,6000,7000,8000])
ax0.set_xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,18,20])
ax0.set_xlim([-0.5,5])
ax0.set_xlabel('CO(ppm)')
ax0.set_ylabel('Freequency of occurence',fontsize=10)
ax0.set_title('(a)')


ax1.hist(wxnan_o, 15, ec='red', fc='none', lw=1.5, histtype='step', label='Winter')
ax1.hist(pmxnan_o, 20, ec='green', fc='none', lw=1.5, histtype='step', label='Pre-monsoon')
ax1.hist(mxnan_o, 10, ec='blue', fc='none', lw=1.5, histtype='step', label='Monsoon')
ax1.hist(psmxnan_o, 10, ec='black', fc='none', lw=1.5, histtype='step', label='Post-Monsoon')
ax1.legend(loc='upper right')
ax1.set_yticks([0,1000,2000,3000,4000,5000])
ax1.set_xlim([-5,70])
ax1.set_xticks([0,10,20,30,40,50,60,70])
ax1.set_xlabel('Ozone(ppb)')
ax1.set_ylabel('Freequency of occurence',fontsize=10)
ax1.set_title('(b)')


ax2.hist(wxnan_so2, 70, ec='red', fc='none', lw=1.5, histtype='step', label='Winter')
ax2.hist(pmxnan_so2, 15, ec='green', fc='none', lw=1.5, histtype='step', label='Pre-monsoon')
ax2.hist(mxnan_so2, 50, ec='blue', fc='none', lw=1.5, histtype='step', label='Monsoon')
ax2.hist(psmxnan_so2, 40, ec='black', fc='none', lw=1.5, histtype='step', label='Post-Monsoon')
ax2.legend(loc='upper right')
ax2.set_yticks([0,500,1000,1500,2000,2500,3000])
ax2.set_xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,18,20])
ax2.set_xlim([-0.5,9])
ax2.set_xlabel('SO$_2$(ppb)')
ax2.set_ylabel('Freequency of occurence',fontsize=10)
ax2.set_title('(c)')


ax3.hist(wxnan_no2, 8, ec='red', fc='none', lw=1.5, histtype='step', label='Winter')
ax3.hist(pmxnan_no2, 40, ec='green', fc='none', lw=1.5, histtype='step', label='Pre-monsoon')
ax3.hist(mxnan_no2, 8, ec='blue', fc='none', lw=1.5, histtype='step', label='Monsoon')
ax3.hist(psmxnan_no2, 10, ec='black', fc='none', lw=1.5, histtype='step', label='Post-Monsoon')
ax3.legend(loc='upper right')
ax3.set_yticks([0,1000,2000,3000,4000,5000,6000,7000,8000])
ax3.set_xticks([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70])
ax3.set_xlim([-3,35])
ax3.set_xlabel('NO$_2$(ppb)')
ax3.set_ylabel('Freequency of occurence',fontsize=10)
ax3.set_title('(d)')


ax4.hist(wxnan_pm2, 20, ec='red', fc='none', lw=1.5, histtype='step', label='Winter')
ax4.hist(pmxnan_pm2, 30, ec='green', fc='none', lw=1.5, histtype='step', label='Pre-monsoon')
ax4.hist(mxnan_pm2, 10, ec='blue', fc='none', lw=1.5, histtype='step', label='Monsoon')
ax4.hist(psmxnan_pm2, 30, ec='black', fc='none', lw=1.5, histtype='step', label='Post-Monsoon')
ax4.legend(loc='upper right')
ax4.set_yticks([0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000])
ax4.set_xticks([0,10,20,30,40,50,60,70,80])
ax4.set_xlim([-3,125])
ax4.set_xlabel('PM2.5(ug/m3)')
ax4.set_ylabel('Freequency of occurence',fontsize=10)
ax4.set_title('(e)')

ax5.hist(wxnan_pm10, 20, ec='red', fc='none', lw=1.5, histtype='step', label='Winter')
ax5.hist(pmxnan_pm10, 30, ec='green', fc='none', lw=1.5, histtype='step', label='Pre-monsoon')
ax5.hist(mxnan_pm10, 20, ec='blue', fc='none', lw=1.5, histtype='step', label='Monsoon')
ax5.hist(psmxnan_pm10, 30, ec='black', fc='none', lw=1.5, histtype='step', label='Post-Monsoon')
ax5.legend(loc='upper right')
ax5.set_yticks([0,500,1000,1500,2000,2500])
ax5.set_xticks([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170])
ax5.set_xlim([-3,180])
ax5.set_xlabel('PM2.5(ug/m3)')
ax5.set_ylabel('Freequency of occurence',fontsize=10)
ax5.set_title('(e)')
fig.suptitle(' Trivandrum(8.5,76.9) \n 2016-2020',fontsize = 15)
plt.show()

fig.suptitle(' Trivandrum(8.5,76.9) \n 2016-2020',fontsize = 15)
plt.show()




#################################################################




fig, [(ax0), (ax1), (ax2), (ax3),(ax4),(ax5)] = plt.subplots(nrows = 6,ncols = 1, figsize = (10,18),constrained_layout=True)                                            
ax0.hist(wx_co, 10,histtype ='step',edgecolor = 'red')
ax0.hist(pmx_co, 10,histtype ='step',edgecolor = 'black')         
ax0.hist(mx_co, 10,histtype ='step',edgecolor = 'cyan')        
ax0.hist(psmx_co, 10,histtype ='step',edgecolor = 'green')  
ax0.set_yticks([((wl_co/100)*10),((wl_co/100)*20),((wl_co/100)*30),((wl_co/100)*40),
            ((wl_co/100)*50),((wl_co/100)*60),((wl_co/100)*70),((wl_co/100)*80),((wl_co/100)*90),((wl_co/100)*100)])
ylabelm =([10,20,30,40,50,60,70,80,90,100])
ax0.set_yticklabels(ylabelm,fontsize=10)

ax0.legend(['W','PM','M','PSM'],loc='upper right')
ax0.set_xlabel('CO(ppm)')
ax0.set_ylabel('Freequency of occurence(%)',fontsize=12)
ax0.set_title('(a)')
ax0.set_xlim(-0.25,5)


ax1.hist(wx_o, 10,histtype ='step',edgecolor = 'red')
ax1.hist(pmx_o, 10,histtype ='step',edgecolor = 'black')         
ax1.hist(mx_o, 10,histtype ='step',edgecolor = 'cyan')        
ax1.hist(psmx_o, 10,histtype ='step',edgecolor = 'green')  
ax1.set_yticks([((wl_o/100)*10),((wl_o/100)*20),((wl_o/100)*30),((wl_o/100)*40),
            ((wl_o/100)*50),((wl_o/100)*60),((wl_o/100)*70),((wl_o/100)*80),((wl_o/100)*90),((wl_o/100)*100)])
ylabelm =([10,20,30,40,50,60,70,80,90,100])
ax1.set_yticklabels(ylabelm,fontsize=10)
ax1.legend(['W','PM','M','PSM'],loc='upper right')
ax1.set_xlabel('Ozone(ppb)')
ax1.set_ylabel('Freequency of Occurence(%)',fontsize=12)
ax1.set_title('(b)')
ax1.set_xlim(-5,80)

ax2.hist(wx_no2, 15,histtype ='step',edgecolor = 'red')
ax2.hist(pmx_no2, 15,histtype ='step',edgecolor = 'black')         
ax2.hist(mx_no2, 15,histtype ='step',edgecolor = 'cyan')        
ax2.hist(psmx_no2, 15,histtype ='step',edgecolor = 'green')  
ax2.set_yticks([((wl_no2/100)*10),((wl_no2/100)*20),((wl_no2/100)*30),((wl_no2/100)*40),
            ((wl_no2/100)*50),((wl_no2/100)*60),((wl_no2/100)*70),((wl_no2/100)*80),((wl_no2/100)*90),((wl_no2/100)*100)])
ylabelm =([10,20,30,40,50,60,70,80,90,100])
ax2.set_yticklabels(ylabelm,fontsize=10)
ax2.legend(['W','PM','M','PSM'],loc='upper right')
ax2.set_xlabel('NO2(ppb)')
ax2.set_ylabel('Freequency of occurence(%)',fontsize=12)
ax2.set_xlim(-5,100)
ax2.set_title('(c)')
ax2.set_xlim(-2,30)

ax3.hist(wx_so2, 15,histtype ='step',edgecolor = 'red')
ax3.hist(pmx_so2, 15,histtype ='step',edgecolor = 'black')         
ax3.hist(mx_so2, 15,histtype ='step',edgecolor = 'cyan')        
ax3.hist(psmx_so2, 15,histtype ='step',edgecolor = 'green')  
ax3.set_yticks([((pml_so2/100)*10),((pml_so2/100)*20),((pml_so2/100)*30),((pml_so2/100)*40),
            ((pml_so2/100)*50),((pml_so2/100)*60),((pml_so2/100)*70),((pml_so2/100)*80),((pml_so2/100)*90),((pml_so2/100)*100)])


ylabelm =([10,20,30,40,50,60,70,80,90,100])
ax3.set_yticklabels(ylabelm,fontsize=10)
ax3.legend(['W','PM','M','PSM'],loc='upper right')
ax3.set_xlabel('SO2(ppb)')
ax3.set_ylabel('Freequency of occurence(%)',fontsize=12)
ax3.set_xlim(-1,20)
ax3.set_title('(d)')


ax4.hist(wx_pm2, 15,histtype ='step',edgecolor = 'red')
ax4.hist(pmx_pm2, 15,histtype ='step',edgecolor = 'black')         
ax4.hist(mx_pm2, 15,histtype ='step',edgecolor = 'cyan')        
ax4.hist(psmx_pm2, 15,histtype ='step',edgecolor = 'green')  
ax4.set_yticks([((pml_pm2/100)*10),((pml_pm2/100)*20),((pml_pm2/100)*30),((pml_pm2/100)*40),
            ((pml_pm2/100)*50),((pml_pm2/100)*60),((pml_pm2/100)*70),((pml_pm2/100)*80),((pml_pm2/100)*90),((pml_pm2/100)*100)])
#########

#########

#########

ylabelm =([10,20,30,40,50,60,70,80,90,100])
ax4.set_yticklabels(ylabelm,fontsize=10)
ax4.legend(['W','PM','M','PSM'],loc='upper right')
ax4.set_xlabel('PM2.5(µg/m3)')
ax4.set_ylabel('Freequency of occurence(%)',fontsize=12)
ax4.set_xlim(-10,200)

ax4.set_title('(e)')


ax5.hist(wx_pm10, 15,histtype ='step',edgecolor = 'red')
ax5.hist(pmx_pm10, 15,histtype ='step',edgecolor = 'black')         
ax5.hist(mx_pm10, 15,histtype ='step',edgecolor = 'cyan')        
ax5.hist(psmx_pm10, 15,histtype ='step',edgecolor = 'green')  
ax5.set_yticks([((pml_pm10/100)*10),((pml_pm10/100)*20),((pml_pm10/100)*30),((pml_pm10/100)*40),
            ((pml_pm10/100)*50),((pml_pm10/100)*60),((pml_pm10/100)*70),((pml_pm10/100)*80),((pml_pm10/100)*90),((pml_pm10/100)*100)])


ylabelm =([10,20,30,40,50,60,70,80,90,100])
ax5.set_yticklabels(ylabelm,fontsize=10)
ax5.legend(['W','PM','M','PSM'],loc='upper right')
ax5.set_xlabel('PM10(µg/m3)')
ax5.set_ylabel('Freequency of occurence(%)',fontsize=12)
ax5.set_xlim(-10,200)

ax5.set_title('(f)')



fig.suptitle(' Trivandrum(8.5,76.9) \n 2016-2020',fontsize = 15)




####################################### Boxplot ##########################
############### change >> column = "" for individual variables #############

fig, [(ax0),(ax1),(ax2),(ax3),(ax4),(ax5)] = plt.subplots(nrows = 6,ncols = 1, figsize = (10,18),constrained_layout=True)   
     
bplot = ds.boxplot(ax=ax0,by = 'Season',column='CO(ppm)' ,positions=[3,4,2,1],showfliers = False,return_type='dict', figsize=(8,6), grid=True, patch_artist=True, 
                     sym='d', fontsize=16)

colors = ['cyan', 'cyan', 'cyan', 'cyan']
for patch, color in zip(bplot['CO(ppm)']['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('0.2')
    patch.set_linewidth(1.5)
for whisker in bplot['CO(ppm)']['whiskers']:
    whisker.set_color('0.2')
    whisker.set_linewidth(1.5)
for fliers in bplot['CO(ppm)']['fliers']:
    fliers.set_markerfacecolor('0.2')
for median in bplot['CO(ppm)']['medians']:
    median.set_color('0.2')
    median.set_linewidth(1.5)
for caps in bplot['CO(ppm)']['caps']:
    caps.set_color('0.2')
    caps.set_linewidth(1.5)
    
#plt.suptitle("",fontsize = 18)
ax0.set_xlabel("", fontsize=18)
ax0.set_ylabel("CO(ppm)", fontsize=18)
ax0.set_title('(a)',fontsize=18)
#plt.title("Chennai(13.0,80.2)  \n (e)",fontsize = 18)


bplot = ds.boxplot(ax=ax1,by = 'Season',column='Ozone(ppb)' ,positions=[3,4,2,1],showfliers = False,return_type='dict', figsize=(18,26), grid=True, patch_artist=True, 
                     sym='d', fontsize=16)

colors = ['cyan', 'cyan', 'cyan', 'cyan']
for patch, color in zip(bplot['Ozone(ppb)']['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('0.2')
    patch.set_linewidth(1.5)
for whisker in bplot['Ozone(ppb)']['whiskers']:
    whisker.set_color('0.2')
    whisker.set_linewidth(1.5)
for fliers in bplot['Ozone(ppb)']['fliers']:
    fliers.set_markerfacecolor('0.2')
for median in bplot['Ozone(ppb)']['medians']:
    median.set_color('0.2')
    median.set_linewidth(1.5)
for caps in bplot['Ozone(ppb)']['caps']:
    caps.set_color('0.2')
    caps.set_linewidth(1.5)


#plt.title("Chennai(13.0,80.2)  \n (e)",fontsize = 18)
#plt.suptitle("",fontsize = 18)
ax1.set_xlabel("", fontsize=18)
ax1.set_ylabel("Ozone(ppb)", fontsize=18)
ax1.set_title('(b)',fontsize=18)



bplot = ds.boxplot(ax=ax2,by = 'Season',column='SO2(ppb)' ,positions=[3,4,2,1],showfliers = False,return_type='dict', figsize=(8,6), grid=True, patch_artist=True, 
                     sym='d', fontsize=16)

colors = ['cyan', 'cyan', 'cyan', 'cyan']
for patch, color in zip(bplot['SO2(ppb)']['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('0.2')
    patch.set_linewidth(1.5)
for whisker in bplot['SO2(ppb)']['whiskers']:
    whisker.set_color('0.2')
    whisker.set_linewidth(1.5)
for fliers in bplot['SO2(ppb)']['fliers']:
    fliers.set_markerfacecolor('0.2')
for median in bplot['SO2(ppb)']['medians']:
    median.set_color('0.2')
    median.set_linewidth(1.5)
for caps in bplot['SO2(ppb)']['caps']:
    caps.set_color('0.2')
    caps.set_linewidth(1.5)


#plt.title("Chennai(13.0,80.2)  \n (e)",fontsize = 18)
#plt.suptitle("",fontsize = 18)
ax2.set_xlabel("", fontsize=18)
ax2.set_ylabel("SO$_2$(ppb)", fontsize=18)
ax2.set_title('(c)',fontsize=18)


bplot = ds.boxplot(ax=ax3,by = 'Season',column='NO2(ppb)' ,positions=[3,4,2,1],showfliers = False,return_type='dict', figsize=(8,6), grid=True, patch_artist=True, 
                     sym='d', fontsize=16)

colors = ['cyan', 'cyan', 'cyan', 'cyan']
for patch, color in zip(bplot['NO2(ppb)']['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('0.2')
    patch.set_linewidth(1.5)
for whisker in bplot['NO2(ppb)']['whiskers']:
    whisker.set_color('0.2')
    whisker.set_linewidth(1.5)
for fliers in bplot['NO2(ppb)']['fliers']:
    fliers.set_markerfacecolor('0.2')
for median in bplot['NO2(ppb)']['medians']:
    median.set_color('0.2')
    median.set_linewidth(1.5)
for caps in bplot['NO2(ppb)']['caps']:
    caps.set_color('0.2')
    caps.set_linewidth(1.5)


#plt.title("Chennai(13.0,80.2)  \n (e)",fontsize = 18)
plt.suptitle("",fontsize = 18)
ax3.set_xlabel("", fontsize=18)
ax3.set_ylabel("NO$_2$(ppb)", fontsize=18)
ax3.set_title('(d)',fontsize=18)

bplot = ds.boxplot(ax=ax4,by = 'Season',column='PM2.5(µg/m3)' ,positions=[3,4,2,1],showfliers = False,return_type='dict', figsize=(8,6), grid=True, patch_artist=True, 
                     sym='d', fontsize=16)

colors = ['cyan', 'cyan', 'cyan', 'cyan']
for patch, color in zip(bplot['PM2.5(µg/m3)']['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('0.2')
    patch.set_linewidth(1.5)
for whisker in bplot['PM2.5(µg/m3)']['whiskers']:
    whisker.set_color('0.2')
    whisker.set_linewidth(1.5)
for fliers in bplot['PM2.5(µg/m3)']['fliers']:
    fliers.set_markerfacecolor('0.2')
for median in bplot['PM2.5(µg/m3)']['medians']:
    median.set_color('0.2')
    median.set_linewidth(1.5)
for caps in bplot['PM2.5(µg/m3)']['caps']:
    caps.set_color('0.2')
    caps.set_linewidth(1.5)


#plt.title("Chennai(13.0,80.2)  \n (e)",fontsize = 18)
#plt.suptitle("",fontsize = 18)
ax4.set_xlabel("", fontsize=18)
ax4.set_ylabel("PM2.5 ($\mu$g/m$^3$)", fontsize=18)
ax4.set_title('(e)',fontsize=18)
#fig.suptitle(' Chennai(13.0,80.2) \n',fontsize = 20)

bplot = ds.boxplot(ax=ax5,by = 'Season',column='PM10(µg/m3)' ,positions=[3,4,2,1],showfliers = False,return_type='dict', figsize=(8,6), grid=True, patch_artist=True, 
                     sym='d', fontsize=16)

colors = ['cyan', 'cyan', 'cyan', 'cyan']
for patch, color in zip(bplot['PM10(µg/m3)']['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('0.2')
    patch.set_linewidth(1.5)
for whisker in bplot['PM10(µg/m3)']['whiskers']:
    whisker.set_color('0.2')
    whisker.set_linewidth(1.5)
for fliers in bplot['PM10(µg/m3)']['fliers']:
    fliers.set_markerfacecolor('0.2')
for median in bplot['PM10(µg/m3)']['medians']:
    median.set_color('0.2')
    median.set_linewidth(1.5)
for caps in bplot['PM10(µg/m3)']['caps']:
    caps.set_color('0.2')
    caps.set_linewidth(1.5)


#plt.title("Chennai(13.0,80.2)  \n (e)",fontsize = 18)
plt.suptitle("",fontsize = 18)
ax5.set_xlabel("", fontsize=18)
ax5.set_ylabel("PM10 ($\mu$g/m$^3$)", fontsize=18)
ax5.set_title('(f)',fontsize=18)
fig.suptitle(' Trivandrum(8.5,76.9) \n 2016-2020',fontsize = 20)





