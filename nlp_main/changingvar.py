#cart_df       = {"+917666779269":pd.DataFrame({"+917666779269":[]})}
 
import os
dir = os.path.dirname(__file__)
filename = os.path.join(dir, '../public/mydata.json')
 

mainDB        = {"+917666779269":[]}
pot1          = {"+917666779269":[]}          
pot           = {"+917666779269":[]}           
total         = {"+917666779269":0}
cart          = {"+917666779269":""}


import json

# 'C:\\Users\\ADWAIT\\Downloads\\mydata.json'
class jsonfile():

  def __init__(self,cust,file =filename):
    self.cust = cust
    self.file = file 

  def read(self):
    f = open(self.file,'r')
    datas = json.load(f)
    f.close()
    return datas

  def write(self,content):
    with open(self.file,'w') as fp:
      json.dump(content,fp)

  def add_dict(self,dict2):
    data123 = self.read()
    data123.update(dict2)
    self.write(data123)

  def update(self,var,action="a",msg="ok",num=0):
    
    data = self.read()

    if var=='pot':
      
      if action=="r":
        return data[self.cust]['pot']
      elif action =="hi":
        data[self.cust]['pot']=['hi']
      elif action=="null":
        data[self.cust]['pot'] = []
      elif action=="ap":
        data[self.cust]['pot'].append(msg)
      elif action=="r-1":
        data[self.cust]['pot']=data[self.cust]['pot'][:-1]
      elif action=="a-1":
        return data[self.cust]['pot'][-1]
      elif action=="last":
        data[self.cust]['pot'][-1]=msg

    elif var == "pot1":
      if action=="r":
        return data[self.cust]['pot1']
      elif action == "null":
        data[self.cust]['pot1'] = []
      elif action=="a-1":
        return data[self.cust]['pot1'][-1]
      elif action == "ap":
        data[self.cust]['pot1'].append(msg)

    elif var=="mainDB":
      if action=="r":
        return data[self.cust]['mainDB']
      elif action == "null":
        data[self.cust]['mainDB'] = []
      elif action=="a-1":
        return data[self.cust]['mainDB'][-1]
      elif action == "ap":
        data[self.cust]['mainDB'].append(msg)

    elif var=="total":
      if action=="r":
        return data[self.cust]['total']
      elif action == "null":
        data[self.cust]['total']=0
      elif action == "ad":
        data[self.cust]['total'] += num

    elif var=="cart":
      if action=="r":
        #print("my"+ data[self.cust]['cart'])
        return data[self.cust]['cart']
      elif action == "null":
        data[self.cust]['cart']=""
      elif action == "ad":
        data[self.cust]['cart'] += msg

    elif var == "contacts":
      if action == "check":
        if self.cust in data:
          return 1
        

    self.write(data)
     
