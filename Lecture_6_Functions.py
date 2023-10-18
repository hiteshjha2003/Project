#!/usr/bin/env python
# coding: utf-8

# In[2]:


#FUNCTIONS :---
"""
    It is block of code which is Oraganized , this code can be reusable and it is used to Perform specific task 
    
    Defining a function :--
     1) Without Paramters
        def function_name():
            your statements or code anything which u want to perform
        def function_name(par1 , para2 , para3 , para4......paran):
            your code
            
    Calling the function:----
        function_name()
    
    
    Types of Functions :--
    1) Built-in functions
    2) User-Defined Functions
    
    
    Whenever you are giving the parameters at the definition time then you have to pass argument at the time of Calling
    functions
    
"""
 


# In[26]:


def myrange():
    for i in range(1 , 10):
        print(i)


# In[27]:


print(myrange())


# In[10]:


print(myrange())


# In[11]:


print(myrange())


# In[12]:


print(myrange())


# In[13]:


print(myrange())


# In[18]:


def my_function(name):
    print("Hello "+name)


# In[19]:


my_function("Anhuya")


# In[28]:


#Function Calling:--
# 1) Call a function  that performs a task and has no return value
def my_name():
    print("Coachx")
    
my_name()


# In[30]:


# Call the function with retrun values:-
def my_functions():
    return "Hello Hi Everyone"

my_functions()


# In[32]:


#call a functions with arguments
def avg_nos(x ,y):
    print("Average of " , x , "and " , y , "is " , (x+y)/2)
    
avg_nos(3,4)


# In[33]:


#type conversion :
# 1) Implicit type Conversion
# 2) Explicit type Conversion

val1 = 10
val2 = 10.5
sum1 = val1+val2
print(sum1)


# In[36]:


s= "10101010"
print(type(int(s)))
    


# In[37]:


#Built in functions:---
"""
1) min():--
2) max():--
3) pow():--
4) round():--
5) abs():--
6) cos() , sin() , tan() :-
7) ceil() :--
8) floor() :--
9) exp():--
10) factorial():--

"""


# In[38]:


#Composition functions:--
# E.g we will write a function that takes two points :- the center of circle  ,
#perimeter of circle and this function will computes the area of circle:--

#centerd point is stored in variable xc , yc , and perimetere points i sstored in xp , yp.

#The first step is to find radius

def distance(xc , yc , xp , yp):
    
    
    
def area():
    
    

def area_circle(xc , yx , xp , yp):
    radius = distance(xc , yc , xp , yp)
    result = area(radius)
    return result



# In[ ]:


"""
Paramters:--
    THere are two types of Parameters :
    1) Actual Parameters:--
        
    2) Formal Parameters:--

"""


def cube(x):       #Formal Parameters 
    return x*x*x


res = cube(7)     #Actual Parameters 
print(res)


# In[ ]:


"""
Arguments:---


"""

