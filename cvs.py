import numpy as np
import pandas as pd

df=pd.read_csv("coffeevssleep.csv")
data1=df["sleep in hours"].tolist()
data2=df["Coffee in ml"].tolist()
m=np.corrcoef(data2,data1)
print(m[0][1]*100)

