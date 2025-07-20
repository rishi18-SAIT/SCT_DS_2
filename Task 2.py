#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data =pd.read_csv("test.csv")


# In[3]:


data.head()


# In[4]:


data.tail()


# In[5]:


data.describe()


# In[6]:


data.info()


# In[7]:


data.isnull().sum()


# In[12]:


data.dropna(subset=["Embarked"],inplace=True)
data["Cabin"].fillna("Unknown",inplace=True)
data["Age"].fillna(data["Age"].mean(),inplace=True)


# In[14]:


data.isnull().sum()


# In[15]:



data.duplicated().sum()


# In[16]:


plt.figure(figsize=(6,3))
sns.histplot(data["Age"],kde=True)
plt.title("Age Distributed")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()


# In[17]:


plt.figure(figsize=(6,3))
sns.countplot(data=data,x="Sex",hue="Sex")
plt.title("Survival by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.legend(title="Survived",loc="upper right")
plt.show()


# In[18]:


plt.figure(figsize=(6,3))
sns.scatterplot(data=data,x="Age",y="Fare", hue="Age")
plt.title("Scatter plot of Age and Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.legend(title="Survived")
plt.show()


# In[ ]:




