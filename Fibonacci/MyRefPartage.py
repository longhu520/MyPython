#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = [1, 2]
b = a
a[0] = 3
a


# In[3]:


b


# In[5]:


a = [1, 2]
b = a[:]
a[0] = 3
a


# In[6]:


b


# In[7]:


a = [1, [2]]
import copy
b = copy.deepcopy(a)
a[1][0] = 'Spam'
a


# In[8]:


b


# In[ ]:




