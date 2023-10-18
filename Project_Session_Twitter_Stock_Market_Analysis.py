#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install plotly')


# In[39]:


import pandas as pd
import datetime
from datetime import date , timedelta

import plotly.graph_objects as go
import plotly.express as px

import plotly.io as pio


pio.templates.default = "plotly_white"




# In[40]:


#1)	Read the data and display the first 100 rows from the data
data = pd.read_csv('twtr.csv')
print(data.head(100))


# In[41]:


#2)Give the column insights 

print(data.info())


# In[42]:


#3)	Check whether this dataset contains any null values or not if it is there then remove the null values from it 
print(data.isnull().sum())




# In[43]:


data = data.dropna()
print(data.head(100))


# In[44]:


print(data.isnull().sum())


# In[45]:


#4)Find the statistical description of the data.
print(data.describe())



# In[46]:


#5)Find the missing values in the data 
print(data.isnull().sum())


# In[47]:


get_ipython().system('pip install statsmodels')


# In[23]:





# In[48]:


#6)Give me the Z-test O/R T-test over High, low, and close columns and see if the null hypothesis gets rejected or accepted

#Program for z-test

import statistics as st
from statsmodels.stats import weightstats as stests
from numpy import random

high = data['High']
print('Data=' ,high)
high_mean = st.mean(high)
print("Mean Data = " , high_mean)
high_stdev = st.stdev(high)
print("Standard Deviation" , high_stdev)

ztest  , pval = stests.ztest(high , value = 30)
print("Z-test Score" , ztest)
print("p-Value " , pval)

if pval<0.05:
    print("Reject Null hypothesis")
else:
    print("Accept the Null hypothesis")
    
       


# In[32]:


#program for T-test
from scipy.stats import ttest_1samp
import statistics as st



high = data['High']
print('Data=' ,high)
high_mean = st.mean(high)
print("Mean Data = " , high_mean)
high_stdev = st.stdev(high)
print("Standard Deviation" , high_stdev)

t_test  , pval = ttest_1samp(high , 50)
print("T-test Score" , t_test)
print("p-Value " , pval)

if pval<0.05:
    print("Reject Null hypothesis")
else:
    print("Accept the Null hypothesis")


# In[58]:


#7)By using ANOVA find the Fvalue and Pvalue from the data and see its Acceptance and rejection of the Null hypothesis

import pandas as pd
import scipy.stats
import io
data = pd.read_csv('twtr.csv')
print(data.head(5))
data = data.dropna()

grp1= data['High']
grp2 = data['Low']
print(grp1.head(5))
print(grp2.head(5))

F , pval = scipy.stats.f_oneway(grp1 , grp2)
print(F)
print(pval)

if  pval<0.05:
    print("Reject Null Hypothesis")
else:
    print("Accept Null Hypothesis")

    



# In[62]:


#8)Check if the data is dependent or independent by using the chi-square method

from scipy import stats
datas = {'High':data['High'] , 'Low':data['Low']}
print(datas)
chisq  , pval = scipy.stats.chisquare(datas['Low'])

alpha = 0.05
print("Chi-Square value =" , chisq)

print("p-value is " , pval)


if pval<alpha:
    print("Dependent {Reject Ho}")
else:
    print("Independent{Accept the Ho}")


    


# In[69]:


#Outliers --

from scipy import stats
import numpy as np
import pandas as pd

mu  , sigma = 100 , 5

array = np.random.normal(mu , sigma , 200)

array[90] = 180
array[50] = -40

df = pd.DataFrame(array , columns=['Data'])
print(df)

z = np.abs(stats.zscore(df))

print(z)


print("Nos of outliers=" ,df[z>3].count())
print("Outliers are:",df[(z>3)|(z<-3)])
df_new =  df[(z>-3)&(z<3)]

print(df_new)
print(df.shape)
print(df_new.shape)




# In[70]:


data = pd.read_csv('twtr.csv')
print(data.head(100))


# In[71]:


print(data.isnull().sum())


# In[73]:


data = data.dropna()
print(data.head(50))


# In[76]:


#11)Show the Twitter stock prices over the years  and give a conclusion.

figure = go.Figure(data = [go.Candlestick(x = data["Date"],
                                        open =data["Open"],
                                       high = data["High"],
                                       low = data["Low"],
                                       close = data["Close"])])

figure.update_layout(title="Twitter Stcok Prices Over the Years" , xaxis_rangeslider_visible=False)

figure.show()




# In[77]:


#12)Now compare the close vs date column for Twitter prices over the years.

figure = px.bar(data , 
               x = "Date",
               y = "Close",
               color = "Close")

figure.update_xaxes(rangeslider_visible= True)
figure.show()




# In[79]:


import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(16,10))

sns.heatmap(data.isnull() , cbar = False , cmap="YlGnBu")

plt.show()


# In[81]:


#14)Assign buttons to control time periods.  Add the  buttons to analyze the stock prices of Twitter in different time periods:

figure = px.bar(data , x = "Date" , y ="Close" , color = "Close")
figure.update_xaxes(rangeslider_visible = True)

figure.update_layout(title = "Twitter Stock prices over the years" , xaxis_rangeslider_visible=False)

figure.update_xaxes(
    
    
    
    
    
    
    
    rangeselector = dict(
        buttons = list([
            
            dict(count = 1 ,label = "1m" , step ="month" ,stepmode ="backward"),
            dict(count = 6 ,label = "6m" , step ="month" ,stepmode ="backward"),
            dict(count = 3 ,label = "3m" , step ="month" ,stepmode ="backward"),
            dict(count = 1 ,label = "1y" , step ="year" ,stepmode ="backward"),
            dict(count = 2 ,label = "2y" , step ="year" ,stepmode ="backward"),
            dict(step="all"),
                
            
        ])
    
    
    )

)


figure.show()


# In[83]:


#15)Give the complete timeline of Twitter in the stock market. (Line Graph)
data["Date"] = pd.to_datetime(data["Date"], format='%Y-%m-%d')
data['Year'] = data['Date'].dt.year

data["Month"] = data["Date"].dt.month




fig = px.line(data , 
             x="Month",
             y="Close",
             color ="Year",
             title ="Complete timeline of Twitter")

fig.show()


# In[87]:


import plotly.figure_factory as ff
import numpy as np
x = np.random.rand(15,12)
fig = ff.create_dendrogram(x)
fig.update_layout({'plot_bgcolor':'white'})
fig.show()


# In[ ]:




