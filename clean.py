import pandas as pd
dataset=pd.read_csv("test.csv")

df=dataset.iloc[:,1:]
df.to_csv("cleaned.csv")