import sys
import random
import changingvar as cv
import constantfunc as cf
import createfunc as crf
import textprocess as tp

  
class sub1():
 
  def __init__(self,cust):
      self.cust=cust
      
  def add_and_show(self,arg,obj,dictionary): 
      if arg in ["Hi","hi"]:
          #cv.pot[self.cust] = ["hi"]
          cv.jsonfile(self.cust).update('pot','hi')
          return  cf.sendtxt(cf.switch1("Hi"),self.cust)
        
      else:
          if "cat" in arg:
              #cv.pot[self.cust] = ["hi"]
              cv.jsonfile(self.cust).update('pot','hi')
              #if self.cust in cv.contacts:
              if cv.jsonfile(self.cust).update('contacts','check')==1:
                  return cf.switch1("Hi")
              else:
                  return cf.switch("Hi2.0")
            
          elif "cart" in arg:
              #sp = cv.cart[self.cust]
              sp = cv.jsonfile(self.cust).update('cart','r')
              print(sp)
              if sp== "" :
                   return "your cart is empty \njust send *Hi* and add items in your cart"
              else:
                   #return  "your cart till now\n"+sp+"\nTOTAL : "+str(cv.total[self.cust])
                   return "your cart till now\n"+sp+"\nTOTAL : " + str(cv.jsonfile(self.cust).update('total','r'))
                
          elif "place" in arg :
              ##################self.pot1[self.cust].append(self.pot[self.cust])  ignore this
              #cv.mainDB[self.cust].append(cv.pot[self.cust])
              cv.jsonfile(self.cust).update('mainDB','ap',cv.jsonfile(self.cust).update('pot','r'))
              #mpl = cv.cart[self.cust]
              mpl = cv.jsonfile(self.cust).update('cart','r')
              #cv.pot[self.cust] = []
              cv.jsonfile(self.cust).update('pot','null')
              #cv.pot1[self.cust]=[]
              cv.jsonfile(self.cust).update('pot1','null')
              #net = cv.total[self.cust]
              net = cv.jsonfile(self.cust).update('total','r')
              #cv.total[self.cust] = 0
              cv.jsonfile(self.cust).update('total','null')
              if mpl ==  "":
                  return cf.sendtxt("you cannot place the order as you dont have any items in your cart",self.cust )
              else:
                  #cv.cart[self.cust]=""
                  cv.jsonfile(self.cust).update('cart','null')
                  return "thanks for shopping with us\n" + mpl+"\nTOTAL : "+str(net)+"\nYour order will be delivered by half-hour,..\nvist the E- mart again...!!"
            
          else:
              try:
                  #cv.pot[self.cust].append(arg)
                  cv.jsonfile(self.cust).update('pot','ap',arg)
                  #pot = cv.pot[self.cust]
                  pot = cv.jsonfile(self.cust).update('pot','r')
                  mayu = int(arg) 
                  #print(pot)
                  if len(pot) == 2:
                      if pot[-1] in "1234":
                          return cf.urls(pot[-1])+"\n"+cf.switch1(pot[-1])
                      else:
                          #cv.pot[self.cust].pop(-1)
                          cv.jsonfile(self.cust).update('pot','r-1')
                          return cf.sendtxt("plz give the correct input so I can understand.",self.cust) 
                  elif len(pot) == 3:
                      if pot[-1] in "12345":
                          return cf.sendtxt(cf.switch2(pot[1:]),self.cust)
                      else:
                          #cv.pot[self.cust].pop(-1)
                          cv.jsonfile(self.cust).update('pot','r-1')
                          return cf.sendtxt("plz give the correct input so I can understand.",self.cust)

 
                  elif len(pot)==4:
                      if cf.wordnum(pot[-1])!=-1:
                        #######wtm = cf.wordnum(pot[-1])         ignore this
                        #cv.pot[self.cust][-1]=str(wtm)
                        cv.jsonfile(self.cust).update('pot','last',str(wtm))
                        #cv.pot1[self.cust].append(cv.pot[self.cust])
                        cv.jsonfile(self.cust).update('pot1','ap',cv.jsonfile(self.cust).update('pot','r'))
                        #cv.pot[self.cust] = ["hi"]
                        cv.jsonfile(self.cust).update('pot','hi')
                        #cf.finalcart(cv.pot1[self.cust][-1],self.cust,obj,dictionary)
                        cf.finalcart(cv.jsonfile(self.cust).update('pot1','a-1'),self.cust,obj,dictionary)
                        return cf.sendtxt(cf.switch3(pot[-1]),self.cust)
                      else:
                         #cv.pot[self.cust].pop(-1)
                         cv.jsonfile(self.cust).update('pot','r-1')
                         return cf.sendtxt("plz give the correct input so I can understand.\nTo order new item just send *Hi* here",self.cust) 
                           

                  else:
                      #cv.pot[self.cust].pop(-1)
                      cv.jsonfile(self.cust).update('pot','r-1')
                      return cf.sendtxt("plz give the correct input so I can understand.\nTo order new item just send *Hi* here",self.cust) 
              except:# type(arg) == str:
                  
                  #pot = cv.pot[self.cust]
                  pot = cv.jsonfile(self.cust).update('pot','r')
                  if len(pot)==4:
                      wtm = cf.wordnum(pot[-1])
                      if wtm != -1:
                        #cv.pot[self.cust][-1]=str(wtm)
                        cv.jsonfile(self.cust).update('pot','last',str(wtm))
                        #cv.pot1[self.cust].append(cv.pot[self.cust])
                        cv.jsonfile(self.cust).update('pot1','ap',cv.jsonfile(self.cust).update('pot','r'))
                        #cv.pot[self.cust] = ["hi"]
                        cv.jsonfile(self.cust).update('pot','hi')
                        #cf.finalcart(cv.pot1[self.cust][-1],obj,self.cust,dictionary)
                        cf.finalcart(cv.jsonfile(self.cust).update('pot1','a-1'),obj,self.cust,dictionary)
                        return cf.sendtxt(cf.switch3(pot[-1]),self.cust)
                      else:
                         #cv.pot[self.cust].pop(-1)
                         cv.jsonfile(self.cust).update('pot','r-1')
                         return cf.sendtxt("plz give the correct input so I can understand.\nTo order new item just send *Hi* here",self.cust) 
                           
                      return cf.sendtxt(cf.switch3(pot[-1]),self.cust)
                  else:
                      #cv.pot[self.cust].pop(-1)
                      cv.jsonfile(self.cust).update('pot','r-1')
                      return cf.sendtxt(cf.random_response(random.randint(1,3)),self.cust)
                    
                    
