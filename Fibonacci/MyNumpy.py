#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
np.ones(shape=3)


# In[4]:


np.ones(shape=(2, 3)) # dimension 


# In[5]:


np.ones(shape=(2, 3, 3))


# In[6]:


a = np.ones((2, 2))
a


# In[7]:


a[1, 1] = 18
a


# In[8]:


np.sctypes


# In[9]:


a = np.array([1, 100, 110], dtype=np.int8)
a


# In[10]:


a.dtype


# In[11]:


a.itemsize


# In[12]:


a.nbytes


# In[19]:


np.array([1, 4.5, 128], dtype=np.int8)    #int8 = -128 to 127


# In[20]:


a = np.array([1, 2, np.nan])
a.dtype


# In[21]:


np.sctypes['others']


# In[22]:


a = np.array(['spam', 'beans'], dtype=np.str)
a


# In[24]:


a = np.array(['spam', 'beans'], dtype=(np.str,2))
a


# In[25]:


a = np.random.randint(1, 10, size=(3, 3))
a


# In[26]:


a[1:, 2:]     # Slicing


# In[27]:


b = a[1:, :2]
b


# In[29]:


a = np.random.randint(1, 10, size=(4, 4))
a


# In[30]:


b = a.reshape(8, 2)    # Reshaping
b


# In[31]:


mars = np.random.randint(-5, 20, size=31)
mars


# In[32]:


mars > 0


# In[33]:


mars == 0


# In[34]:


np.sum(mars > 0)


# In[35]:


np.any(mars == 20)


# In[36]:


np.all(mars > 0)


# In[37]:


jours_mars = np.arange(1, mars.size + 1, dtype=np.int8)
jours_mars


# In[39]:


np.sum((mars > 10) & (jours_mars >= 15))


# In[40]:


mars[mars > 10]    # indexation


# In[41]:


mars[(mars > 10) & (jours_mars >= 15)]


# In[43]:


moy = np.mean(mars[mars > 0])
mars[mars < 0] = moy
mars


# In[44]:


pays = np.array(['fr', 'uk', 'cn'])
pays[[0, 0, 1, 2, 0]]


# In[2]:


import numpy as np
a = np.arange(1, 10).reshape(3, 3)
a


# In[3]:


np.sum(a)


# In[4]:


np.sum(a, axis=0)    # somme de la colonne 


# In[5]:


np.sum(a, axis=1)    # somme de la ligne


# In[6]:


a = np.arange(1, 10, dtype = np.float64).reshape(3, 3)
a


# In[7]:


a[1, 1] = np.nan
a


# In[8]:


np.mean(a)


# In[9]:


np.nanmean(a)    # ignore nan


# In[ ]:




