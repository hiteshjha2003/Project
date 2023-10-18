#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
List :--
It is a collection of items or elements of different datatypes

The elements  or items in a list can be accessed by their position i.e indices.
The index position always start from 0 and  ends with n-1 (n-1= last element-1)

List is mutable it means  we can change the values of the list


"""


# Different types of list:
list1 = [] # empty list

list2 = [1 ,2 , 3 , 4, 5 , 6] # integer list

list3 = ['!' , '@' , '#'  , '$' , '%' , '^' , '&' ,'*' , '(' ,')'  , '4' , 'h' , 'A'] #character list

list4 = ["Hitesh" , "Aryaditya" ,"Suman" ,"Shubh" ,"Gaurav"] # String list

list5 = [3.14,5.36,546.65,155.20,1.00] # float list

list6 = [True , False] # boolean list

list7 = [' '  , 1 , 'a' , 'A' , '@' ,"Aryaditya", 'Suman' ,3.14 , True] #Dynamic list or Mixed list or Special List

nested_list = [[1,2,3,4,5,6] ,
               ['H' ,'I' ,'T' ,'E'] , 
               [3.14,6.312,56.32,58.36] ,
               ["Aryaditya"  , "Suman" , "Shubh" ,"Gaurav"]]


# In[8]:


a = [10 ,20 , 30]
print(a)





# In[19]:


#List Operations:- Updating the list

list1 = [10,20,30,40,50]
print(list1)

list1[0] = 60 #changing the first index
print(list1)


list1[4] = 100 #replacing the last element of the list with indexes
print(list1)


# without using the indexes  I want to add the elements at the end of the list
#append():-- add the elements at the end of the list. It can append Single item 

list1 = [10,20,30,40,50]
res = list1.append(60)
print(list1)

# extend() :- which will extend the list by appending the items . It can append multiple items


list2 = [10,20,30,40,50]
list2.extend([60,70,80,90,100])
print(list2)


#insert():-  on desired location  we can put our values
list3 = [1,2,3,5,6]
list3.insert(3 , 4)
print(list3)



# In[28]:


cnt = 0
while  cnt <3:
   
    cnt = cnt+1
else:
    print('Inside else')


# In[33]:


total = 0
nos = int(input("Enter the nos"))
while nos!=0:
    total+=nos
    nos = int(input("Enter a nos"))
print('total = ' , total)



# In[ ]:




