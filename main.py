import pandas as pd
import random
df = pd.read_csv('salaries_by_college_major.csv')
print(df.head(n=50))
print(df.shape)
print(df.columns[0])
df.isna()
df.tail()
df.dropna()
print(df['Starting Median Salary'].idxmax())
print(df['Undergraduate Major'].loc[43])
print(df.loc[random.randint(0,50)])
print(df['Starting Median Salary'].idxmin())
