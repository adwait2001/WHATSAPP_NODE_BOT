 
import en_core_web_sm
import spacy
from google_trans_new import google_translator
import re
from word2number import w2n


import changingvar as cv
import constantfunc as cf
import createfunc as crf



'''def next(a,b,cust):
  ap = tp.textprocess(cust)
  pm = ap.last(b,0)
  if pm != "item not available in our stock":
      return pm
  else:
      return a.add_and_show(b,ap,ap.formdict(b))'''
    
class textprocess():  
  nlp = en_core_web_sm.load()
  def __init__(self,cust):
      self.cust = cust
       

  def regex(self,senti):
      my = []
      sent = senti.split()
     
      for i in sent:
          try:
              x=re.search(i,crf.text)
              my.append(x.group())
          except:
              pass
      return my
  
  def formdict(self,sent):
      ok = self.data_parts(sent )
      mp2={}
      for i in ok:
          mp = self.analysis(ok[i])
          if mp!={}:
              mp2.update(mp)
      return mp2
              
  def hinglish(self,sent,x):
      translator = google_translator()
      result = translator.translate(sent, lang_src="en",lang_tgt='mr')
      if x==1:
          return result
      elif x==2:
          final = translator.translate(result,lang_src = "mr", lang_tgt='en')
          return final
      else:
          return sent
  
  def meaning(self,word):
      for i in crf.doc:
          if word in crf.doc[i]:
              return i  

  def analysis(self,lis):
      book = {}
    
      for j in lis:
          
          m = self.meaning(j)
          
          if m != None:
              book[m] = j
      return book
  
  def tree_enquiry(self,mp , sr = '',flag=0):
      doc = crf.doc
      #print(doc)
      productinfo = crf.productinfo
      if 'greetings' in mp:
          return "welcome,I hope you liked it.."
      elif 'enquiry' in mp:
          if 'subcat' in mp:
              sr += mp['subcat']
              if 'company' in mp:
                  if 'price' in mp:
                      pce = productinfo[mp['company']]
                      if 'quantity' in mp:
                          net = pce * int(mp['quantity'])
                      else:
                          net = pce*1
                      if "weight" in mp:
                          return "the price of {} {} {} is {}".format(mp['quantity'],mp['weight'],mp['company'],net)
                      else:
                          return "the price of {} {} {} is {}".format(mp['quantity'],'litre',mp['company'],net)
                  else:
                      return "Yes ,your demanded item {} is available".format(mp['company'])
              else:
                  return cf.switch1(str((doc['subcat'].index(mp['subcat']))+1))
          else:
              if 'product' in mp:
                  if 'price' in mp:
                      pce = productinfo['product']
                      if 'quantity' in mp:
                          net = pce * int(mp['quantity'])
                      else:
                          net = pce*1
                      if "weight" in mp:
                          return "the price of {}{} is {}".format(mp['quantity'],mp['weight'],mp['product'])
                  else:
                      return "Yes ,your demanded item {} is available".format(mp['product'])
              else:
                  print("ok")
                  return "item not available in our stock"
      else:
          return self.tree_order(mp,'')
  
  def tree_order(self,mp , sr = '' ,flag=0):
      doc = crf.doc
      productinfo = crf.productinfo
      if 'order' in mp:
          if 'subcat' in mp:
              sr += mp['subcat']
              if 'company' in mp:
                  sr=" "+mp['company']+ ' '+sr
                  pce = productinfo[mp['company']]
                  if 'quantity' in mp:
                      mp['quantity']=w2n.word_to_num(mp['quantity'])
                      net = pce *(mp['quantity'])
                  else:
                      net = pce*1
                      mp['quantity']=1
                  if "weight" in mp:
                      kpl = productinfo[mp['weight']]
                      net = net * kpl//1000
                      
                      sr+="    " + str(mp['quantity'])+' X '+mp['weight']+"   "+str(net)
                  else:
                      sr+="    " + str(mp['quantity']) +"   "+str(net)
                  #cv.total[self.cust] += net
                  cv.jsonfile(self.cust).update('total','ad',num = net)
                  
                  pmf = "\n" + sr
                  cv.jsonfile(self.cust).update('cart','ad',pmf)
                  return   "your cart till now\n"+ cv.jsonfile(self.cust).update('cart','r') + "\nTOTAL:" + str(cv.jsonfile(self.cust).update('total','r'))
              else:
                  return cf.switch1(str((crf.doc['subcat'].index(mp['subcat']))+1))
          else:
              if 'product' in mp:
                  flag+=1
                  sr+=mp['product']
                  pce = productinfo[mp['product']]
                  if 'quantity' in mp:
                      mp['quantity']=w2n.word_to_num(mp['quantity'])
                      net = pce * mp['quantity']
                  else:
                      net = pce*1
                      mp['quantity'] = 1
                  if "weight" in mp:
                      kpl = productinfo[mp['weight']]
                      net = net * kpl//1000
                      sr += '    ' + mp['quantity']+' '+mp['weight']+'    '+str(net)
                      
                  else:
                      sr += '   ' + mp['quantity']+'    '+str(net)
                  #cv.total[self.cust] += net
                  cv.jsonfile(self.cust).update('total','ad',num = net)
                  pmf = "\n" + sr
                  cv.jsonfile(self.cust).update('cart','ad',pmf)
                  return   "your cart till now\n"+ cv.jsonfile(self.cust).update('cart','r') + "\nTOTAL:" + str(cv.jsonfile(self.cust).update('total','r'))
              else:
                  return "item not available in our stock"
      else:
          if 'subcat' in mp:
              sr += mp['subcat']
              if 'company' in mp:
                  if 'price' in mp:
                      pce = productinfo[mp['company']]
                      if 'quantity' in mp:
                          net = pce * w2n.word_to_num(mp['quantity'])
                      else:
                          net = pce*1
                      if "weight" in mp:
                          return "the price of {} {} {} is {}".format(mp['quantity'],mp['weight'],mp['company'],net)
                      else:
                          return "the price of {} {} {} is {}".format(mp['quantity'],'litre',mp['company'],net)
                  else:
                      return "Yes ,your demanded item {} is available".format(mp['company'])
              else:
                  return cf.switch1(str((doc['subcat'].index(mp['subcat']))+1))
          else:
              if 'product' in mp:
                  if 'price' in mp:
                      pce = productinfo['product']
                      if 'quantity' in mp:
                          net = pce * w2n.word_to_num(mp['quantity'])
                      else:
                          net = pce*1
                      if "weight" in mp:
                          return "the price of {}{} is {}".format(mp['quantity'],mp['weight'],mp['product'])
                  else:
                      return "Yes ,your demanded item {} is available".format(mp['product'])
              else:
                  #print("rjnk")
                  return "item not available in our stock"
                  #return 7890
        
        
            

  def data_parts(self,text):
      common = {"noun":[],"verb":[],"adj":[],"digit":[],"unknown":[],"stop":[],"pronoun":[]}
      doc = self.nlp(text)
      #df = pd.DataFrame({"word":[],"noun":[],"adj":[],"verb":[],"digit":[],"punct":[],"stopword":[]})
      for token in doc:
      #df.loc[len(df)]=[token, token.pos_=='NOUN',token.pos_=="ADJ",token.pos_=="VERB" ,token.is_digit ,token.is_punct,token.is_stop ]
          if token.pos_=="NOUN":
              common["noun"].append(token.text)
          elif token.pos_ == "PRON":
              common["pronoun"].append(token.text)
          elif token.pos_=="ADJ":
              common['adj'].append(token.text)
          elif token.pos_=="VERB":
              common['verb'].append(token.text)
          elif token.is_digit == True:
              common['digit'].append(token.text)
              crf.doc['quantity'].append(token.text)
          elif token.is_stop == True:
              common['stop'].append(token.text)
          elif token.is_punct == True:
              pass
          else:
              common['unknown'].append(token.text)
      return common
  
  def last(self,sent,flag=0):
      obj = self
      om = self.hinglish(sent,flag)
     # print(om)
      pm = obj.formdict(om)
     # print(pm)
      return self.tree_enquiry(pm)

 
