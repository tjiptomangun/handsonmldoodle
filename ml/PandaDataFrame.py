
# coding: utf-8

# In[3]:


#Playing with panda

#DataFrame.loc 
#Access a group of rows and columns by label(s) or a boolean array.
#https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.loc.html

import pandas as pd
df = pd.DataFrame([[1, 2], [4, 5], [7, 8]], 
             index=["cobra", "viper", "sidewinder"],
             columns=["max_speed", "shield"])
df


# In[5]:


#Getting values

#Single label. Note this returns the row as a Series.
df.loc['viper']


# In[20]:


#Play some
df.loc[['viper']]


# In[6]:


#List of labels. Note using [[]] returns a DataFrame.
df.loc[['viper', 'sidewinder']]


# In[21]:


#Single label for row and column
df.loc['cobra', 'shield']


# In[25]:


#Slice with labels for row and single label for column.
#As mentioned above, note that both the start and stop of the slice are included.
df.loc['cobra':'viper', 'max_speed']


# In[24]:


df.loc[['cobra','viper'], 'max_speed']


# In[12]:


df.loc[[False, False, True]]


# In[13]:


df.loc[df['shield']>6]


# In[17]:


#Conditional that returns a boolean Series with column labels specified
df.loc[df['shield']>6, ['max_speed']]


# In[19]:


#Callable that returns a boolean Series
df.loc[lambda df: df['shield'] == 8]


# In[26]:


#Setting Values

#Set value for all items matching the list of labels
df.loc[['viper', 'sidewinder'], ['shield']] = 50


# In[27]:


df


# In[28]:


#Set value for an entire row

df.loc['cobra'] = 10


# In[29]:


df


# In[30]:


df.loc['cobra']


# In[32]:


#Set value for an entire column
df.loc[:, 'max_speed']  = 30
df


# In[33]:


df.loc[df['shield'] > 35] = 0

df


# In[ ]:


#Getting values on a DataFrame with an index that has integer labels

