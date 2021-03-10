import sys
import json

# print(sys.argv[1])

class jsonf():

  def __init__(self,cust,file = 'mydata.json'):
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

  def update(self,msg):
    data = self.read()
    data[self.cust] += msg
    self.write(data)
    return self.read()[self.cust]
    
print(jsonf("ok").update(sys.argv[1]))

