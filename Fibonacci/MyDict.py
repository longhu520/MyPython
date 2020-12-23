#!/usr/bin/env python
# coding: utf-8

# In[1]:


age = {}
type(age)


# In[2]:


age = {'ana' : 35, 'bob' : 38, 'eve' : 30}
age


# In[3]:


del age['bob']
age


# In[4]:


len(age)


# In[5]:


'ana' in age


# In[6]:


'bob' in age


# In[7]:


age.keys()


# In[8]:


age.values()


# In[9]:


age.items()


# In[10]:


for k, v in age.items() :
    print(f"{k} {v}")


# In[11]:





# In[ ]:




