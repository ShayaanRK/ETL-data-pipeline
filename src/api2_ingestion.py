# pyrefly: ignore [missing-import]
import numpy as np
import pandas as pd
# pyrefly: ignore [missing-import]
import kagglehub
import os

os.system('cls') 

file_path = kagglehub.dataset_download("ruchi798/data-science-job-salaries")
print("Path to dataset files:", file_path)

# dict1 = {
#     "name" : ['harry', 'rohan', 'shubham', 'sandy'],
#     "marks" : [90, 80, 70, 60],
#     "city" : ["delhi", "mumbai", "kolkata", "chennai"]
# }

# ser = pd.Series(np.random.rand(34))
# print(ser)

# newdf = pd.DataFrame(np.random.rand(34, 5), index=np.arange(34))
# print(newdf)
# print(type(newdf))

# operations on data frames
# newdf.loc[0,0] = 654
# print(newdf.head())

# newdf.columns = list("ABCDE")
# print(newdf.head())

# newdf.loc[2, 'C'] = 69
# print(newdf.head())

# print(newdf.head())
# print(newdf.loc[[1,2], [1,2]])

csv_path = os.path.join(file_path, "ds_salaries.csv")
df = pd.read_csv(csv_path)
print(df.head())

# 1. Check shape (Rows, Columns)
print("\n=== Dimensions ===")
print(f"Shape: {df.shape} (Rows: {df.shape[0]}, Columns: {df.shape[1]})")

# 2. Checking data types of each columns
print("\n=== Column Data Types ===")
print(df.dtypes)

# 3. Check missing/null values per column
print("\n=== Null Values Per Column ===")
print(df.isnull().sum())

# 4. Copmrehensive summary 
print("\n=== Comprehensive Summary ===")
df.info()

