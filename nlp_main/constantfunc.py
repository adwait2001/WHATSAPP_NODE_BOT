import pandas as pd
import random
import pandas as pd
import en_core_web_sm
import spacy
from google_trans_new import google_translator
import re
from word2number import w2n

import changingvar as cv
 
 
import createfunc as crf
import dataframe as dfi

 
import process as pc
 
 
 

################################################################################################################################################
def switch1(argument): 
  mydict = {"Hi":  "order your items or products by typing code for it \n"+ crf.company_numberwise_static,
           "Hi2.0": " to add next item in your cart\n"+ crf.company_numberwise_static
           }    
  mydict.update(crf.made_one_dic)
  a = "plz give correct input option number.I am still in learning phase."
  return  (mydict.get(argument, a))
  
def switch2(pot_lis): 
  """switcher = {
          "1": "how many litres of milk do you want?", 
          "2": "how many grams or KGs of Dal you want to buy?", 
          "3": "how many Kgs of oil do you need?",
          "4": "how many soaps do you want?",
          }"""
  
  return crf.find_and_ask(pot_lis)

def switch0(arg0="Hi"):
  return switch1("Hi")

 

def switch3(arg3):
  switchof="product added to the cart \n\n'CAT'-> To view the subcategories\n'PLACE'->To place the order and confirm"
  return switchof

def switch4(arg4):
  dictl = {"1":switch1("Hi"),
           "2":"your order is taken by our side",
          }
  return dictl.get(arg4," I don't understand your response plz make it correct")

def random_response(arg):
  randomdict = { 1:"sorry I didn't hear that ",
      2:"please specify your input in correct manner which I can understand",
      3:"Ohh I didn't see that coming make it more specific in a way I can understand"
        
  }
  return randomdict[arg]

def rules():
  mp = 'WELcome to SuPeR MaRkeT ...\n enjoy the new way of whatsapp shopping with your trustworthy local businesses\n\n shortkeys to place the orders ,checking prices,payments,cartlist etc...\n CAT-to get the list of products\n\nCART-to get to know about items you have added \n\nPLACE- confirming and go towards payments\n\n'#*ADD*- specifying this will help to directly add products in your cart\n\n'#*RATE*- rate our service out of 10'#\n\n*KHATA*- know your history of last 7 days orders\n\n*INST*- write specific instruction deemands for your product delivery '
  return mp

def urls(args):
  dic = {"1":'https://i.ibb.co/SrNmjbK/outfile.jpg',
         "2":'https://i.ibb.co/dQQsnc8/outfile.jpg',
         "3":'https://i.ibb.co/hLVx7x1/outfile.jpg',
        "4":'https://i.ibb.co/bRZD1vh/outfile.jpg'}
  return dic[args]



##3################ instaed of this take list as parameter############################################################################################
############### return find_and_ask[lis]
    


def finalcart(my_list,obj,cust,my_dict):
  #cv.cart[cust]
  cv.jsonfile(cust).update('cart','r')
  item = my_list
  #cv.cart[cust]
  pm = "\n"+ cart(item[1],item[2],item[3],cust,my_dict,obj)
  #print("you said"+pm)
  cv.jsonfile(cust).update('cart','ad',pm)
  #print("pl  "+cv.jsonfile(cust).update('cart',"r"))
  return  cv.jsonfile(cust).update('cart',"r")

def cart(x,y,z,cust,my_dict,obj):
  ###################################    databse that will change $$$$$$$$$$$$$$$$$
  try:
      s1 = crf.productinfo[my_dict['weight']]
      s2=float(w2n.word_to_num(my_dict['quantity']))
      cost = (crf.price_dict[x][int(y)]) * int(s1)*s2//1000
      #cv.total[cust] += cost
      cv.jsonfile(cust).update('total','ad',num=cost)
      return dv.dic1[x+y]+"      " + z + " X " + my_dict['weight']+"    " + str(cost)
  except:
      #print(crf.price_dict)
      cost = (crf.price_dict[x][int(y)]) * float(z)
      #print(cost)
      #cv.total[cust] += cost
      cv.jsonfile(cust).update('total','ad',num=cost)
      returnl= crf.dic1[x+y]+"      " + str(z) + " X " + "quan    "+"    " + str(cost)
      #print(returnl)
      return returnl
    
def sendtxt(msg,cust):
  #return gupshup().sendgupshup( msg,cust)
  return msg

 

def wordnum(s):
    for i in s.split():
        try:
            return (w2n.word_to_num(i)) 
        except:
            pass
    return -1




 
######################################################################################################################
