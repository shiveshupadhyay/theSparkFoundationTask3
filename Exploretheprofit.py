#!/usr/bin/env python
# coding: utf-8

# # Shivesh Upadhyay

# # Looking at Data

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# In[2]:


dataset = pd.read_csv('SampleSuperstore.csv')
dataset.head()


# In[3]:


dataset.shape


# ##### We now need to look which column  has how many unique value, so that we can see that which column can be looked first to analysis if we can increase the profit. We also look at null values(missing data) if any. 

# In[4]:


dataset.nunique()


# In[5]:


dataset.isnull().sum()


# ##### Now looking at above result we can see that the columns which can be a parameter to identify the profit issues are 'Ship Mode' , 'Segment' , 'city' , 'state', 'region' , 'category' 'sub-category'  and 'discount'.  Out of this some are large in number and some are very less in number, some can directly affect profit and some have indirect affect.   We can see that 'Sub-Category' is best place to start because of following reason. Firstly it directly affect profit because customer buy the product according to their need i.e. 'Sub-Category' and also this has neither too big nor too large number of unique value.

# In[6]:


dataset["Sub-Category"].unique()


# In[7]:


x1 = ['Bookcases', 'Chairs', 'Labels', 'Tables', 'Storage',
       'Furnishings', 'Art', 'Phones', 'Binders', 'Appliances', 'Paper',
       'Accessories', 'Envelopes', 'Fasteners', 'Supplies', 'Machines',
       'Copiers']
for i in x1:
    d5 = dataset[dataset["Sub-Category"] == i]
    print(i + "=", end =" ")
    print(d5["Profit"].sum())


# #### So here we see  three Sub-Categories ('Bookcases', 'Tables' , 'Supplies') are giving loss. Now we know loss area so we can plot profit to get  idea of reason for loss

# In[8]:


x2 = ['Bookcases', 'Tables' , 'Supplies']
for i in x2:
    d = dataset[dataset["Sub-Category"] == i]
    plt.scatter(d["Sub-Category"],d["Profit"])


# #### From above plot we can't find any reason so need deeper  analysis of the dataset for these sub categories. So we as follows

# In[9]:


d1 = dataset[dataset["Sub-Category"].isin(x2)]


# In[10]:


d1.shape


# In[11]:


d1.nunique()


# #### Now for this data we look  effect of other columns by ploting it vs profit

# In[12]:


plt.scatter(d1["Sales"],d1["Profit"])


# In[13]:


plt.scatter(d1["Discount"],d1["Profit"])


# ### From above plot we see that giving discount on these sub- category tends to lower the profit in negative area. So if for these sub- categories if company stops giving discount then loss will changed to profit. This is shown numerically below

# In[14]:


d2 = d1[d1['Discount'] == 0.0]
d2['Profit'].sum()


# In[15]:


for i in x2:
    d = d2[d2["Sub-Category"] == i]
    print(d['Profit'].sum())


# In[16]:


plt.scatter(d1["Quantity"],d1["Profit"])


# In[17]:


plt.scatter(d1["State"],d1["Profit"])


# #### From above plot we see that many of states are giving loss and many are giving profit. But the ratio being around 50-50 , we can draw any practically implementable conclusion and solution from this

# ### Although we can reach out this problem in other ways also and get other ways of increasing profit also but I stop here getting one solution only

# In[38]:


x = dataset['Profit'].sum()
y = dataset[~(dataset['Sub-Category'].isin(x2) & dataset['Discount'] != 0.0)]['Profit'].sum()
print(x, y)
plt.plot(['Before', 'After'], [x,y])
plt.title('Increasing Profit')
plt.show()


# In[ ]:




