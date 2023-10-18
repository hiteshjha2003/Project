#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""

Data Analysis :--

    It is a process of inspecting  , cleaning , transforming and modelling the data they have the gaol of discovering the
    useful information  and taking out some conclusion out of it.
    
    
    
Data Analytics:--

    Data analysis is subset of Analytics  domain..

Lifecycle of Data Analytics:--
1. Data Discovery:-
            to set some project objectives, 
            
            
2.Data Preparation:--
        

3.Model Planning:--


4.Model Building:--
        
        
5.Communication Results:-


6.Operationalize :-- 



"""
"""
Data Sources:---
How many formats of Data ?
Excel , CSV , JSON , Different types of Databases..and etc

Sources:-- Wikipedia , Social Medias , Kaggle , Texts , Hardcopies , Audios  , Videos, and Etc



"""







# In[1]:


"""

Numpy :---
    Numerical Python is used scientific computing.
    
    
    



"""


# In[2]:


import  numpy as np


# In[3]:


get_ipython().system('pip install numpy')


# In[6]:


n_array = np.array([[0,1,2,3] , 
                   [4,5,6,7] , 
                   [8,9,10,11]])

print(n_array)


# In[8]:


"""
three important attributes are there of for array


1) ndim:-- to find the dimensions of the array

2) shape:-- size of each dimensions it will return rows and columns

3) dtype :-- datatype of the array


"""
print(n_array.ndim)

print(n_array.shape)

print(n_array.dtype)


# In[10]:


names = np.array([['Suman' , 'Vyanktesh'] ,
                  ['Madhuri' , 'Hitesh'] ,
                  ['Gaurav' , 'chetan']])
print(names)


# In[23]:


#Mathematcal Operations:--
#Array Addition:-

a = np.array([1,2,14,40,50,60])
b = np.array([7,8,9,10,11,12])

sub = b-a

add = a+b

product = a*b

div = a/b


square = a**2

print(square)
print(div)
print(sub)
print(add)
print(product)



print(" The cosine of a matrix is ",np.cos(a))

print(b<2)
print(a==b)
print(a!=b)
print(a>=b )


# In[24]:


A1 = np.array([[1 , 1], 
              [1,2]])

A2 = np.array([[3 , 4], 
              [5, 6]])


print(A1)

print(A2)


# In[25]:


print(A1+A2)


# In[26]:


print(A1-A2)


# In[27]:


print(A1*A2)


# In[28]:


print(A1/A2)


# In[29]:


print(A1)

print(A2)


# In[37]:


print(n_array)


# In[38]:


print(n_array.ravel())


# In[40]:


n_array.shape = (6,2)
print(n_array)


# In[41]:


print(n_array.transpose())


# In[ ]:




