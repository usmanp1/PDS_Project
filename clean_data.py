#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import glob


# In[2]:


def load_data(data_Folder):
    path = (data_Folder + "/*.csv")
    all_files = glob.glob(path)

    dfs = []
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        dfs.append(df)

    # Concatenate all data frames into a single data frame
    merged = pd.concat(dfs, axis=0, ignore_index=True)
    
    return merged


# In[3]:


merged_df = load_data('C:/Users/USMAN/Desktop/KSBL/PDS/term_assignment/')


# In[4]:


merged_df


# In[5]:


def clean_data(merged_df):
    
    
    ## Removing the unneccesary columns of image, link, and unnamed: 0
    merged_df = merged_df.drop(['image','link','Unnamed: 0'],axis=1)
    

    ##Convert 'Ratings' column to numeric
    merged_df['ratings'] = pd.to_numeric(merged_df['ratings'], errors='coerce')
    
    
    ## Convert discount price column to float
    merged_df['discount_price'] = merged_df['discount_price'].str.replace(',', '').str.replace('₹', '').astype(float)

    # Calculate mean separately from each unique value of the corresponding column
    merged_df['discount_price'] = merged_df.groupby(merged_df['discount_price'].fillna('NaN'))['discount_price'].transform(lambda x: x.fillna(x.mean()))
    
    ## Convert No. Of Ratings column to numeric
    merged_df['no_of_ratings'] = pd.to_numeric(merged_df['no_of_ratings'], errors='coerce')

    
    ## Remove currency mark and comma from Actual Price column and convert it to float
    merged_df['actual_price'] = merged_df['actual_price'].str.replace(',', '').str.replace('₹', '').astype(float)

    #Calculate mean separately from each unique value of the corresponding column
    merged_df['actual_price'] = merged_df.groupby(merged_df['actual_price'].fillna('NaN'))['actual_price'].transform(lambda x: x.fillna(x.mean()))

    ## Replace all the null values in RATINGS column from the mean of coresponding Sub_Category 
    merged_df['ratings'] = merged_df.groupby('sub_category')['ratings'].transform(lambda x: x.fillna(x.mean()))
    
    ## replace all the null values in No_Of_RATINGS column from the mean of coresponding Sub_Category
    merged_df['no_of_ratings'] = merged_df.groupby('sub_category')['no_of_ratings'].transform(lambda x: x.fillna(x.mean()))
    
    ## Round 3 column such that the values before decomal does not change
    cols_to_round = ['no_of_ratings', 'discount_price', 'actual_price']
    merged_df[cols_to_round] = merged_df[cols_to_round].round(0)

    ## Change the name of the column Discount Price
    merged_df = merged_df.rename(columns={'discount_price': 'discount_price (Rs. )'})

    ## Change the name of the column Actual Price
    merged_df = merged_df.rename(columns={'actual_price': 'actual_price (Rs. )'})

    ## Replace Nan Values in Discount price Column with the mean of each sub category
    merged_df['discount_price (Rs. )'] = merged_df.groupby('sub_category')['discount_price (Rs. )'].transform(lambda x: x.fillna(x.mean()))

    ## There were some rows left in Actual price column with Nan Value, since they were not in large numbers, so we just dropped them
    merged_df.dropna(inplace=True)
    
    return merged_df


# In[6]:


clean_df = clean_data(merged_df)


# In[7]:


clean_df


# In[31]:


########## YOU HAVE YOUR CLEAN DATA #################


# In[ ]:

print("testing")

