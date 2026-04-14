import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')
print(df.tail(3))
print(df.shape)
print(df.dtypes)
print(df.notnull())