#####################3333333333333333333333########################3###################3
              
def next(a,b,cust):
  ap = tp.textprocess(cust)
  pm = ap.last(b,0)
  #print(4353545454475566)
  if pm !="item not available in our stock":
      #print(pm+'  ok')
      return pm
  else:
     # print("you :",ap.formdict(b))
      return a.add_and_show(b,ap,ap.formdict(b))
    
def sms_reply(msg,remote_number = "+919518394022"):
   
  am = msg.lower()  

  #if remote_number in cv.contacts:
  if cv.jsonfile(remote_number).update('contacts','check')==1:
       
      #cv.contacts[remote_number].cart_df[remote_number].loc[len(contacts[remote_number].cart_df[remote_number].index) , remote_number] = am
      mk = next(sub1(remote_number),am,remote_number)      
  else:
      '''cv.contacts[remote_number] = sub1(remote_number)
      cv.total[remote_number] = 0
      cv.pot[remote_number]=[]
      cv.pot1[remote_number]=[]
      cv.mainDB[remote_number]=[]
      #cv.contacts[remote_number].cart_df={remote_number:pd.DataFrame({remote_number:[]})}
      #cv.contacts[remote_number].cart_df[remote_number].loc[len(contacts[remote_number].cart_df[remote_number].index) , remote_number] = am
      #mk = next(contacts[remote_number],am)
      cv.cart[remote_number] = ""'''

      pf = {remote_number: {"pot": [], "pot1": [], "mainDB": [], "total": 0, "cart": ""}}
      cv.jsonfile(remote_number).add_dict(pf)
      mk = cf.rules()
  return str(mk)

