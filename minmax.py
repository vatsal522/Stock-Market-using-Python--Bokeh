from pandas_datareader import *
from pandas_datareader import data
import numpy as np
import datetime
from datetime import timedelta
import pandas
from pandas import *
from bokeh.plotting import figure,show,output_file
list1=[]
start=datetime.datetime(2015,11,2)
end=datetime.datetime(2020,5,11)
"""
delta = start - end
print(delta.days)
abc=delta.days%5
if abc==0:
    print('sdsadsa')
else:
    start =start - timedelta(abc)
"""
df=data.DataReader(name="AAPL",data_source="yahoo",start=start,end=end)

maxweek=[]
minweek=[None]
week_open=0
week_close=0
weekopen=[]
weekclose=[]
a=0
u=0
max_week=0
"""
y=len(df.High)
filterrows=y%5
tuu=0
#SORTING HIGH AND LOW ON WEEKLY BASIS
for x in df.High:
    
    if x>=max_week:
        max_week=x
        #a=1
        
   
    u+=1   
    if u%5==0:
        maxweek.append(max_week)
        max_week=0


    
    tuu+=1
    if tuu>(y-filterrows):
        break
        
    
print(len(maxweek))    
    #if u==len(df.index):
        #break
        
#print(len(maxweek))
#print(maxweek)
"""
df.to_csv('AAPL12.csv')
print('_______________________________________________________')


c=0
xyzz=len(df.index)
#print(xyzz)
frowfordate=xyzz%5
tuub=0
list1=[]
for xx in df.index:
    tuub+=1

    if tuub>(xyzz-frowfordate):
        break

    if c%5==0:
        list1.append(xx)
    c+=1



print(list1)
print(len(list1))
