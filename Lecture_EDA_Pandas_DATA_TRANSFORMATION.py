#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv('netflix_titles.csv')
print(df)


# In[3]:


#Let's check it out First 10 Rows for First n rows 
print(df.head(10))


# In[4]:


#Last 10 data
print(df.tail(5))


# In[5]:


print(df.isnull())


# In[14]:


df['release_year'].loc[1:100:20].isnull()



# In[15]:


#Creating a dataframe

df = pd.DataFrame(np.random.randn(5 , 3) , index = ['a' , 'c' ,'b'  ,'e' , 'h'] , columns = ['c1', 'c2' , 'c3'])

print(df)




# In[16]:


df = df.reindex(['a', 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])
print(df)


# In[17]:


# replace the missing values with zeros

print("\n \n Every missing values replaced with '0':")
print(df.fillna(0))


# In[18]:


#Drop rows with missing values
print("\n \n Dropping Rows with Missing Values:")
print(df.dropna())



# In[20]:


#replacing Missing values with Mean/Median/Mode

print("Replacing NaN with Median Values:")
median = df['c1'].median()
print(median)

df['c1'].fillna(median , inplace = True)
print(df)




# In[21]:


mean = df['c1'].mean()
df['c2'].fillna(mean , inplace = True)
print(df)


# In[23]:


mean = df['c3'].mean()
df['c3'].fillna(mean, inplace = True)
print(df)


# In[25]:


df1 = pd.DataFrame(np.random.randn(5 , 3) , index = ['a' , 'c' ,'b'  ,'e' , 'h'] , columns = ['c1', 'c2' , 'c3'])

print(df1)


# In[26]:


df1 = df1.reindex(['a', 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])
print(df1)


# In[30]:


#replace the NaN values with prev or next values:--
df1 = df1.fillna(method = "ffill") # this is for filling with Previous value
print(df1)

df1 = df1.fillna(method = "bfill") # this is for filling with next values
print(df1)


# In[31]:


#By using interpolation method :--
df_new = df1.interpolate()

print(df_new)


# In[ ]:


"""
Noisy Data :--

Errors
Outliers(Anomalies)
Inconsistent values

Reasons for Noisy Data.
1. Duplicate Entries
2. Mutiple Entries for a  single Entity.
3. Huge Outliers 

Outliers :--
Its an Observation that lies an abnormal distance from other values in an Attribute columns 
i.e it dffers significantly from other values.
Causes of Outliers:--
1. Measurement Errors
2. Data Entry error
3. Experimental Error
4. Data Processing Error
5. Sampling Errors


"""



# In[ ]:


"""
Data Transformation:---
What ?
    Is a Process of Converting data from one format to another format.
    Typically from the format of source system into required destination system.
    
    
How ?

sklearn :-- scikit learning is ML library


1. Rescaling:---
    It transform the data in such way that it fits for given range of values like minimum to maximum(0-100) (100-200)
    
2. Normalising:--
    its a scaling technique simple ur values or data get scaled again between 0 to 1(Min-Max Scaling)
    
    
3. Binarizing:--
    Its a  Process of Converting the data to either 0 or 1 based on a threshold value.
    
4. Standardizing:---
    

5. Label Encoding:--
    Ordinal features:-- Features have some orders
    
    Nominal features:--features doesn't have any orders it have just label
    
    
6. One Hot Encoding:--
    white -100
    red - 010
    balck - 001



"""


# In[32]:






# In[33]:


get_ipython().system('pip install scikit-learn')


# In[35]:


from sklearn import preprocessing
import pandas as pd



# In[36]:


#create a dataframe:--
df = pd.DataFrame({"Apples":[10,20,30] , "Oranges":[40,50,60]})
print(df)


# In[37]:


normalized = preprocessing.normalize(df)
print("Normalized Data")
print(normalized)



# In[38]:


from sklearn import preprocessing
import pandas as pd
import numpy as np
import scipy.stats as s


# In[39]:


#Create Dataframe:--

d = {'c1':[1,2,3,4] , 'c2':[4,5,6,7] , 'c3':[8,9,10,11]}
data = pd.DataFrame(d)


# In[40]:


print("\n \n ORIGINAL DATA VALUES")
print("--------------------------------")

print(data)


# In[42]:


#Method 1 Rescaling of the Data

print("\n \n Data Scaled between 0 to 1:")
data_scalar = preprocessing.MinMaxScaler(feature_range = (0,1))
data_scaled = data_scalar.fit_transform(data)
print("\n Min Max Scaled Data")
print("-----------------------")
print(data_scaled)
print(data_scaled.round(2))



# In[47]:


#Method 2 :-- Normalization rescales such that sum of each row is 1
dn = preprocessing.normalize(data, norm = 'l1')
print("Normalized Data")
print("----------------")
print(dn.round(2))


# In[56]:


#Method 3:--Binarizing the data
data_binarized = preprocessing.Binarizer(threshold = 5).transform(data)
print("\n Binarized Data")
print("------------------")
print(data_binarized)


# In[59]:


#Method 4:- Standardization data
print("\n Standardized Data:")
print("---------------------")

data = np.array([[1.,-1.,2.],[2.,0.,0.],[0.,1.,-1.]])
print(" \n Original Data" , data)

print("\n Initial Mean:" , s.tmean(data).round(2))
print("\n  Initial Standard Deviation:", round(data.std() , 2))
data_scaled = preprocessing.scale(data)

data_scaled.mean(axis =0)
data_scaled.std(axis = 0)

print("\n Standardized data\n" , data_scaled.round(2))
print("\n Scaled Mean:" , s.tmean(data_scaled).round(2))
print("\n Standard deviation :" , round(data_scaled.std() , 2))












# In[62]:


#Method 5 :-- Label Encoding

from sklearn.preprocessing import LabelEncoder

data_f = {'Name':['Anhuya', 'Aryaditya' , 'Hitesh' , 'Gaurav' ,'Madhuri'],
         'Feedback':['Good' , 'Better' , 'Worst' , 'Excellent' , 'Best']}

dff = pd.DataFrame(data_f)
print(dff)


# In[65]:


print("\n LABEL ENCODING")
print("-------------------")
labelencoder = LabelEncoder()
dff['Feedback'] = labelencoder.fit_transform(dff['Feedback'])
print(dff)


# In[66]:


print("One Hot Encoding")
print("-------------------")
enc = preprocessing.OneHotEncoder()

onehotlabel_data = enc.fit_transform(dff[['Name']]).toarray()
print("\n" , onehotlabel_data)


# In[ ]:




