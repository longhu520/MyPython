#!/usr/bin/env python
# coding: utf-8

# In[1]:


s = set()
type(s)


# In[2]:


s = {1,2,3, 'a', True}
a = [1, 2, 3, 4, 1, 18, 30, 4, 1]
set(a)


# In[3]:


len(s)


# In[10]:


s.add('alice')
s


# In[12]:


s.update([1,2,3,4,5,6])
s


# In[13]:


a = [1,2,3,4,5,6]
a


# In[14]:


s = set(a)
s


# In[15]:


get_ipython().run_line_magic('timeit', '-n 50 3 in a')


# In[16]:


get_ipython().run_line_magic('timeit', '-n 50 3 in s')


# In[ ]:




