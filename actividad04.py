import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')
print(df.head(2))
print(df.dtypes)
print(df.tail(10))