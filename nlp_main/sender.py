import requests
import sys 
import process as pc

message=pc.sms_reply(sys.argv[1])


class gupshup():
    
    ### private data
    
    __url     = "https://api.gupshup.io/sm/api/v1/msg"
    __API_KEY = '8w3nskoooe0rznmewrjlcec2eltfvfpx'    #### your api - key
    __headers = {
              'Content-Type': 'application/x-www-form-urlencoded',
              'apikey': __API_KEY
              }
    __payload ='channel=whatsapp&source=917834811114&destination={}&src.name='+'adwait2020'+'&' ## in place of newbot711 place ur  src.name
    
  
    def __init__(self,cust="919518394022"):
        self.cust = cust
        
    def sendgupshup(self,msg):
        pload = self.__payload.format(self.cust)+'message=%7B%22type%22%3A%20%22text%22%2C%22text%22%3A%20%22'+ msg +'%20%22%7D'
        pload2 = self.__payload.format(self.cust)+'message=%7B%22type%22%3A%20%22image%22%2C%22%22%3A%20%22originalUrl%22%2C%22%22%3A%20%22'+ msg +'%22%2C%22%22%3A%20%22previewUrl'+msg+'%20%22%7D'

        res   = requests.request("POST",self.__url,headers = self.__headers,data = pload)

def sms_reply2(msg,cust):
    gupshup(cust).sendgupshup(msg)



print(sms_reply2(message,sys.argv[2]))
