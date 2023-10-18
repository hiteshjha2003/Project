#!/usr/bin/env python
# coding: utf-8

# In[3]:


#For loop :-
#Iterate  over the lists , tuples ,string , and dictionary


# for variable in iteration_condition:
     #print(variable)

languages = ['Swift' , 'Python' , 'GO' , 'Javascript' , 'JAVA' , 'C' , 'C++' , 'C#' , 'Scala' ,'Fortran']

for i in languages:
    print(i)



# In[5]:


for x in 'Any thing you want':
    print(x)
    
    
    


# In[9]:


#Suppose you have a range 

values = range(10) #last-1
for  i in values: # iterate i =0 to i = 4
        print(i)
        


# In[10]:


languages = ['Swift' , 'Python' , 'GO' , 'Javascript' , 'JAVA' , 'C' , 'C++' , 'C#' , 'Scala' ,'Fortran']

for i in languages:
    print('Hello Python')
    print('Hi Python')
    
    
    


# In[11]:


languages = ['Swift' , 'Python' , 'GO' , 'Javascript' , 'JAVA' , 'C' , 'C++' , 'C#' , 'Scala' ,'Fortran']

for _ in languages:
    print('Hello Python')
    print('Hi Python')
    


# In[14]:


nos = [0,1,5,4]
for i in nos :
    print(i)
else:
    print("No items left")
    


# In[15]:


for i in range(0,10):
    print(i)


# In[16]:


names = ("Aryaditya" , "Shubh" ,"Suman" , "Chetan" , "vyanktesh", "Hitesh" )
for i in names:
    print(i)


# In[24]:


#dictionary = {'xyz':123 , 'abc':158}

d = dict()
d['xyz'] = 123
d['abc'] = 321
for i in d:
    print("%s %d" % (i , d[i]))
    print(i,d[i])
    


# In[ ]:


"""
#Escape Sequence:--
int - %d
string - %s
character - %c
float - %f
new line -\n

"""


# In[26]:


for letter in 'Coachxisbestplatform':
    if letter == 'c' or letter =='f' or letter == 'C':
        continue
    print("Current letter",letter)


# In[30]:


for letter in 'Coachxisbestplatform':
    if letter == 'f' :
        break
    print("Current letter",letter)


# In[31]:


for letter in 'Coachxisbestplatform':
    if letter == 'f' :
        pass
    print("Current letter",letter)


# In[ ]:




