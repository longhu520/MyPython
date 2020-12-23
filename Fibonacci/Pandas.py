#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
df = pd.read_csv("dataset/data.csv")
df.head()


# In[5]:


df["Name"].head()


# In[13]:


fr_df = df[df["Nationality"] == 'France'].head()
fr_df.tail(5)


# In[16]:


fr_df.plot()


# In[ ]:




