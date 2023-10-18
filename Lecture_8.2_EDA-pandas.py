#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
pandas :---

Its is designed for Data Analysis and it has been built on the top of Numpy 



 this pandas library essentially has three data structures:---
 
 1) Series
 
 2) DataFrame
 


"""


# In[17]:


#Series:-- Series is one dimensional array which can hold any type of Data such as integers , floats  , strings , and Python objects

import numpy as np
import pandas as pd

pd.Series(np.random.randn(5))


# In[22]:


pd.Series(np.random.randn(5) , index = {'a' , 'b' , 'c' , 'd' , 'e'})


# In[23]:


d = {'A':10 , 'B':20 , 'C':30}
print(pd.Series(d))


# In[26]:


"""
DataFrame:-- is used to create 2D array with can be of Diferent datatypes.this df can be seeen as table
inorder to create dataframe we required some data structures:-

1)1-D Numpy array
2) Lists
3) Dicts
4) Series
5) 2-D Numpy array



NaN :-- Not a Number
"""
#lets Create dataframe with the help of Series and Dicts:--

d1 = {
    'c1':pd.Series(['A' ,'B' ,'C']),
    'c2':pd.Series([10, 20 , 30, 40])
    
}

df = pd.DataFrame(d1)
print(df)


# In[30]:


#We will create dataframe with the help of List and Dicts

city_table = {
    
    'Names':['Hitesh' , 'Gaurav' , 'Madhuri' , 'Vyanktesh' , 'Suman'],
    'City' :['Pune-Vishrantwadi' , 'Mumbai' , 'Pune-Pimpri' , 'Satara', 'Haryana'],
    'age' : [10,20,30,40,50]
}


print(pd.DataFrame(city_table))


# In[34]:


d2 = {
    'Item1':pd.DataFrame(np.random.randn(4 , 3)),
    'Item2':pd.DataFrame(np.random.randn(4,2))
}

print(pd.Series(d2))


# In[36]:


#Reading of a Data  it means to load the data by using pandas

data = pd.read_csv("netflix_titles.csv")
print(data)


# In[43]:


data2 = pd.read_csv("C:/Users/com/Downloads/netflix_titles.csv")
print(data2)


# In[44]:


data2 = pd.read_excel("D:/netflix_titles.xlsx")
print(data2)


# In[ ]:




