import matplotlib as plt
import numpy as np 
import pandas as pd  

df=pd.read_csv("datasets/AAPL.csv")
AAPL_df=df["Close"]
AAPL_df.head()

