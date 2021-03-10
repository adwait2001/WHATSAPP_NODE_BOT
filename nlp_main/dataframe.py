import pandas as pd 
import os
dir = os.path.dirname(__file__)
filename = os.path.join(dir,'../public/data.csv')


df= pd.read_csv('C:\\Users\\ADWAIT\\Downloads\\dataofcust.csv')
df = df.iloc[:len(df)].set_index("srno")