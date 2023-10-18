#!/usr/bin/env python
# coding: utf-8

# In[3]:


from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt



# In[7]:


a = np.random.randint(100 , size =(40))
b = np.random.randint(70,size =(40))
c = np.random.randint(50 , size = (40))



# In[9]:


figure = plt.figure(figsize=(10,7))
ax = plt.axes(projection ="3d")
ax.scatter3D(a , b, c , color = "red")
plt.title("Simple 3D Visualization")
plt.show()



# In[13]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





# In[15]:


normal = np.random.normal(0 , 1,  1000)
quartiles = pd.DataFrame(normal).quantile([0.25 , 0.5 , 0.75 ,1])[0]

fig , axs = plt.subplots(nrows =2)
fig.set_size_inches(14 , 8)

plot1 = sns.boxplot(normal , ax = axs[0])
plot1.set(xlim=(-4,4))


plot2 = sns.distplot(normal , ax = axs[1])
plot2.set(xlim = (-4,4))


plt.axvline(np.median(normal) , color ='r' , linestyle ='dashed' , linewidth =2)

for i  , q , in enumerate(quartiles):
    plt.axvline(q , color='g' , linestyle='dotted' , linewidth=2)


# In[ ]:




