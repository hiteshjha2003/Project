#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Tuple:- is a collection of object which are immuatble and ordered

"""
Difference between List and Tuples:--
List :--
1) Mutable
2) Uses Square brackets[]
3) List has variable length
4) List are Homogenous
5) List shows Orders

Tuple :--
1) Immutable
2) Uses Parenthesis()
3) Fixed length
4) Tuples are heteogenous
5) Tuples will show structures

"""


# In[2]:


t1 = (10,20,30)
print(t1)


# In[3]:


t2 = (10,20,'A', 'a' , 'Names')
print(t2)


# In[4]:


t3 = ("Python" , [10,20,30] , ['A' , 'B' , 'C']) #list inside the tuple
print(t3)


# In[5]:


t4 = (('A'   , 'B' , 'C'), (1,2,3) , ('!' , '@' , '#')) #tuple inside the tuple
print(t4)


# In[7]:


t5 = 10,20,30,40,50
print(t5)


# In[10]:


#indexing / Slicing :---
tn = (0,10,20,30,40,50,60,70,80,90)
print(tn[3])


# In[11]:


print(tn[-1])


# In[12]:


print(tn[1:])


# In[13]:


print(tn[:6])


# In[14]:


print(tn[1:6])


# In[15]:


print(tn[1:6:2])


# In[19]:


#tuple Assignments
    
t_name = (11, "Gaurav" , "Pune")
(id , name , city) = t_name
print(id)
print(name)
print(city)


# In[24]:


list2 = [10 , 'Hitesh' , 'Anuhuya' , 'Aryaditya', 'Pune']
[id , name1 , name2 , name3 , city] = list2
print(id)
print(name3)
print(city)


# In[26]:


t = divmod(7,3)
print(t)


# In[30]:


t1 = (10,20,30,40)
print(t1)
print(t1.remove(10))


# In[33]:


t3 = (1,2,3,4,5)
res = t3[:2] + t3[3:]
print(res)


# In[37]:


t10 = (1,2,3,4,5,6)
list1 = list(t10) # convert tuple into list
print(list1)
list1.remove(5)


print(list1)
b = tuple(list1) # Convert list into tuple
print(b)


# In[39]:


t1 = (10,20)
t2 = (30,40)
print(t1+t2)
print(t1*10)


# In[40]:


tuples = (1,2,3,4,5,6,7,8,9)
for i in tuples:
    print(i)


# In[41]:


tupless = (('A'   , 'B' , 'C'), (1,2,3) , ('!' , '@' , '#'))
for i  in tupless:
    for j in i:
        print(j , end = ' ')
    print('\n')
    


# In[42]:


t100 = (1,2,3,4,5,6,7,8,9)
print(min(t100))


# In[43]:


print(max(t100))


# In[44]:


print(sum(t100))


# In[45]:


print(len(t100))


# In[46]:


print(sum(t100)/len(t100))


# In[48]:


#zip function :-- It will zips the elements from two tuples into a list of tuples
tup1 = (1,2,3)
tup2 = ('A', 'B' , 'C')
tup3 = zip(tup1 , tup2)
print(list(tup3))


# In[52]:


tupl12 = (1,1,1,2,2,3,5)
print(tupl12.count(2))


# In[53]:


print(tupl12.index(2))


# In[ ]:




