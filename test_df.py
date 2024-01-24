import pandas as pd

selected_classification = "Pattern Category"

df =pd.read_csv('dataset.csv')

df = df[pd.notnull(df["text"])]
col = ["text", selected_classification]
df = df[col]

print(df[selected_classification].value_counts())