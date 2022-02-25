import numpy as np
import pandas as pd

df=pd.read_csv("marksvsdays.csv")
data1=df["Days Present"].tolist()
data2=df["Marks In Percentage"].tolist()
m=np.corrcoef(data2,data1)
print(m[0][1]*100)

