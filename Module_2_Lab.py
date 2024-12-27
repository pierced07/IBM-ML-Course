import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
import requests

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import norm
from scipy import stats

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML0232EN-SkillsNetwork/asset/Ames_Housing_Data1.tsv"

# Download the file
response = requests.get(url)
if response.status_code == 200:
    with open("Ames_Housing_Data1.tsv", "wb") as f:
        f.write(response.content)

# Load the data using pandas
housing = pd.read_csv("Ames_Housing_Data1.tsv", sep='\t')

# Display the first 5 rows
print("First 5 rows of the dataset:")
print(housing.head(5))

# Print the shape of the DataFrame (number of rows and columns)
print("\nShape of the dataset (rows, columns):")
print(housing.shape)

# Print basic information about the DataFrame (columns, types, non-null counts)
print("\nBasic information about the dataset:")
print(housing.info())

# Optionally, you can display summary statistics of numerical columns
print("\nSummary statistics of the dataset:")
print(housing.describe())

print(housing["SalePrice"].describe())

print(housing["Sale Condition"].value_counts())

hous_num = housing.select_dtypes(include = ['float64', 'int64'])
hous_num_corr = hous_num.corr()['SalePrice'][:-1] # -1 means that the latest row is SalePrice
top_features = hous_num_corr[abs(hous_num_corr) > 0.5].sort_values(ascending=False) #displays pearsons correlation coefficient greater than 0.5
print("There is {} strongly correlated values with SalePrice:\n{}".format(len(top_features), top_features))

for i in range(0, len(hous_num.columns), 5):
    sns.pairplot(data=hous_num,
                x_vars=hous_num.columns[i:i+5],
                y_vars=['SalePrice'])
    
sp_untransformed = sns.displot(housing['SalePrice'])
