#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Taking the input from User

#To take input from the user :-


names = input("Enter your Name")  # To take string values




numbers = int(input("Enter an integer"))  #To take integer values
print("The integer is" , number)



decimal = float(input("Enter the decimals")) #to take Float or decimal values
print("the decimal nos is" , decimal)





# In[2]:


# Program to find Square root of a nos 
x = int(input("Enter an integer number:"))
result=x**0.5
print("The Square root = " , int(result))


# In[4]:


# Program to find the area of rectangle
l = float(input("Enter the length of rectangle:"))
b = float(input("Enter the breadth of rectangle:"))
area = l*b
print("The area of rectangle is :" , area)




# In[7]:


#Program to calculate area and Parameter of the Square
side = int(input("Enter the side of Square"))
area = side**2
side2 = int(input("Enter the perimeter of Square"))
perimeter = 4*side2
print("The Area of Square is : " , area)
print("The Perimeter of square is :" , perimeter)



# In[8]:


#Program to calculate the Surface Volume and area of Cylinder

pi = 3.14
height = float(input("Enter the height of cylinder"))
radius = float(input("Enter the radius of the cylinder"))

volume = pi*radius*radius*height
print("The volume is :" , volume)

surface_area = ((2*pi*radius)*height) + ((pi*radius**2)*2)
print("Surface area of cylinder:" , surface_area)


# In[9]:


#Program to Swap the values of two Variables(Imp)

nos1 = int(input("Enter the first value"))
nos2  = int(input("Enter the second value"))

print("Nos before swapping")
print("number 1 is " , nos1)
print("number 2 is " , nos2)

temp = nos1
nos1 = nos2
nos2 = temp

print("Nos after swapping")

print("number 1 is " , nos1)
print("number 2 is " , nos2)





# In[11]:


#Swapping the value of two values without using third variables
x = 4
y = 7

x ,y = y, x
print("the value of x:" , x , "The value of y: " , y)


# In[14]:


#Conditional Statements:--
"""
Syntax of if:
if(condition):
    statements
    
    

"""
i = 10
if(i<15):
    print("i is less then 15" )
    

#print("Outside the if statements")




# In[1]:


# I want tp find absolute value of any nos

x = int(input("Enter an negative integer nos"))
y = x
if(x<0):
    x = -x
    print('The Absolute value of ' ,y , '=' , x )
    
    


# In[4]:


i = int(input("Enter the value"))
if(i<15):
    print("i is less then 15" )
else:
    print("i is greater then 15")


# In[6]:


x = int(input("Enter an negative integer nos"))
y = x
if(x<0):
    x = -x
    print('The Absolute value of ' ,y , '=' , x )
else:
    print("You have entered positive integer")
    


# In[10]:


# To find the whether a nos is even or odd

nos = int(input("Enter any nos"))
if(nos%2)==0:
    print(nos , "is an  even nos")
else:
    print(nos , "is an odd nos")
    
    
    


# In[20]:


#To check if the input year is leap year or not :--
year = int(input("Enter the year to be checked"))
if(year%4 ==0 and year%100 !=0 or year%400==0):
    print("It is a leap year")
else:
    print("It is not a leap year")


# In[22]:


year = int(input("Enter the year to be checked"))
if(year%4 == 0 ):
    print("It is a leap year")
elif(year%100!=0):
    print("100 is not a century leap year")
elif(year%400==0):
    print("400 is  starting century leap year")
else:
    print("It is not a leap year")


# In[25]:


# To check the given nos is positive  , negative or zero

num = float(input("Enter the nos:"))
if(num>0):
    print("It is positive nos")
elif(num==0):
    print("It is zero")
else:
    print("It is negative nos")
    


# In[2]:


num = float(input("Enter the nos:"))
if(num>=0):
    if(num>0):
        print("Positive nos")
    else:
        print("Zero")
else:
    print("negative nos")


# In[8]:


#To find the largest of the three nos

nos1 = int(input("Enter first nos"))
nos2 = int(input("Enter second nos"))
nos3 = int(input("Enter third nos"))

if(nos1>nos2 and nos1>nos3):
    print("{0} is largest".format(nos1))
elif(nos2>nos1 and nos2>nos3):
    print("{0} is the largest".format(nos2))
else:
    print(nos3 , "is the largest ")
    print("{0} is the largest".format(nos3))
    
    


# In[1]:


#Looping:
"""
while(condition):
    expression
    
1 - initialization 
2 - condition
3 - increment / decrement   

"""
i = 1 # initialization 
while i<=15:  # condition
    print(i)
    i = i+1    #increment
    
    




# In[2]:


# while with else statements:-

cnt = 0
while cnt <3:
    print("Inside loop")
    cnt = cnt+1
else:
    print("Inside else statements")


# In[10]:


cnt = 0
while cnt <5:
    if cnt == 4:
        break
        
        print("Inside the loop")
    cnt = cnt+1
else:
    print("Inside else statements")


# In[5]:


i = 1
while i<=10:
    print('8*', (i) , '=' , 8*i)
    if i>=4:
        break
        
    i+=1


# In[6]:


#to print the odd nos from 1 to 10

nos =0
while nos<=10:
    nos+=1
    if (nos%2)==0:
        continue
    print(nos)
    
    


# In[ ]:




