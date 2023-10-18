#!/usr/bin/env python
# coding: utf-8

# 
# 
# 
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 

# In[15]:


"""

1
1 2
1 2 3 
1 2 3 4
1 2 3 4 5
"""
rows = 5
for i in range(1 , rows+1):
    for j in range(1 , i+1):
        print(j ,end = ' ' )
    print(' ')
    

    

n = [1 , 2  ,3  , 4 , 5]
for i in n:
    for j in range(i):
        print(i , end= ' ')
    print('')
    


# In[21]:


"""
5 5 5 5 5
5 5 5 5
5 5 5 
5 5
5

"""


for i in range(1,6):
    for j in range(i , 6):
        print("5", end = ' ')
    print(' ')
    

    


rows = 5
num = rows

for  i in range(rows , 0 ,-1):
    for j in  range(0,i):
        print(num,end = ' ')
    print(' ')
    
    
    




# In[10]:


for i in range(1,6):
    for j in range(i , 6):
        print("*", end = ' ')
    print(' ')
    
    


# In[40]:


"""
1 1 1 1 1 
2 2 2 2
3 3 3
4 4
5

"""


    

import time

start_time = time.time()

for i in range(1,6):
    for j in range(i , 6):
        print(i, end = ' ')
    print(' ')
    
end_time = time.time()


execution_time = end_time-start_time
print("Execution time of the code  " , execution_time , "seconds")

    
    
    


start_time = time.time()
    
rows = 5
b = 0
for i in range(rows , 0 , -1):
    b+=1
    for j in range(1 , i+1):
        print(b , end=' ')
    print(' ')

end_time = time.time()


execution_time = end_time-start_time
print("Execution time of the code  " , execution_time , "seconds")


# In[41]:


"""

         1
      1  2
    1 2  3
  1 2 3  4
1 2 3 4  5 


"""


rows = 6
for i in range(1, rows):
    num = 1
    for j in range(rows, 0 , -1):
        if j>i:
            print(' ' , end = ' ')
        else:
            print(num , end=' ')
            num+=1
    print(" ")
    
    
    


# In[ ]:


# Pascals Traiangle:---

"""
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1

(a+b)^2 = a^2 + 2ab +b^2
(a+b)^3 = a^3 +3a^2b + 3ab^2 +b^3

(a+b)^6 = a^6 + 6a^5b +15a^4b + 20ab^3 + 15ab^2 + 6ab + b^6


"""









