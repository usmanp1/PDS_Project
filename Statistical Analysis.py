import pandas as pd

# Convert into float

df = pd.read_csv(r"C:\Users\User\Downloads\Book1.csv")
df['discount_price'] = df['discount_price'].str.replace('₹', '').str.replace(',', '').astype(float)
df['actual_price'] = df['actual_price'].str.replace('₹', '').str.replace(',', '').astype(float)


##### Descriptive Statistics


# Shape of Dataset

# def shapeDf(dataset):
#     return dataset.shape

# shape = shapeDf(df)
# print(shape)


# Description of Dataset

# def describeDf(dataset):
#     return dataset.describe()

# describe = describeDf(df)
# print(describe)



# def describeDf(dataset):
#     return dataset.describe(include=['object'])

# describe = describeDf(df)
# print(describe)



# def describeDf(dataset):
#     return dataset.describe(include='all')

# describe = describeDf(df)
# print(describe)



# Info of Dataset

# def infoDf(dataset):
#     return dataset.info()


# info = infoDf(df)
# print(info)


# Sum of Dataframe 

# def sumDf(dataset):
#     return dataset.sum()

# sum = sumDf(df)
# print(sum)


# Standard Deviation of Dataframe 

# def stdDf(dataset):
#     return dataset.std()

# std_dev = stdDf(df)
# print(std_dev)


# Median of Dataframe 

# def medDf(dataset):
#     return dataset.median()

# median = medDf(df)
# print(median)



# Mode of Dataframe 

# def modeDf(dataset):
#     return dataset.mode()

# mode = modeDf(df)
# print(mode)


# Min of Dataframe 

# def minDf(dataset):
#     return dataset.min()

# min = minDf(df)
# print(min)


# Max of Dataframe 

# def maxDf(dataset):
#     return dataset.max()

# max = maxDf(df)
# print(max)



# Mode of Dataframe 

# def modeDf(dataset):
#     return dataset.mode()

# mode = modeDf(df)
# print(mode)


# Mode of Dataframe 

# def modeDf(dataset):
#     return dataset.mode()

# mode = modeDf(df)
# print(mode)




##### Data Visualization 



# import matplotlib.pyplot as plt
# import seaborn as sb


## Product Rating Histogram


# def ratings_histogram(data):
#     sb.histplot(data=df, x='ratings', bins=5)
#     plt.title('Product Ratings Histogram')
#     plt.xlabel('Ratings')
#     plt.ylabel('Frequency')
#     plt.show()

# ratings_histogram(df)



# Relationship between actual price and ratings


# def ratings_scatterplot_actual(data):
#     sb.scatterplot(data=df, x='actual_price', y='ratings')
#     plt.title('Actual Price vs. Ratings')
#     plt.xlabel('Actual Price')
#     plt.ylabel('Ratings')
#     plt.show()

# ratings_scatterplot_actual(df)



# Relationship between discount price and ratings


# def ratings_scatterplot_discount(data):
#     sb.scatterplot(data=df, x='discount_price', y='ratings')
#     plt.title('Discount Price vs. Ratings')
#     plt.xlabel('Discount Price')
#     plt.ylabel('Ratings')
#     plt.show()

# ratings_scatterplot_discount(df)



# Box plot of actual price by sub category

# def actualPrice_BySubCategory_boxplot(data):
#     sb.boxplot(data=df, x='sub_category', y='actual_price')
#     plt.title('Actual Price by Sub Category')
#     plt.xlabel('Sub Category')
#     plt.ylabel('Actual Price')
#     plt.show()

# actualPrice_BySubCategory_boxplot(df)



# Box plot of discount price by sub category

# def discountPrice_BySubCategory_boxplot(data):
#     sb.boxplot(data=df, x='sub_category', y='discount_price')
#     plt.title('Discount Price by Sub Category')
#     plt.xlabel('Sub Category')
#     plt.ylabel('Discount Price')
#     plt.show()

# discountPrice_BySubCategory_boxplot(df)



# Box plot of actual price by main category

# def actualPrice_ByMainCategory_boxplot(data):
#     sb.boxplot(data=df, x='main_category', y='actual_price')
#     plt.title('Actual Price by Main Category')
#     plt.xlabel('Main Category')
#     plt.ylabel('Actual Price')
#     plt.show()

# actualPrice_ByMainCategory_boxplot(df)



# Box plot of discount price by main category

# def discountPrice_ByMainCategory_boxplot(data):
#     sb.boxplot(data=df, x='main_category', y='discount_price')
#     plt.title('Discount Price by Main Category')
#     plt.xlabel('Main Category')
#     plt.ylabel('Discount Price')
#     plt.show()

# discountPrice_ByMainCategory_boxplot(df)










