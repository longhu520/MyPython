#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
s = pd.Series([20, 30, 40, 50], 
              index=['eve', 'bill', 'liz', 'bob'])
s


# In[2]:


s.values


# In[3]:


s.index


# In[4]:


s.loc['eve']


# In[5]:


animaux = ['chien', 'chat', 'chat', 'chien', 'poisson']
proprio = ['eve', 'bob', 'eve', 'bill', 'liz']

s= pd.Series(animaux, index=proprio)
s


# In[15]:


s.sort_index()


# In[19]:





# In[21]:


s = s.sort_index()
s.loc['eve':'liz']


# In[22]:


s


# In[23]:


s.iloc[0]


# In[24]:


s.iloc[4]


# In[26]:


s.iloc[0:3]


# In[27]:


s.loc[(s == 'chien') | (s == 'poisson')]


# In[29]:


s.loc[(s == 'chien') | (s == 'poisson')] = 'autre'
s


# In[32]:


s1 = pd.Series([1, 2, 3], index=list('abc'))
s2 = pd.Series([5, 6, 7], index=list('acd'))
s1


# In[33]:


s2


# In[34]:


s1 + s2 


# In[36]:


s1.add(s2, fill_value=50)


# In[19]:


import pandas as pd
import numpy as np
prenoms = ['liz', 'bob', 'bill', 'eve']
age = pd.Series([25, 30, 35, 40], index=prenoms)
taille = pd.Series([160, 175, 170, 180], index=prenoms)
sexe = pd.Series(list('fhhf'), index=prenoms)
df = pd.DataFrame({'age': age, 
                   'taille': taille, 
                   'sexe': sexe})
df


# In[2]:


df.index


# In[3]:


df.columns


# In[4]:


df.values


# In[5]:


df.head(2)


# In[6]:


df.tail(2)


# In[7]:


df.describe()


# In[8]:


df.loc['liz']


# In[9]:


df.loc['liz', 'age']


# In[10]:


df.loc[:, 'taille']


# In[11]:


df.loc[df.loc[:, 'age']<32]


# In[12]:


df = df.reset_index()
df


# In[13]:


df = df.rename(columns={'index': 'prenom'})
df


# In[14]:


df.set_index('age')


# In[16]:


df = pd.DataFrame({'age': age, 
                   'taille': taille, 
                   'sexe': sexe})
df


# In[18]:


df = df.reset_index().rename(columns={'index':'nom'}).set_index('age')
df


# In[21]:


df1 = pd.DataFrame(np.ones((2, 2)),
                  index=list('ab'),
                  columns=list('xy'))
df1


# In[22]:


df2 = pd.DataFrame(np.ones((2, 2)),
                  index=list('ac'),
                  columns=list('xz'))
df2


# In[23]:


df1 + df2


# In[27]:


df3 = df1.add(df2, fill_value = 0)
df3


# In[28]:


df3.fillna(-1)


# In[29]:


df3.dropna()


# In[5]:


import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.random.randint(1, 10, size=(2, 2)),
                  columns=list('ab'),
                  index=list('xy'))
df2 = pd.DataFrame(np.random.randint(1, 10, size=(2, 2)),
                  columns=list('ab'),
                  index=list('zt'))


# In[6]:


df1


# In[7]:


df2


# In[8]:


pd.concat([df1, df2])


# In[9]:


df1 = pd.DataFrame(np.random.randint(1, 10, size=(2, 2)),
                  columns=list('ab'),
                  index=list('xy'))
df2 = pd.DataFrame(np.random.randint(1, 10, size=(2, 2)),
                  columns=list('cd'),
                  index=list('xy'))


# In[10]:


df1


# In[11]:


df2


# In[12]:


pd.concat([df1, df2], axis=1)


# In[19]:


df1 = pd.DataFrame({'personnel' : ['Bob','Lisa','Sue'],
                   'groupe':['SAF', 'R&D', 'RH']})
df2 = pd.DataFrame({'personnel' : ['Lisa', 'Bob', 'Sue'],
                   'date embauche' : [2004, 2008, 2014]})


# In[20]:


df1


# In[21]:


df2


# In[22]:


pd.merge(df1, df2)


# In[23]:


import pandas as pd
import numpy as np
import seaborn as sns

ti = sns.load_dataset('titanic').loc[:,['survived', 'sex', 
                                       'class']]
ti.head()


# In[24]:


ti.shape


# In[25]:


ti.loc[:, 'survived'].mean()


# In[26]:


ti.loc[ti.loc[:,'class']=='First', 'survived'].mean()


# In[28]:


ti.groupby('class').mean()


# In[30]:


ti.groupby(['class', 'sex']).mean()


# In[31]:


ti.pivot_table('survived',
              aggfunc=np.mean,
              index='class',
              columns='sex')


# In[32]:


np.datetime64('2020-03-27 17:56')


# In[33]:


pd.to_datetime('27 Mar 2020 17h57')


# In[34]:


pd.to_datetime(['27 mar 2020', '27-mar-2020'])


# In[35]:


index = pd.date_range('1 jan 2018', periods=1000, freq='D')
index


# In[36]:


index = pd.date_range('1 jan 2018', periods=1000, freq='43h56t')
index


# In[38]:


s = pd.Series(np.random.randint(100, size=1000), index=index)
s


# In[39]:


s['Dec 2018']


# In[40]:


s.resample('M').mean()


# In[41]:


s.resample('W-WED').mean()   //depuis mercredi chaque semaine


# In[ ]:




