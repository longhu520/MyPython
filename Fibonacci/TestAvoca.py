#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
df = pd.read_csv("dataset/avocado.csv")
df['Date'] = pd.to_datetime(df["Date"])
albany_df = df[df['region'] == "Albany"]
albany_df.set_index("Date", inplace=True)
# print(albany_df)
albany_df["AveragePrice"].plot()


# In[7]:


albany_df["AveragePrice"].rolling(25).mean().plot()


# In[10]:


albany_df.index
albany_df.sort_index(inplace=True)
albany_df["AveragePrice"].rolling(25).mean().plot()


# In[21]:


# print(albany_df.head(3))
albany_df["price25m"] = albany_df["AveragePrice"].rolling(25).mean()
# print(albany_df.head(3))
print(albany_df.tail(3))


# In[22]:


print(albany_df.dropna().head(3))


# In[27]:


albany_df = df.copy()[df['region'] == "Albany"]
albany_df.set_index("Date", inplace=True)
albany_df["price25mean"] = albany_df["AveragePrice"].rolling(25).mean()


# In[32]:


# print(df["region"].values.tolist())
print(set(df["region"].values.tolist()))


# In[33]:


print(df["region"].unique())


# In[39]:


graphe_df = pd.DataFrame()

for region in df["region"].unique()[:16]:
    print(region)
    region_df = df.copy()[df["region"] == region]
    region_df.set_index("Date", inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f"{region}_price25mean"] = region_df["AveragePrice"].rolling(25).mean()
    
    if graphe_df.empty:
        graphe_df = region_df[[f"{region}_price25mean"]]
    else:
        graphe_df = graphe_df.join(region_df[f"{region}_price25mean"])
print(graphe_df.tail(3))    


# In[ ]:


df = pd.read_csv("dataset/avocado.csv")
df = df.copy()[df['type'] == 'organic']
df["Date"] = pd.to_datetime(df["Date"])
df.sort_values(by="Date", ascending=True, inplace=True)
print(df.head())


# In[43]:


graphe_df = pd.DataFrame()

for region in df["region"].unique()[:16]:
    print(region)
    region_df = df.copy()[df["region"] == region]
    region_df.set_index("Date", inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f"{region}_price25mean"] = region_df["AveragePrice"].rolling(25).mean()
    
    if graphe_df.empty:
        graphe_df = region_df[[f"{region}_price25mean"]]
    else:
        graphe_df = graphe_df.join(region_df[f"{region}_price25mean"])
print(graphe_df.tail()) 


# In[47]:


graphe_df.plot(figsize=(8,5), legend=False)


# In[ ]:




