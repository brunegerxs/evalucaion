import pandas as pd
df=pd.read_csv('StudentsPerformance.csv')
print(df['gender'].head(12))
print(df['lunch'].head(12))
print(df['math score'].head(12))
print(df['gender'].tail(8))
print(df['lunch'].tail(8))
print(df['math score'].tail(8))