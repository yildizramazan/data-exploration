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


#3
# Which college major has the lowest mid-career salary and how much can people expect to earn with this degree?
index_3 = df["Mid-Career Median Salary"].idxmin()
major_3 = df["Undergraduate Major"].loc[index_3]
print(index_3, major_3)
mid_career_salary = df["Mid-Career Median Salary"].loc[index_2]
print(mid_career_salary)


spread_col = df['Mid-Career 90th Percentile Salary'] - df['Mid-Career 10th Percentile Salary']
df.insert(1, 'Spread', spread_col)
low_risk = df.sort_values('Spread')
print(low_risk)

highest_potential = df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

highest_spread = df.sort_values('Spread', ascending=False)
highest_spread[['Undergraduate Major', 'Spread']].head()

print(df.groupby('Group').count())