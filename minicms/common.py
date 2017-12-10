# coding:utf-8
import urllib2
import json
import time
import random
import string
import hashlib


def accesstokens():
    url= 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxeb8c8e02e23bc96a&secret=02368f878158ae508177fcae0e64dace'
    req = urllib2.Request(url)  
    data = urllib2.urlopen(req)  
    res = data.read()  
    res= json.loads(res)
    return res['access_token']


def getJsApiTicket():
    accessToken = accesstokens()
    url = "https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token={}&type=jsapi".format(accessToken)
    req = urllib2.Request(url)  
    res_data = urllib2.urlopen(req)  
    res = res_data.read()  
    res = json.loads(res)
    return str(res['ticket']) 


def createNonceStr(length = 16):   
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))


def getSignPackage(request):
    jsapiTicket = getJsApiTicket()
    # url = 'http://www.cug.top/column/321/1/'
    url = 'http://' + request.get_host() + request.get_full_path()
    timestamp = int(time.time())
    nonceStr = createNonceStr()
    ret = {  
        'nonceStr': nonceStr,  
        'jsapi_ticket': jsapiTicket,  
        'timestamp': timestamp,  
        'url': url  
     }
    string = '&'.join(['%s=%s' % (key.lower(), ret[key]) for key in sorted(ret)])  
    signature = hashlib.sha1(string).hexdigest()
    signPackage = {  
        "appId": 'wxeb8c8e02e23bc96a',  
        "nonceStr":nonceStr,  
        "timestamp":timestamp,  
        "url":url,  
        "signature":signature,  
        "rawString":string  
    }
    return signPackage   
# print getSignPackage()
