import pandas as pd 
import os
dir = os.path.dirname(__file__)
filename = os.path.join(dir,'../public/data.csv')


df= pd.read_csv('https://raw.githubusercontent.com/adwait2001/WHATSAPP_NODE_BOT/master/public/data.csv')
df = df.iloc[:len(df)].set_index("srno")