#Each row in the assignment datafile corresponds to a single observation.
#The following variables are provided to you:
#id : station identification code
#date : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
#element : indicator of element type
#TMAX : Maximum temperature (tenths of degrees C)
#TMIN : Minimum temperature (tenths of degrees C)
#value : data value for element (tenths of degrees C)
#For this assignment, you must:

#Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
#Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
#Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
#Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker as tck
import matplotlib.dates as mdates

df = pd.read_csv('fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
#Ordenemos el df por fecha en orden ascendente
df.sort_values(by=['Date'], inplace=True) # inplace: sobre escribe el df original
#Seleccionamos las fechas desde enero 2005 hasta diciembre 2014
from_date = (df['Date']>='2005-01-01')
up_to_date = (df['Date']<='2014-12-31')
selected_date = from_date & up_to_date
df = df[selected_date]
print(df.head())
df['Date'] = pd.to_datetime(df['Date'])
print(df.dtypes)

max_min_T_per_day = df.set_index('Date').groupby(level=0)['Data_Value'].agg({'MaxT': np.max, 'MinT': np.min})
max_min_T_per_day['year'] = max_min_T_per_day.index.year
max_min_T_per_day['month'] = max_min_T_per_day.index.month
max_min_T_per_day['day'] = max_min_T_per_day.index.day
max_min_T_per_day.head()

new_df = pd.DataFrame()

for m in range(1,13,1):
    if((m==1) or (m==3) or (m==5) or (m==7) or (m==8) or (m==10) or (m==12)):
        for d in range(1,32,1):
            maxt = max_min_T_per_day[(max_min_T_per_day['day'] == d)&(max_min_T_per_day['month'] == m)].max()[0]
            mint = max_min_T_per_day[(max_min_T_per_day['day'] == d)&(max_min_T_per_day['month'] == m)].min()[0]
            new_df = new_df.append({'date':pd.Timestamp('2005-'+str(m)+'-'+str(d)), 'Tmax': maxt/10, 'Tmin': mint/10}, ignore_index=True)
    if((m==4) or (m==6) or (m==9) or (m==11)):
        for d in range(1,31,1):
            maxt = max_min_T_per_day[(max_min_T_per_day['day'] == d)&(max_min_T_per_day['month'] == m)].max()[0]
            mint = max_min_T_per_day[(max_min_T_per_day['day'] == d)&(max_min_T_per_day['month'] == m)].min()[0]
            new_df = new_df.append({'date':pd.Timestamp('2005-'+str(m)+'-'+str(d)), 'Tmax': maxt/10, 'Tmin': mint/10}, ignore_index=True)
    if(m==2):
        for d in range(1,29,1):
            maxt = max_min_T_per_day[(max_min_T_per_day['day'] == d)&(max_min_T_per_day['month'] == m)].max()[0]
            mint = max_min_T_per_day[(max_min_T_per_day['day'] == d)&(max_min_T_per_day['month'] == m)].min()[0]
            new_df = new_df.append({'date':pd.Timestamp('2005-'+str(m)+'-'+str(d)), 'Tmax': maxt/10, 'Tmin': mint/10}, ignore_index=True)
new_df.head()


Tmax = new_df['Tmax']
Tmin = new_df['Tmin']
new_df['date'] = pd.to_datetime(new_df['date'])
date = new_df['date']
myFmt = mdates.DateFormatter('%b %d')

#Creamos el plot
fig,ax= plt.subplots(figsize=(10,8))
#plt.title('Maximun and Minimum Temperature', fontsize=20)
plt.xlabel('Date',fontsize=20)
plt.ylabel('Temperature [C]',fontsize=20)
ax.xaxis.set_major_locator(tck.MultipleLocator(base=30))
ax.xaxis.set_major_formatter(myFmt)
plt.xticks(rotation=45, ha='right')
plt.xlim(min(date),max(date))


plt.plot(date, Tmax, '-', color='r', label='Max Temperature')
plt.plot(date, Tmin, '-', color='b', label='Min Temperature')

plt.fill_between( range(len(Tmin)), Tmin, facecolor='black' )

plt.legend()

#plt.gcf().autofmt_xdate()
#plt.gca().fill_between(range(len(date)),Tmin, Tmax, facecolor='grey', alpha=0.5 )

plt.savefig('Assignment2.pdf')
