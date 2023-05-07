# -*- coding: utf-8 -*-
"""
Created on Sun May  7 12:59:47 2023

@author: HNS
"""

# Load Data Function by Ali
import pandas as pd
import glob

def upload_files():
    folder_path = input('Enter path to the folder where the files are located: ')
    file_list = glob.glob(folder_path + "/*.csv")

    data_frames = []

    for filename in file_list:
        df = pd.read_csv(filename, index_col=None, header=0)
        data_frames.append(df)

    combined_df = pd.concat(data_frames, axis=0, ignore_index=True)
    
    combined_df.drop_duplicates(inplace=True)
    
    return combined_df

# Clean Data Function by Usman------------------------------------------------------------------------------------------------------------------------

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


# Statistical Anaylysis by Faraz ------------------------------------------------------------------------------------------------------------------------

#import pandas as pd  ##ALREADY IMPORTED WHILE UPLOADING DATA##

# Convert into float

df = pd.read_csv(r"C:\Users\User\Downloads\Book1.csv")
df['discount_price'] = df['discount_price'].str.replace('₹', '').str.replace(',', '').astype(float)
df['actual_price'] = df['actual_price'].str.replace('₹', '').str.replace(',', '').astype(float)


##### Descriptive Statistics


# Shape of Dataset

def shapeDf(dataset):
    return dataset.shape

shape = shapeDf(df)
print(shape)


# Description of Dataset

def describeDf(dataset):
    return dataset.describe()

describe = describeDf(df)
print(describe)



def describeDf(dataset):
    return dataset.describe(include=['object'])

describe = describeDf(df)
print(describe)



def describeDf(dataset):
    return dataset.describe(include='all')

describe = describeDf(df)
print(describe)



# Info of Dataset

def infoDf(dataset):
    return dataset.info()


info = infoDf(df)
print(info)


# Sum of Dataframe 

def sumDf(dataset):
    return dataset.sum()

sum = sumDf(df)
print(sum)


# Standard Deviation of Dataframe 

def stdDf(dataset):
    return dataset.std()

std_dev = stdDf(df)
print(std_dev)


# Median of Dataframe 

def medDf(dataset):
    return dataset.median()

median = medDf(df)
print(median)



# Mode of Dataframe 

def modeDf(dataset):
    return dataset.mode()

mode = modeDf(df)
print(mode)


# Min of Dataframe 

def minDf(dataset):
    return dataset.min()

min = minDf(df)
print(min)


# Max of Dataframe 

def maxDf(dataset):
    return dataset.max()

max = maxDf(df)
print(max)



# Mode of Dataframe 

def modeDf(dataset):
    return dataset.mode()

mode = modeDf(df)
print(mode)


# Mode of Dataframe 

def modeDf(dataset):
    return dataset.mode()

mode = modeDf(df)
print(mode)




##### Data Visualization 



import matplotlib.pyplot as plt
import seaborn as sb


## Product Rating Histogram


def ratings_histogram(data):
    sb.histplot(data=df, x='ratings', bins=5)
    plt.title('Product Ratings Histogram')
    plt.xlabel('Ratings')
    plt.ylabel('Frequency')
    plt.show()

ratings_histogram(df)



# Relationship between actual price and ratings


def ratings_scatterplot_actual(data):
    sb.scatterplot(data=df, x='actual_price', y='ratings')
    plt.title('Actual Price vs. Ratings')
    plt.xlabel('Actual Price')
    plt.ylabel('Ratings')
    plt.show()

ratings_scatterplot_actual(df)



# Relationship between discount price and ratings


def ratings_scatterplot_discount(data):
    sb.scatterplot(data=df, x='discount_price', y='ratings')
    plt.title('Discount Price vs. Ratings')
    plt.xlabel('Discount Price')
    plt.ylabel('Ratings')
    plt.show()

ratings_scatterplot_discount(df)



# Box plot of actual price by sub category

def actualPrice_BySubCategory_boxplot(data):
    sb.boxplot(data=df, x='sub_category', y='actual_price')
    plt.title('Actual Price by Sub Category')
    plt.xlabel('Sub Category')
    plt.ylabel('Actual Price')
    plt.show()

actualPrice_BySubCategory_boxplot(df)



# Box plot of discount price by sub category

def discountPrice_BySubCategory_boxplot(data):
    sb.boxplot(data=df, x='sub_category', y='discount_price')
    plt.title('Discount Price by Sub Category')
    plt.xlabel('Sub Category')
    plt.ylabel('Discount Price')
    plt.show()

discountPrice_BySubCategory_boxplot(df)



# Box plot of actual price by main category

def actualPrice_ByMainCategory_boxplot(data):
    sb.boxplot(data=df, x='main_category', y='actual_price')
    plt.title('Actual Price by Main Category')
    plt.xlabel('Main Category')
    plt.ylabel('Actual Price')
    plt.show()

actualPrice_ByMainCategory_boxplot(df)



# Box plot of discount price by main category

def discountPrice_ByMainCategory_boxplot(data):
    sb.boxplot(data=df, x='main_category', y='discount_price')
    plt.title('Discount Price by Main Category')
    plt.xlabel('Main Category')
    plt.ylabel('Discount Price')
    plt.show()

discountPrice_ByMainCategory_boxplot(df)

# KPIs by Hammad ------------------------------------------------------------------------------------------------------------------------
 
# Visualizations by Hassan ------------------------------------------------------------------------------------------------------------------------

# Program Execution ------------------------------------------------------------------------------------------------------------------------

folder_path = input("Enter Folder Path")
df = load_data(folder_path)
df = clean_data(df)
statistical_analysis(df)
kpis(df)
visualization(df)

print("End of Program")




