#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Dictionary :--
"""
       --- It is an unordered collection of an elements where data is stored in the form of 
        key-value pairs.
       -- Is also called as associative data structure :- elements or items arev stored in non-linear fashion.
       -- here positions and indexes is not useful.
       -- Dictionary is mutable datatypes .
syntax:--
dict_name = {key1:value1 , key2:value2 , key3:value3 , ........ , keyn:valuen}

dictname = {}
list1 = []
t1 = ()


Rules:--
1.There should be one key and one value pair ,
2.dictionary doesn't hold multiple keys and mutiple values



"""
d1 = {1:'Orange' , 2:'Mango', 3:'Apple' , 4:'PineApple'}
print(d1)


d2 = {1:'Orange' , 2:'Mango', 3:'Apple' , 4:'PineApple' , 5:[10,20,30]  , 3.14:[1.23,3.15,321.36] ,
      'Names':['Anhuya' , 'preety' , 'mayank' , 'suman', 'vyanktesh' , 'vaibhav']}

print(d2)

d3 = {['Anhuya' , 'preety' , 'mayank' , 'suman', 'vyanktesh' , 'vaibhav']:'Names'} #this is mot possible
print(d3)


d4 = {'Anhuya' , 'preety' , 'mayank' , 'suman', 'vyanktesh' , 'vaibhav' : 'N1' , 'N2' , 'N3' , 'N4', 'N5' , 'N6'}
print(d4)


d5 = {'Anhuya'  : 'N1' , 'N2' , 'N3' , 'N4', 'N5' , 'N6'}
print(d5)


# In[16]:


#Built-in function
# dict()
# in how many types you create your dictionaries:--
d12 = {1:'Orange' , 2:'Mango', 3:'Apple' , 4:'PineApple'}
print(d12)

d1 = dict({1:2 , 3:4 , 'Name' :'Coahcx'})
print(d1)


d2 = dict([(1,"Red") , (2 , "yellow") , (3 , "Green")])
print(d2)

#dn = (1,"Red") , (2 , "yellow") , (3 , "Green")
d3 = dict(one =1 , Two=2 , Three = 3)
print(d3)


# In[20]:


#How to Acces the values in a Dictionary:---
#1. Referring to its key name  , inside the Square brackets([])

d12 = {1:'Orange' , 2:'Mango', 3:'Apple' , 4:'PineApple'}
print(d12[1])
print(d12[3])
print(d12[3 ,4]) # this is simply not possible


# In[26]:


#2. By using get() method returns the values for a key 

d12 = {1:'Orange' , 2:'Mango', 3:'Apple' , 4:'PineApple'}

print(d12.get(1))

print(d12.get(2))

print(d12.get(2,3))

print(d12.get(3,4)) # It will always consider first key


#print(d12['Orange'])
print(d12.get('Orange')) 


# In[27]:


#How we can Access the keys 

d12 = {1:'Orange' , 2:'Mango', 3:'Apple' , 4:'PineApple'}


print(d12.keys())


# In[33]:


#How we can access the particular key :--
names = {"Pune":31 , "Mumbai":41, "Jaipur":51 , "Delhi":61}
print(names)

print(names.keys())


print('2nd keys using the keys():'   , list(names.keys())[1])

print(list(names.keys())[2])



# In[36]:


#Deleting the elements from a Dictionary :--
#Remove an  last items:-

Squares = {1:1 ,2:4 , 3:9 , 4:16 , 5:25}
print(Squares.popitem())

print(Squares)



# In[38]:


#Remove a Particular item with given key :--
Squares = {1:1 ,2:4 , 3:9 , 4:16 , 5:25}
print(Squares.pop(2))
Squares


# In[41]:


#Remove all the items:--
Squares = {1:1 ,2:4 , 3:9 , 4:16 , 5:25}
print(Squares)

print(Squares.clear())
Squares


# In[46]:


#Updating of a Dictionary :--
# update the Values in dictionary:--
d1 = {'Name1':'Hitesh' ,'Name2':'Anuhya' , 'Name3':'Aryaditya', 'Name4':'Gaurav' }
print(d1)
d1['Name1'] = 'MADHURI'
print(d1)

d1['Name5']= 'Suman Nayak'
print(d1)

d1['Name6']= ['Vyanktesh', 'Mayank' , 'preety']
print(d1)


# In[48]:


#Basic Operatios:--
#Memebership test:- in
Squares = {1:1 ,2:4 , 3:9 , 4:16 , 5:25}
print(1 in Squares )
print(10 in Squares )


# In[53]:


#Traversing Dictionary :-
Squares = {1:1 ,2:4 , 3:9 , 4:16 , 5:25}
for i in Squares:
    print( i, Squares[i])
    #print(i) This is for printing the keys
    #print(Squares[i]) # this is for printing the values


# In[57]:


#Traversing List inside the Dictionary :--
# By using list comprehension
d1 = {'Names':[1,2,3,4,5] , 'Roll_nos':[10,20,30,40,50] , 'Address':['Pune' , 'Banglore' ,'Delhi']}
print(d1)
res = [[i for i in d1[j]] for j in d1.keys()]
print(res)



# In[72]:


#Built-in Functions  and Methods in dictionary:--
Squares = {1:1 ,2:8 , 3:9 , 4:64 , 5:25}
print(all(Squares))

# traversing  - list , tuples , dictionary






# In[61]:


dict = {}
print(any(dict))


# In[73]:


len(Squares)


# In[74]:


type(Squares)


# In[76]:


Squares.clear()
print(Squares)


# In[78]:


s1 = {1:1 ,2:8 , 3:9 , 4:64 , 5:25}

s2 = s1.copy()

print(s2)


# In[ ]:




