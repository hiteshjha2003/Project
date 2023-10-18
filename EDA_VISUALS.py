#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Data Visualization:--

EDA :- Explorartory Data Analysis:--

For Visual :-
matplotlib and Seaborn


Why Visualizations necessary

1) To identify Outliers in data

2) Improve Response time:--

3) Greater Simplicity :--


What is Visual Encoding?
Distribution --- Scatter chart , 3D Area Chart , Histograms
Relationship :-- Bubble Chart , Scatter Chart
Comparison :- Bar Chart , Line Chart , Column Chart  , Area Chart
Composition:-- Pie Chart ,Waterfall Chart , Stacked Column Chart , Stacked Area chart
Location :--Maps(Bubble Maps  , Choropleth map , Connection Map)
Connection :-- Matrix Chart , Node-lin-Diagram , Word Cloud , and etccc



Lemme give you some intro abt libraries:--
matplotlib
seaborn

plotly
altair

ggplot
Bokeh library

geoplotlib





"""


# In[1]:


get_ipython().system('pip install matplotlib')


# In[3]:


#Histograms:--
import matplotlib.pyplot as plt
import numpy as np

a = np.array([22,87,4,5,65,14,56,25,87,69,26,36,12,45,68,45])

plt.hist(a , bins=[0,25,50,75,100] ,edgecolor= "green" , color ="lightgray")

plt.title("An example of histogram")

plt.xlabel("Data Values")

plt.ylabel("Values")

plt.show()



# In[5]:


#Bar Chart (Vertical) :-
x = ['Pascal' , 'C' , 'JAVA' , 'Python' , 'R'  , 'C#' , 'C++']
y = [1,2,3,4,5,6,10]

plt.bar(x , y , edgecolor = 'blue' , color ='orange')

plt.xlabel("Programming Languages")

plt.ylabel("Nos of Usages")

plt.title("Programming languages used in Companies")

plt.show()


# In[6]:


#Bar Chart (horizontal) :-

x = ['Pascal' , 'C' , 'JAVA' , 'Python' , 'R'  , 'C#' , 'C++']
y = [1,2,3,4,5,6,10]

plt.barh(x , y , edgecolor = 'blue' , color ='orange')

plt.xlabel("Programming Languages")

plt.ylabel("Nos of Usages")

plt.title("Programming languages used in Companies")

plt.show()


# In[9]:


#Scatter Plots :--

x = np.array([5,6,8,7,9,5,4,2,36,5, 8])
y = np.array([4,5,6,89,80,40,60,50,60,47,80])

plt.scatter(x ,y)

plt.xlabel('Age of Car (yrs)')

plt.ylabel('Maximum Speed')


plt.title("Correlation betwen car age and speed")

plt.show()



# In[10]:


#Line Charts:--
x = [2015,2016,2017,2018,2019,2020,2021,2022,2023]

y_abc = [11,12,14,16,18,16,21,25,30]

y_pqr = [11,12,20,45,50,16,21,25,30]

plt.plot(x , y_abc , marker = 'o' , color = 'blue' , linewidth = 2 , label='Company ABC')
plt.plot(x , y_pqr , marker = 'D' , color = 'red' , linewidth = 2 , label='Company  PQR')

plt.xlabel('year')

plt.ylabel('Sales in Lakhs')

plt.title('Sales trend of ABC and PQR Companies')

plt.legend()

plt.show()


# In[20]:


#Area Plots

import seaborn as sns
import pandas as pd

sns.set_theme()

df  = pd.DataFrame({'Period':[1,2,3,45,6,7,8],
                   'team_A':[20,1,1,4,16,45,14],
                   'team_B':[5,7,8,9,7,4,5],
                   'team_C':[4,5,6,8,9,7,8]})


plt.stackplot(df.Period , df.team_A , df.team_B , df.team_C)

plt.show()


# In[31]:


#Pie Charts

labels = ['Pascal' , 'C' , 'JAVA' , 'Python' , 'R'  , 'C#' , 'C++']
sizes = [32,47,85,94,48,65,15]
colors = ['silver' ,'green' , 'skyblue' , 'pink' , 'orange' , 'gold', 'red' ]

explode = (0,0,0,0,0,0,0.1)

plt.pie(sizes  ,explode = explode, labels = labels , colors = colors  , autopct ='%1.1f%%', shadow = True)

plt.title(" percentange of Students learning Programming Languages ")

plt.show()


# In[34]:


#Some Special charts

#doughnut

labels = ['Pascal' , 'C' , 'JAVA' , 'Python' , 'R'  , 'C#' , 'C++']
sizes = [32,47,85,94,48,65,15]
colors = ['silver' ,'green' , 'skyblue' , 'pink' , 'orange' , 'gold', 'red' ]

explode = (0,0,0,0,0,0,0.1)

plt.pie(sizes  ,explode = explode, labels = labels , colors = colors  , autopct ='%1.1f%%', shadow = True)

circle = plt.Circle((0,0)  , 0.75 , color = 'blue' , fc = 'white' , linewidth = 1.25)

Figure = plt.gcf()
Figure.gca().add_artist(circle)

plt.title(" Percentange of Students learning Programming Languages ")

plt.show()


# In[ ]:




