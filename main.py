import pandas as pd
import random
df = pd.read_csv('salaries_by_college_major.csv')
# print(df.head(n=50))
# print(df.shape)
# print(df.columns[0])
# df.isna()
# df.tail()
# df.dropna()
# print(df['Starting Median Salary'].idxmax())
# print(df['Undergraduate Major'].loc[43])
# print(df.loc[random.randint(0,50)])
# print(df['Starting Median Salary'].idxmin())

#1
# What college major has the highest mid-career salary?
index_1 = df["Mid-Career 10th Percentile Salary"].idxmax()
major_1 = df["Undergraduate Major"].loc[index_1]
print(index_1, major_1)
# How much do graduates with this major earn?
starting_salary_1 = df["Starting Median Salary"].loc[index_1]
print(starting_salary_1)


#2
# Which college major has the lowest starting salary and how much do graduates earn after university?
index_2 = df["Starting Median Salary"].idxmin()
major_2 = df["Undergraduate Major"].loc[index_2]
print(index_2, major_2)
starting_salary_2 = df["Starting Median Salary"].loc[index_2]
print(starting_salary_2)
