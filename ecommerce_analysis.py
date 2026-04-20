#dataset
import pandas as pd

df = pd.read_csv("online_retail.csv", encoding='latin1')
print(df.head())