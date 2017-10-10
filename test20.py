# coding:utf-8
import requests
url = 'http://capi.yuntongzhi.vip/Api/Sms/sendSms'
import hashlib
import time
def cremd5(src):
    m2 = hashlib.md5()
    m2.update(src)
    return m2.hexdigest()
password = cremd5(cremd5('12345678')+str(int(time.time())))
time1 = str(int(time.time()))
d = {'user': 'xuwei', 'passwd': password, 'times': time1, 'mobile': '1899',
     'content': '【云通知】您的验证码是：1234。请不要把验证码泄露给其他人。如非本人操作，可不用理会！', 'stype': 1}
r = requests.post(url, data=d)
print r.text