#!/usr/bin/env python
# coding: utf-8

# In[137]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[138]:


s = pd.read_csv(r'C:\Users\admin\Music\imarticus python\customer_shopping_data (1).csv')


# In[139]:


s.head()


# In[140]:


s.isnull().sum()[s.isnull().sum() > 0]


# In[141]:


s.groupby('quantity').price.mean()


# In[142]:


df3 = pd.DataFrame(s.shopping_mall.value_counts())


# In[143]:


df3


# In[144]:


df3.columns = ['count_of_customers']


# In[145]:


plt.figure(figsize = (8,8))
plt.pie(df3.count_of_customers, labels = df3.index,autopct='%1.0f%%')
plt.title('Number of customers from shopping mall');

#The pie chart shows the percentage of customers from different shopping malls.
#The mall with the highest number of customers is Kanyon, with 20% of the total customers.
#The mall with the second highest number of customers is Mall of Istanbul, with also 20%.
#The rest of the malls have significantly fewer customers, with each accounting for less than 10% of the total.


# In[146]:


s.category.value_counts()


# In[147]:


df4 = pd.DataFrame(s.category.value_counts())


# In[148]:


df4


# In[149]:


df4.columns = ['count_of_categories']


# In[150]:


plt.figure(figsize = (8,8))
plt.pie(df4.count_of_categories, labels = df4.index,autopct='%1.0f%%',explode = (.07,.0,.0,.0,.0,.0,.0,.0))
plt.title('number of shoppings by categories');

#This pie chart shows the percentage of each category of goods sold by a company.
#The company sells the most clothing, at 35%, followed by cosmetics and food and beverage, each at 15%.
#The next most popular items are toys and shoes, each at 10%.
#After that, the company sells 5% books, 5% technology, and 5% souvenirs.


# In[151]:


plt.figure(figsize=(10, 6))
df4.plot(kind='bar' , color = 'red')
plt.grid()
plt.xlabel('categories')
plt.ylabel('counts of customers')
plt.title('number of shoppings by categories')
plt.show()

#The bar graph shows the number of shopping by categories.
#Clothing is the most popular category with over 35,000 shoppers.
#Cosmetics and Food & Beverage are the second and third most popular categories with around 15,000 shoppers each.
#Toys, Shoes, and Souvenir follow with around 10,000, 5,000, and 5,000 shoppers respectively.
#Technology and Books have the lowest number of shoppers with around 5,000 each.


# In[152]:


plt.figure(figsize=(10,6))
sns.barplot(x= df4.index ,y =  df4.count_of_categories)
plt.xticks(rotation = 90);

#The bar plot graph in seaborn library shows the number of shopping by categories.
#Clothing is the most popular category with over 35,000 shoppers.
#Cosmetics and Food & Beverage are the second and third most popular categories with around 15,000 shoppers each.
#Toys, Shoes, and Souvenir follow with around 10,000, 5,000, and 5,000 shoppers respectively.
#Technology and Books have the lowest number of shoppers with around 5,000 each.


# In[153]:


sns.countplot(x = 'shopping_mall' , data = s , order = s['shopping_mall'].value_counts().index)
plt.xticks(rotation = 90)
plt.ylabel('count of customers')
plt.title('Number of customers from shopping mall');

#graph shows number of customers visited for shopping mall
#The bar graph shows the number of customers from different shopping malls.
#Mall of Istanbul has the highest number of customers followed by Kanyon.
#Metrocity is the third highest. 
#The number of customers decreases as we move to the right. 
#The mall with the least number of customers is Emaar Square Mall.


# In[154]:


sns.countplot(x = 'shopping_mall' , data = s , order = s['shopping_mall'].value_counts().index,hue = 'gender')
plt.xticks(rotation = 90)
plt.ylabel('count of customers')
plt.title('count of male and female in each mall');
#by this graph female do more shopping as compare to male in each mall 


# In[155]:


plt.figure(figsize = (15,10))
sns.countplot(x = 'shopping_mall' , data = s , order = s['shopping_mall'].value_counts().index,hue = 'category')
plt.xticks(rotation = 90)
plt.ylabel('count of cust')
plt.title('count of categories in each mall');
#graph shows that 70 to 80 percent of peoples go shopping malll for clothing


# In[156]:


df5 = pd.DataFrame(s.groupby('category').price.sum())


# In[157]:


df5 = df5.sort_values('price',ascending = False)


# In[158]:


df5


# In[159]:


df5.columns = ['price_of_cat']


# In[160]:


plt.figure(figsize = (8,8))
plt.pie(df5.price_of_cat, labels = df5.index,autopct='%1.0f%%', explode = (.07,.02,.02,.07,.02,.10,.15,.30))
plt.title('Total amount of sales per categories');
#total amount of sales per categories


# In[161]:


df5 = pd.DataFrame(s.groupby('category').price.sum())
df5 = df5.sort_values('price',ascending = False)
df5


# In[162]:


df5.price[0:4]


# In[163]:


df5.index[0:4]


# In[164]:


plt.figure(figsize = (8,8))
plt.pie(df5.price[0:4], labels = df5.index[0:4],autopct='%1.0f%%')
plt.title('Total amount of sales per categories');
#The pie chart shows Top 4 Total amount of sales per categories 


# In[165]:


plt.figure(figsize = (8,8))
plt.pie(df5.price[4:], labels = df5.index[4:],autopct='%1.0f%%')
plt.title('Total amount of sales per categories');
#The pie chart shows bottom 4 Total amount of sales per categories 


# In[166]:


plt.figure(figsize=(10,6))
sns.barplot(x= df5.index[0:4] ,y =  df5.price[0:4])
plt.xticks(rotation = 90)
plt.title('Total amount of sales per categories');


# In[167]:


plt.figure(figsize=(10,6))
sns.barplot(x= df5.index[4:] ,y =  df5.price[4:])
plt.xticks(rotation = 90)
plt.title('Total amount of sales per categories');


# In[168]:


plt.figure(figsize=(10,6))
sns.barplot(x= df5.index ,y =  df5.price)
plt.xticks(rotation = 90)
plt.title('Total amount of sales per categories');


# In[169]:


df5['price_in_million'] = df5.price / 1000000


# In[170]:


df5
#Here we make a dataframe and convert a price in million for better understandings


# In[171]:


plt.figure(figsize=(10,6))
sns.barplot(x= df5.index ,y =  df5.price_in_million)
plt.grid()
plt.xticks(rotation = 90)
plt.title('Total amount of sales per categories in millions USD');


# In[172]:


ist = s[s.shopping_mall == 'Mall of Istanbul']
ist.head()


# In[173]:


sns.boxplot(x = 'category' , y = 'price',data = ist)
plt.xticks(rotation = 90)
plt.title('price range for each category');

#The box plot shows the distribution of prices for different product categories.
#Technology has the highest median price, followed by Shoes.
#Clothing has the third highest median price, while Cosmetics, Toys, Food & Beverage, Books, 
#and Souvenir have much lower median prices.
#The price range for Technology is very wide, with some items costing over 5000.
#Shoes and Clothing have a moderate price range, while the rest of the categories have a narrower price range.
#Food & Beverage, Books, and Souvenir have a very low price range, with most items costing under 100.


# In[174]:


total_revenue_by_mall = s.groupby('shopping_mall')['price'].sum().round()


# In[175]:


plt.figure(figsize=(10, 6))
total_revenue_by_mall.plot(kind='bar' , color = 'red')
plt.grid()
plt.xlabel('Shopping Mall')
plt.ylabel('Total Revenue in Lakhs')
plt.title('Total Revenue by Shopping Mall');




# In[176]:


p_cat = s.groupby('payment_method')['invoice_no'].count()


# In[177]:


plt.figure(figsize=(8, 8))
p_cat.plot(kind='pie', autopct='%1.0f%%' , explode = (.03,.02,.01))
plt.title('Total Purchases by Payment Method')
plt.show()

#total purchases by different payment methods


# In[178]:


plt.figure(figsize=(10, 6))
s.groupby('category')['quantity'].sum().plot(kind='line' ,marker = '*', color = 'lime' )
plt.title('Quantity Sold by Category')
plt.xlabel('Category')
plt.ylabel('Quantity')
plt.grid();


# In[ ]:


#The total spend based on shopping centers shows that Mall of Istanbul, Kanyon,
#and Metrocity are the top-performing locations.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




