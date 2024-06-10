#!/usr/bin/env python
# coding: utf-8

# # Importing libraries and dataset

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# 

# In[21]:


data=pd.read_csv('C:/Users/gauth/Downloads/heart.csv')


# # Displaying top 10 data for visualizing

# In[22]:


data.head(10)


# # Displaying last 10 data for visualization

# In[23]:


data.tail(10)


# # Finding the shape of dataset

# In[24]:


data.shape


# In[25]:


print("Number of Rows",data.shape[0])
print("Number of Columns",data.shape[1])


# # Getting info of the data like no of rows and columns,data types

# In[26]:


data.info()


# In[27]:


data.isnull()


# # Checking null values in the dataset

# In[28]:


data.isnull().sum()


# # Checking duplicate data and drop them

# In[29]:


data_dup=data.duplicated().any()
print(data_dup)


# In[30]:


data=data.drop_duplicates()


# In[31]:


data.shape


# # Getting overall discriptive statistics about the dataset

# In[32]:


data.describe()


# # Getting correlation of the data

# In[33]:


data.corr()


# # Drawing correlation matrix

# In[34]:


plt.figure(figsize=(17,6))
sns.heatmap(data.corr(),annot=True)


# In[35]:


data.columns


# # No of people having heart disease

# In[36]:


data['target'].value_counts()


# In[47]:


target_counts = data['target'].value_counts()
plt.bar(target_counts.index, target_counts.values, color=['blue', 'orange'])
plt.xticks(sex_counts.index)
plt.title('People having heart problem')
plt.xlabel('target')
plt.ylabel('Count')
plt.show()


# # Finding the count of male and female

# In[37]:


data['sex'].value_counts()


# In[42]:


sex_counts = data['sex'].value_counts()
plt.bar(sex_counts.index, sex_counts.values, color=['blue', 'orange'])
plt.xticks(sex_counts.index, labels=['Male', 'Female'])
plt.title('Count of Males and Females')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.show()


# # Gender distribution

# In[27]:


sns.countplot(x='sex',hue="target",data=data)
plt.xticks([1,0],['male','female'])
plt.legend(labels=['no disease','disease'])


# # Age distribution

# In[30]:


sns.distplot(data['age'],bins=20)
plt.show()


# In[33]:


data.columns


# # Checking the count of cp

# In[46]:


cp_counts = data['cp'].value_counts()
plt.bar(cp_counts.index, cp_counts.values, color=['blue', 'orange', 'red', 'green'])
plt.xticks(cp_counts.index)
plt.title('Count of cp')
plt.xlabel('Cp_values')
plt.ylabel('Count')
plt.show()


# # cp vs target

# In[32]:


sns.countplot(x="cp",hue="target",data=data)


# # fbs vs target

# In[38]:


sns.countplot(x="fbs",hue="target",data=data)
plt.xticks([1,0],['male','female'])
plt.legend(labels=['no disease','disease'])


# # Checking rbp distribution

# In[39]:


data['trestbps'].hist()


# In[46]:


data.columns


# # Comparing rbp vs sex

# In[50]:


g=sns.FacetGrid(data,hue="sex")
g.map(sns.kdeplot,'trestbps',shade=True)
plt.legend(labels=['male','female'])


# In[51]:


data.columns


# # Distribution of serum chol

# In[52]:


data['chol'].hist()


# In[53]:


data.columns


# # Plot continuous variables

# In[55]:


cate_val=[]
cont_val=[]
for column in data.columns:
    if data[column].nunique() <=10:
        cate_val.append(column)
    else:
        cont_val.append(column)


# In[56]:


cate_val


# In[57]:


cont_val


# In[60]:


data.hist(cont_val,figsize=(15,6))
plt.tight_layout()
plt.show()


# In[ ]:




