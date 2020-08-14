#$#$$#$#$#$#$#$#$#$#$#$
#df is dataframe jaha se import kiya
#new is dataframe that is without header
#new1 is the final dataframe to be displayed at the final
from pandas_datareader import *
from pandas_datareader import data
import numpy as np
import datetime
import pandas
from pandas import *
from bokeh.plotting import figure,show,output_file
list1=[]
start=datetime.datetime(2015,11,2)
end=datetime.datetime(2020,5,11)

df=data.DataReader(name="AAPL",data_source="yahoo",start=start,end=end)

new = df[['High','Low','Open','Close']]

#TRIAL SPACE
new
max_week=0
i=0
j=i+4
u=0
maxweek=[]
minweek=[None]
week_open=0
week_close=0
weekopen=[]
weekclose=[]
a=0
u=0
#SORTING DATES ON WEEKLY BASIS
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
########################################3
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
        
    
    

    
lowweek=[]
lowest=99999
lendf=len(df.High)
filtering=lendf%5
tuup=0
u=0
#SORTING HIGH AND LOW ON WEEKLY BASIS
for x in df.Low:
    
    if x<=lowest:
        lowest=x
        
        
   
    u+=1   
    if u%5==0:
        lowweek.append(lowest)
        lowest=99999


    
    tuup+=1
    if tuup>(lendf-filtering):
        break


print(lowweek)
print(len(lowweek))
    

        
new=pandas.DataFrame()
df.to_csv('withoutheader.csv',header=None)
new=pandas.read_csv('withoutheader.csv')
c=0
counter=0
xyz=len(df.Open)
frowforopen=xyz%5
for x in df.Open:
    counter+=1
    if counter>(xyz-frowforopen):
        break
    if c%5==0:
        weekopen.append(x)
    c+=1
    

"""     
count=0   
while True:
    week_open=df.Open[count]
    week_close=df.Close[count+4]
    count+=4
    weekopen.append(week_open)
    weekclose.append(week_close)
    
    if count==len(df.index)-2:
        break
"""  
df.to_csv('AAPL12.csv')
print(len(maxweek))
print(maxweek)

#print(len(minweek))     
#print(minweek)

counterr=0
weekclose=[]
xxyy=len(df.Close)
frowforclose=xxyy%5
rownum=0
for x in df.Close:
    rownum+=1
    counterr+=1
    
    if counterr>(xxyy-frowforclose):
        break
    
    if rownum%5==0:
        weekclose.append(x)  


print('_______________________________________________________')
print(len(weekopen))     
print(weekopen)

new1=pandas.DataFrame()
new1['Date']=list1
new1['High']=maxweek
new1['Low']=lowweek
new1['Open']=weekopen
new1['Close']=weekclose
print(len(new1))
print('end')
#print(len(df.Open))
