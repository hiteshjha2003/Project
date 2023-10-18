#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Anonymous Functions is also calld as Lambda functions
syntax :-
lambda [arg1 , arg2 , arg3 , ....] : [expression/Conditions]

 
"""


# In[2]:


sq = lambda x1 : x1*x1
print("Sqaure of a nos :" ,sq(10) )


# In[4]:


l1 = [2,1,2,214,5]
l2 = []

for i in l1:
    tmp = lambda i : i**2
    l2.append(tmp(i))

print(l2)


# In[5]:


l1 = [2,1,2,214,5]

l2 = list(map(lambda v:v**2 , l1)) #iteraion with conditions then u can use map with lambda

print(l2)


# In[10]:


lst1 = [2,4,6,27, 21,23,16,20]

l2 = list(map(lambda x : x**2 , filter(lambda y : y%2, lst1))) #if you want to use more then one condition in map function then another condition must be write inside the filter()

print(l2)


# In[15]:


#Void functions:--

def show():
    str = "Hello Hi Python what you are doing here go in amazon forest"
print(str)
print(show())



# In[18]:


#Sum of two nos :--
summation = lambda arg1  , arg2 : arg1+arg2
print("Value of total :" , summation(10,20))


# In[19]:


x = lambda a: a+10
print(x(10))


# In[2]:


#Reduce function
from functools import reduce
lst = [10,20,30,40,50]
sum = reduce((lambda x  , y :x+y) , lst)
print(sum)


# In[ ]:




