#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello  , World")


# In[4]:


import sys    # This is a System Library
print(sys.version) # With this library we are importing Version nos



# In[5]:


import sys    # This is a System Library
print(sys.version) # With this library we are importing Version nos


# In[ ]:


# Single Line Commment 
"""
This is multiline commments 


"""



# In[11]:


#int:-- Integer 0-9 4B or 2B -32565 --- +32565

x = 10
print(x)

# String :-- Combination of Characters  '' , "" , ! , @ . # , $ , %, a , b , c , d, ....z , A ,  B , ... Z
print('Hello Python')


#float :-- Tkes the decimal value 3.14,23.2,265.36
print(3.14)

#boolean :--- True or False
print(bool(1))
print(bool(0))



# In[17]:


#I want to know the type of data
#type()  :-- function swhich shows the data type 
a = "Hitesh"
print(type(a))

b = 3.14
print(type(b))


c = 15
print(type(c))


print(type(True))




# In[20]:


# Complex nos always be in the form of a+bi
import cmath

a = 5
b = 3
c = complex(a , b)


d = 6+3j

print("The real part of Complex nos is " , end="")
print(c.real)
print("The imaginary part of Complex nos is " , end="")
print(c.imag)


print("The real part of Complex nos is " , end="")
print(d.real)
print("The imaginary part of Complex nos is " , end="")
print(d.imag)


# In[23]:


# How we can Convert one datatype to another datatype
nos = 6
print(str(nos))
print(type(str(nos)))

print(float(nos))
print(type(float(nos)))





# In[24]:


nos = 6.15
print(str(nos))
print(type(str(nos)))

print(int(nos))
print(type(int(nos)))


# In[27]:


bool_1 = True
bool_2 = False

print(int(bool_1))
print(int(bool_2))



print(float(bool_1))
print(float(bool_2))


print(str(bool_1))
print(str(bool_2))


print(type(str(bool_1)))


# In[30]:


print(9/3)
print(int(9/3))


# In[32]:


print(9//4)
print(float(9//4))


# In[33]:


print(type(9/3))
print(type(9//4))


# In[34]:


#Addition
x = 56+65+58+3.14+65.32+56
print(x)
print(type(x))


# In[35]:


#Subtraction
x = 85-52-21-8

print(x)


print(type(x))


# In[36]:


#Multiplication

x = 5*7
print(x)


# In[37]:


#Division
x = 125/24
print(x)
print(type(x))


# In[38]:


#Floor division
x = 125//24
print(x)
print(type(x))


# In[1]:


#Exponential

x = 2**3
print(x)



# In[4]:


# Modulus

x = 18%4
print(x)


# In[8]:


#An example Lets Calculate  How many mintues are there in 20 Hours
one_hour = 60
hours = 20
mins = one_hour*hours
print(mins)

print(60*20)



# In[7]:


#An example Lets Calculate  How many hours are there in 348 minutes

mins = 348
one_hour = 60

hours = mins/one_hour
print(hours)


print(348/60)

"""
1-
2-
3-0.8
4-8
5-18
6-28
7-38
8-48
9-58
10-complete time

"""


# In[9]:


#Strings :---

print('Hello , Python')
print("hello Python")

print('0 1 2 3 4 5 6 7 8 9')

print('!@#$%^&*)')




# In[11]:


#indexing of String :-- Position(Index Nos) of Characters in a String
#Indexing always Start with 0 to lastIndex-1

# Positive indexing goes from left to right start with 0
# Negative indexing goes from right to left and starts with -1



a = "Hello  , Python"
print(a[0])

print(a[8])


# In[12]:


#Lets find total length of String :-- len()

a = "Hello  , Python"
print(len(a))


# In[15]:


#Negative INdexing of a string

Name = "Pyhton"

print(Name[-1])
print(Name[-5])



# In[22]:


#Range Slicing 

Name = "Python is a Programming Language"
print(Name[0:5])

print(Name[6:12])


print(Name[:2])  # by default starting from zero


print(Name[2:]) # till the end

print(Name[::2]) # selecting every second elements


print(Name[::3]) # selecting every gapp of 3rd elements

print(Name[0:6:2]) # SELECTING second element in range of 0 to 6





# In[23]:


#Concatenate of Strings

message = 'Hello , World!'
ques = 'How many peoples are there in this meeting?'

Statement = message+ques
print(Statement)




# In[24]:


# printing the string n times (n = 1,2,3,4,5,7,9,....)
message = 'Hello , World!'
print(4*message)


# #Escape Sequences

# In[27]:


print("Hello World \n How many peoples are there in this meeting? ")


# In[30]:


print("Hello World \\ How many peoples are there in this meeting? ")


# In[35]:


#STRING OPERATIONS 

a = "hello python"

print("Using Upper Function we got our value :" , a.upper()) # to convert into upper case

print("Using lower Function we got our value :" , a.lower()) # to Convert into Lower Case

print("Using title  Function we got our value :" , a.title()) # to Capitalize the first Character of the String

print("The replacable string we have :" , a.replace('hello' , 'Hi'))  # to replace the string\


print("I've to find py at position nos " , a.find('py'))


# In[37]:


text = "Data analysis is the process of collecting, modeling, and analyzing data  using various statistical and logical methods and techniques. Businesses rely on analytics processes and tools to extract insights that support strategic and operational decision-making"

print(text.casefold()) # It will return all string which is in lower Case

print(text.count('the')) # it will count  the occurences of the strings inside the text


# In[ ]:




