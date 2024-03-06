#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime,timedelta
import warnings 
warnings.filterwarnings('ignore')


# In[2]:


data=pd.read_csv('input.csv')
data.head()


# In[3]:


data.columns


# In[4]:


#data_new=data.drop(columns=[ 'Compensation', 'Compensation 1','Compensation 2','Review 1', 'Review 2',
#                   'Engagement 1','Engagement 2'])
l1=['Employee Code','Manager Employee Code','Date of Joining' , 'Date of Exit'] 
data_new=data[data.columns[data.columns.str.contains('date')].to_list() + l1]

#data_n=data.drop(data.columns[data.columns.str.contains('Compensation|Review|Engagement')],axis=1)
data_new.head()


# In[5]:


data1=data_new.melt(['Employee Code','Manager Employee Code','Date of Exit'],)
data2=data1.sort_values(by=['Employee Code','value'])
data3=data2.dropna(subset=['value'])
data3
data3[['value','Date of Exit']]=data3[['value','Date of Exit']].apply(pd.to_datetime)
data3['LeadDate']=data3.groupby(['Employee Code'])['value'].shift(-1)
data3


# In[6]:


data3['End Date']= data3.LeadDate - timedelta(days=1)
data3.drop(columns=['LeadDate'],inplace=True)


# In[7]:


for i in range (0,len(data3)):
    if pd.isnull(data3.iloc[i,5]):
        if pd.isnull(data3.iloc[i,2]):
            data3.iloc[i,5]=pd.to_datetime('2100-01-01')
        else:
            data3.iloc[i,5]=data3.iloc[i,2]
data3.drop(columns=['Date of Exit'],inplace=True)
data3


# In[8]:


#data3.loc[data3['variable']=='Date of Joining', 'Comp']='Compensation'
#data3.loc[data3['variable']=='Engagement 1 date','Comp']='Engagement 1'
#data3.loc[data3['variable']=='Review 1 date','Comp']='Review 1'
#data3.loc[data3['variable']=='Compensation 1 date','Comp']='Compensation 1'
#data3.loc[data3['variable']=='Engagement 2 date','Comp']='Engagement 2'
#data3.loc[data3['variable']=='Compensation 2 date','Comp']='Compensation 2'
#data3.loc[data3['variable']=='Review 2 date','Comp']='Review 2'
data3['Comp']=data3['variable'].apply(lambda x: x.replace(' date',''))
data3.loc[data3['variable']=='Date of Joining', 'Comp']='Compensation'
data3
data3.rename(columns={'value':'Effective Date'},inplace=True)
data3


# In[9]:


#data_comp=data.drop(columns=['Compensation 1 date', 'Compensation 2 date','Review 1', 'Review 2','Date of Joining',
 #                   'Engagement 1','Engagement 2','Date of Exit','Engagement 1 date','Engagement 2 date','Review 1 date','Review 2 date'])
#

s1 =set(data.columns[data.columns.str.contains('Compensation|Review|Engagement')])
s2 =set(data.columns[data.columns.str.contains('date')])
fin =list(s1-s2)
l2=['Employee Code','Manager Employee Code'] 
final = l2+fin
#print(final)
data_comp = data[final]
data_comp


# In[10]:


data_tp=data_comp.melt(['Employee Code','Manager Employee Code'])
data_tp_sort=data_tp.sort_values(by=['Employee Code'])
data_tp_sort


# In[11]:


data4=pd.merge(data3,data_tp_sort[['Employee Code','variable','value']],how='left', left_on=['Employee Code','Comp'],right_on=['Employee Code','variable'])
data4.drop(columns=['variable_y'],inplace=True)
data4['Comp']=data4['Comp'].str[:-2]
data4.loc[data4['variable_x']=='Date of Joining', 'Comp']='Compensation'
data4


# In[12]:


data_tp1=data4.pivot_table('value',['Employee Code','Manager Employee Code','variable_x','Effective Date','End Date'],'Comp')
data_tp2 = data_tp1.reset_index()
data_tp1_sort=data_tp2.sort_values(by=['Employee Code','Effective Date'])
data_tp1_sort


# In[13]:


data_tp1_sort.Compensation.fillna(method='ffill',inplace=True)
data_tp1_sort
data_tp1_sort.loc[data_tp1_sort['variable_x']=='Compensation 1 date', 'Last Pay Raise Date']=data_tp1_sort['Effective Date']
data_tp1_sort.loc[data_tp1_sort['variable_x']=='Compensation 2 date', 'Last Pay Raise Date']=data_tp1_sort['Effective Date']
data_tp1_sort['Last Pay Raise Date']=data_tp1_sort.groupby(['Employee Code'])['Last Pay Raise Date'].fillna(method='ffill')
data_tp1_sort=data_tp1_sort.drop(columns=['variable_x'])
data_tp1_sort


# In[14]:


data_tp1_sort['Last Compensation']=data_tp1_sort.groupby(['Employee Code'])['Compensation'].shift(+1)
data5=data_tp1_sort.fillna('')
data5


# In[ ]:





# In[15]:


data5['Variable Pay']=' '
data5['Tenure in Org ']=' '

data5


# In[ ]:





# In[16]:


#final_data['Last Pay Raise Date']=pd.to_datetime(final_data['Last Pay Raise Date'])
#final_data['Effective Date']=pd.to_datetime(final_data['Effective Date'])
#final_data['End Date']=pd.to_datetime(final_data['End Date'])
#final_data


# In[17]:


#final_data.to_csv('outputdata.csv',index=False)


# In[ ]:




