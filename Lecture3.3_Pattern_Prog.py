#!/usr/bin/env python
# coding: utf-8

# In[9]:


rows = int(input("Enter nos of rows"))
columns = int(input("Enter nos of cols"))

import time
start_time = time.time()

for i in range(rows):
    for j in range(columns):
        if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

end_time = time.time()

execution_time = end_time-start_time

print("Execution time  in" , execution_time , "seconds")





# In[10]:


rows = int(input("Enter nos of rows"))
columns = int(input("Enter nos of cols"))

import time
start_time = time.time()

i = 1

while i<=rows:
    j = 1
    while j<=columns:
        if i ==1 or i==rows or j==1 or j== columns:
            print("*" ,end = " ")
            
        else:
            print(" " , end = " ")
        j+=1
    
    print()
    i+=1
    
end_time = time.time()

execution_time = end_time-start_time

print("Execution time  in" , execution_time , "seconds")


# In[ ]:




