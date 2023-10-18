#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Role of Statistics in Analytics Domain:--

Data Exploration:--

Data Cleaning:--

Data transformation:-

Data Visualiaztaion

Find similiarity/Dissimilarity

Model Selection and Evlautaion

Hypothesis Testing

Probability Distribution and Estimations



Types of Statistics:--

Descriptive Statistics:---
    Ways of describing  , presenting, summarizing , and Ogranizing the data either through numerical cals or graphs

Measure of Frequency:--

Measure of Central tendency:---

Mean
Median
Mode



Measure of Dispersion:---

Variance 


Standard Deviation

Range

Quantiles /Quartiles /InterQuartile Range







Inferential Statistics:---


Hypothesis testing---

Any assumption about the parameters of Populations

Two types of hypothesis

1) Null Hypothesis(Ho):---- 
There is   no variation in the outcome , no real effect

Different teaching methods does not affect the students performance 

The vaccine does not  have any effect against the corona virus


2) Alternate Hypothesis (Ha):--- 
There is a variation some real effect in the outcome

Different teaching methods does have significant affect the students performance 

The vaccine does  have any signficant  effect against the corona virus



Whats is the Probability of rejecting the null hypothesis when it istrue (0.05)
p-value
if p<0.05:
    Rejecting null hypothesis
else:
 Accepting null hypothesis
 
 
Type of Erros:--
Type 1 Error:--

When we reject the Null hypo even when it is true

Type 2 Error:--
WHen we accept the Null Hypo even when it is false



important Parameters :--
1) Acceptance Region and Critical region

2) One tailed test and two-tailed test

3) Significance level(Alpha)

5) Calculated probability(p-value)



Parameter Estimation:--

Parametric test :--

One sample
z-test
t-test
chi-Sqaure test



Two Samples:-
Paired-t test




"""


# In[3]:


#Measure of Frequency:--


import pandas as pd

data = {'Group':[1,2,3,4,5,6,8,9,10,11,12,13,14] ,
       'Grade':['A' , 'B' , 'A' , 'B' ,'A+' , 'B+' , 'A' , 'C' , 'B' , 'A' , 'A+' , 'O', 'F' ]}

df = pd.DataFrame(data)

count = df['Grade'].value_counts()

print(count)


# In[5]:


import statistics as st

data = [45,56,58,98,45,25]
print("Mean" , st.mean(data))

print("Median" , st.median(data))

print("Mode " , st.mode(data))


# In[6]:


ranges = max(data) - min(data)
print("Ranges" , ranges)


# In[7]:


print("Standard Deviation" ,st.pstdev(data))


# In[8]:


print("Variance of Data" , st.pvariance(data))


# In[9]:


print("Quantiles of data" , st.quantiles(data))


# In[10]:


q = st.quantiles(data)
print("Interquartile Range" ,q[2]-q[0])


# In[ ]:




