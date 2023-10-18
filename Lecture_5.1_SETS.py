#!/usr/bin/env python
# coding: utf-8

# In[7]:


"""
Set :-
Unordered Collection of Unique elements

Duplicate elements is not allowed inside the set and it must be immutable:-

Sets {}


we cannot access the individual elements in a set

We can only access all the elements at once  and it is possible  by traversing



"""

a = {1,3,4,5,7,9}
print(type(a))


b = {1,1,2,2,3,34,5,68,97}
print(b)


# In[10]:


s1 = set('abc')
print(s1)

s2= set(range(1 , 10))
print(s2)


# In[13]:


days = set(['Mon', 'Tues' ,'Wed' ,'Thur', 'Fri' ,'Sat'])
print(days)
for d in days:
    print(d)


# In[16]:


#Frozen Set :-
        #But its elements cannot be changed once it is assigned
    

vowels = ('a' , 'e' ,'i' , 'o' ,'u')
fset = frozenset(vowels)
print(fset)

#fset.add = 'v'


# In[20]:


s1 = {"A" ,"B" ,"C" , "D" , "E" , "F"}
print(s1.discard("B"))
print(s1.remove("A"))
print(s1.clear())
print(s1)


# In[23]:


#lets addd something
s2 = {1,2,3,4,5}
print(s2)

print(s2.add(6))
print(s2)


# In[27]:


#UPdate something
s3 = {1,2,3}
s4 = {'a' , 'b' , 'c'}
print(s3.update(s4))
print(s3)
print(s3.update({4,5}))
print(s3)


# In[34]:


#Set operations:--
#Union Set(|)

A = {1, 2,3 ,4 , 5}
B = {6,7,8,9,10}
print(A|B)

DaysA = set(["Mon" , "Tue" , "Wed"])
DaysB = set(["Thurs", "Fri" ,"Sat"])

Res = DaysA | DaysB
print(Res)


# In[35]:


#Intersection of Sets (&):--
A1 = {1,2,3,4,5,6}
A2 = {4,5,6,7,8,9}
print(A1&A2)


DaysA = set(["Mon" , "Tue" , "Wed", "Thurs"])
DaysB = set(["Thurs", "Fri" ,"Sat"])

Res = DaysA &DaysB
print(Res)


# In[36]:


#Difference of Sets:--
Set1 = {1,2,3,4,5,6,7,8}
Set2 = {1,2,3,4,5,6}

print(Set1-Set2)


DaysA = set(["Mon" , "Tue" , "Wed"])
DaysB = set(["Thurs", "Fri" ,"Sat"])

Res = DaysA - DaysB
print(Res)


# In[37]:


#Comparison of Sets:--
DaysA = set(["Mon" , "Tue" , "Wed"])
DaysB = set(["Thurs", "Fri" ,"Sat" , "Mon","Tue" ,"Wed"])

SuperSet = DaysA>=DaysB
Subset = DaysA>= DaysB

print(SuperSet)
print(Subset)


# In[38]:


#Symmeteric Differnce :--

# Two sets A and B is said to be symmetric difference if set (A-B) Union (B-A)

A = {1,2,4,6,8}
B = {1,2,3,4,5}
C = A^B
print(C)


# In[ ]:




