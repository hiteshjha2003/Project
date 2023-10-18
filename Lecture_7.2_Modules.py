#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Modules:----
"""

It can be defined as a python program file which contains a python code including functions , classes and etc
 
predefined functionss

user-defined functions


Collection of modules  is said to be a Packages


                        Packages(numpy , pandas ,matplotlib , seaborn)
                           |
                           |
                        Modules (functools , itertools, math, ctypes)
                           |
                           |
                    Built in  Functions (len() , max() , abs() , reduce())
                    
                    
                    
import module_name
import package_name

from module_name import function
from pacakage_name import function, module


when you want import all the built-in function inside any module or pacakge then ue can use *

from module_name import*
from pacakge_name import*

       
"""







# In[1]:





# In[5]:


import math as m 
m.ceil(1.001)

m.sin(90)

m.cos(45)

m.sqrt(144)


# In[39]:


#Random module

import random as r 


#randrange() method is used to generate the random integer 
#rnos = r.randrange(10) 
#print(rnos)
print(r.randrange(10))




# In[40]:


#shuffle() method is used to shuffle the content of the list
color = ['cyan' , 'Magenta' , 'yellow' , 'Black']
shf = r.shuffle(color)
print("Reshuffled color are :" , shf , color)


# In[47]:


#randint() method within bounds like lower bound and upper bound it will generate random integers

print(r.randint(0,10))


# In[1]:


#itertools Module :-
from itertools import*
for val in chain([1,2,3,4,5] , ['a' , 'b' , 'c' , 'd']):
    print(val)


# In[ ]:


value = int(input("Enter ur value"))
l1 = [5,10]


# In[2]:


from itertools import cycle 
cycled_values = cycle(["A", "B", "C"])

# Display the items only 10 times
num_iterations = 10
for _ in range(num_iterations):
    item = next(cycled_values)
    print(item)


# In[18]:


#Datetime module

import datetime as dt
x = dt.datetime.now()
print(x)
print(x.year)
print(x.month)
print(x.strftime("%y"))


# In[ ]:




