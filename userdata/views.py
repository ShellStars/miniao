# coding:utf8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django import forms
from .models import Userinfo, Checknum, Favourite, Score
from PIL import Image
import json
import os
import requests
import hashlib
import time
import random
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 用户
class UserForm(forms.Form):
    username = forms.CharField()
    sex = forms.IntegerField()
    telnum = forms.CharField()
    checknum = forms.IntegerField()
    hospital = forms.CharField()
    department = forms.CharField()
    title = forms.CharField()
    identity = forms.IntegerField()
    password = forms.CharField()
    certificate = forms.FileField()


# 登录
class Login(forms.Form):
    telnum = forms.IntegerField()
    password = forms.CharField()


# 忘记密码
class ForgetpwdForm(forms.Form):
    telnum = forms.IntegerField()
    checknum = forms.IntegerField()


class PwdForm(forms.Form):
    password = forms.CharField()


#用户详细信息
class Modify(forms.Form):
    headimg = forms.FileField()
    #hospital = forms.CharField()
    #department = forms.CharField()
    #title = forms.CharField()


# 修改密码
class Modifypwd(forms.Form):
    oldpwd = forms.CharField()
    newpwd = forms.CharField()


class Modifytelnum(forms.Form):
    oldnum = forms.IntegerField()
    newnum = forms.IntegerField()
    checknum = forms.IntegerField()



###tool

def cremd5(src):
    m2 = hashlib.md5()
    m2.update(src)
    return m2.hexdigest()


def num():
    numtmp = ''
    for i in range(6):
        numtmp += str(random.randint(0, 9))
    return numtmp


def sendnum(telnum):
    url = 'http://capi.yuntongzhi.vip/Api/Sms/sendSms'
    password = cremd5(cremd5('12345678')+str(int(time.time())))
    time1 = str(int(time.time()))
    numtmp = num()
    d = {'user': 'xuwei', 'passwd': password, 'times': time1, 'mobile': telnum,
         'content': '【云通知】您的验证码是：' + numtmp + '。请不要把验证码泄露给其他人。如非本人操作，可不用理会！', 'stype': 1}
    r = requests.post(url, data=d)
    res = r.json()
    res[u'num'] = numtmp
    return res




# 注册
def register(request):
    if request.method == "POST":
        # 医生0，护士1，学生2，其它3
        if "identity" in request.POST and request.POST["identity"] != '':
            identity = request.POST["identity"]
            if identity == '0' or identity == '1':
                uf = UserForm(request.POST, request.FILES)
                if uf.is_valid():
                    telnum = uf.cleaned_data['telnum']
                    checknum = uf.cleaned_data['checknum']
                    telnum1 = Userinfo.objects.filter(telnum=telnum)
                    try:
                        checknum1 = Checknum.objects.filter(telnum=telnum)[0].checknum
                    except:
                        checknum1 = ''
                    if len(telnum1) > 0 :
                        # dic = {'info': '用户已存在'}
                        # return render_to_response('register.html', dic)
                        return HttpResponse(json.dumps({'info': '用户已存在'}), content_type="application/json")
                    elif checknum1 == '' or str(checknum) != checknum1:
                        # dic = {'info': '验证码错误'}
                        # return render_to_response('register.html', dic)
                        return HttpResponse(json.dumps({'info': '验证码错误'}), content_type="application/json")
                    else:
                        username = uf.cleaned_data['username']
                        password = uf.cleaned_data['password']
                        sex = uf.cleaned_data['sex']
                        hospital = uf.cleaned_data['hospital']
                        department = uf.cleaned_data['department']
                        title = uf.cleaned_data['title']
                        identity = identity
                        certificate = request.FILES["certificate"]
                        img = Image.open(certificate)
                        url = BASE_DIR + '/media/uploads/images/certificate/' + certificate.name
                        img.save(url, "jpeg")
                        user = Userinfo()
                        user.username = username
                        user.password = password
                        user.sex = sex
                        user.telnum = telnum
                        user.hospital = hospital
                        user.department = department
                        user.title = title
                        user.identity = identity
                        url1 = '/media/uploads/images/certificate/' + certificate.name
                        #Userinfo.objects.create(username=username, password=password, telnum=telnum, email=email, identity=identity, certificate=url)
                        Userinfo.objects.create(username=username, password=password, sex=sex, telnum=telnum,
                                                hospital=hospital, department=department, title=title,
                                                identity=identity, certificate=url1)
                        Checknum.objects.filter(telnum=telnum).delete()
                        #user1 = Userinfo.objects.filter(telnum=telnum)
                        #request.session['userid'] = user1[0].id
                        #request.session['identity'] = user1[0].identity
                        return HttpResponseRedirect('/index/?from=register')
                        #return HttpResponseRedirect('/userdata/show/')
                        #dic = {'info': '注册成功，请登录'}
                        #return render_to_response('login.html', dic)
                else:
                    return render_to_response('register.html')
            elif identity == '2' or identity == '3':
                telnum = request.POST['telnum']
                checknum = request.POST['checknum']
                telnum1 = Userinfo.objects.filter(telnum=telnum)
                try:
                    checknum1 = Checknum.objects.filter(telnum=telnum)[0].checknum
                except:
                    checknum1 = ''
                if len(telnum1) > 0:
                    # dic = {'info': '用户已存在'}
                    # return render_to_response('register.html', dic)
                    return HttpResponse(json.dumps({'info': '用户已存在'}), content_type="application/json")
                elif checknum1 == '' or str(checknum) != checknum1:
                    # dic = {'info': '验证码错误'}
                    # return render_to_response('register.html', dic)
                    return HttpResponse(json.dumps({'info': '验证码错误'}), content_type="application/json")
                else:
                    username = request.POST['username']
                    password = request.POST['password']
                    sex = request.POST['sex']
                    Userinfo.objects.create(username=username, password=password, sex=sex, telnum=telnum,
                                            identity=identity)
                    Checknum.objects.filter(telnum=telnum).delete()
                    #user = Userinfo.objects.filter(telnum=telnum)
                    #request.session['userid'] = user[0].id
                    #request.session['identity'] = user[0].identity
                    return HttpResponseRedirect('/index/?from=register')
                    #return HttpResponseRedirect('/userdata/show/')
                    # dic = {'info': '注册成功，请重新登录'}
                    # return render_to_response('login.html', dic)
                    # return HttpResponse(json.dumps({'info': '注册成功，请登录'}), content_type="application/json")
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        return render_to_response('register.html')


# 登录
def login(request):
    if request.method == "POST":
        af = Login(request.POST)
        if af.is_valid():
            telnum = af.cleaned_data['telnum']
            password = af.cleaned_data['password']
            user = Userinfo.objects.filter(telnum=telnum, password=password)
            if user:
                if user[0].ispass == True:
                    request.session['userid'] = user[0].id
                    request.session['identity'] = user[0].identity
                    return HttpResponse(json.dumps({'info': 'success'}), content_type="application/json")
                else:
                    # dic = {'info': '正在审核'}
                    # return render_to_response('login.html', dic)
                    return HttpResponse(json.dumps({'info': '正在审核'}), content_type="application/json")
            else:
                # dic = {'info': '您输入的密码有误'}
                # return render_to_response('login.html', dic)
                return HttpResponse(json.dumps({'info': '您输入的密码有误'}), content_type="application/json")
        else:
            return render_to_response('login.html')
    else:
        if "userid" in request.session and "identity" in request.session:
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/index/?from=register')


# 退出
def logout(request):
    try:
        del request.session['userid']
        del request.session['identity']
    except:
        pass
    return HttpResponseRedirect('/')


# 忘记密码
def forgetpwd(request):
    return render_to_response('forgetpwd.html')


def modifypwd(request):
    return render_to_response('modifypwd.html')


def index(request):
    return render_to_response('index.html')

# 发送修改密码验证码
def sendpwdnum(request):
    if request.method == "POST":
        bf = ForgetpwdForm(request.POST)
        if bf.is_valid():
            telnum = bf.cleaned_data['telnum']
            checknum = bf.cleaned_data['checknum']
            telnum1 = Userinfo.objects.filter(telnum=telnum)
            try:
                checknum1 = Checknum.objects.filter(telnum=telnum)[0].checknum
            except:
                checknum1 = ''
            if len(telnum1) == 0:
                # dic = {'info': '未注册'}
                # return render_to_response('forgetpwd.html', dic)
                return HttpResponse(json.dumps({'info': '未注册'}), content_type="application/json")
            elif checknum1 == '' or str(checknum) != checknum1:
                # dic = {'info': '验证码错误'}
                # return render_to_response('forgetpwd.html', dic)
                return HttpResponse(json.dumps({'info': '验证码错误'}), content_type="application/json")
            else:
                response = HttpResponse(json.dumps({'info': 'success'}), content_type="application/json")
                # response = render_to_response('resetpwd.html')
                response.set_cookie('userid', telnum1[0].id)
                Checknum.objects.filter(telnum=telnum).delete()
                return response
        else:
            # dic = {'info': "您输入的信息错误"}
            # return render_to_response('forgetpwd.html', dic)
            return HttpResponse(json.dumps({'info': '您输入的信息错误'}), content_type="application/json")
    else:
        return render_to_response('forgetpwd.html')


def resetpwd(request):
    if "userid" in request.COOKIES:
        if request.method == "POST":
            bf = PwdForm(request.POST)
            if bf.is_valid():
                password = bf.cleaned_data['password']
                a = request.COOKIES["userid"]
                Userinfo.objects.filter(id=a).update(password=password)
                #dic = {'info': '密码已重置，请重新登录'}
                #response = render_to_response('login.html', dic)
                response = HttpResponse(json.dumps({'info': 'success'}), content_type="application/json")
                response.delete_cookie('userid')
                return response
            else:
                return HttpResponseRedirect('/')
        else:
            return render_to_response('resetpwd.html')

    else:
        return HttpResponseRedirect('/')


# 查看个人信息
def show(request):
    if "userid" in request.session and "identity" in request.session:
        a = request.session.get("userid")
        userinfo = Userinfo.objects.filter(id=a)
        #cc = userinfo[0].username
        dic = {'userinfo':userinfo[0]}
        return render_to_response('userinfo.html', dic)
    else:
        return HttpResponseRedirect('/userdata/login')

# 验证用户是否登录head
def navigationinfo(request):
    if "userid" in request.session and "identity" in request.session:
        a = request.session.get("userid")
        userinfo = Userinfo.objects.filter(id=a)
        username = userinfo[0].username
        headimg = userinfo[0].headimg.name
        identity = userinfo[0].identity
        return HttpResponse(json.dumps({'state': 'success', 'username': username, 'headimg': headimg, 'identity': identity}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'state': 'fail'}), content_type="application/json")

# 修改个人信息
def modify(request):
    if "userid" in request.session and "identity" in request.session:
        if request.method == "POST":
            bf = Modify(request.POST, request.FILES)
            if bf.is_valid():
                headimg = request.FILES["headimg"]
                img = Image.open(headimg)
                url = BASE_DIR + '/media/uploads/images/userdata/' + headimg.name
                img.save(url, "jpeg")
                url1 = '/media/uploads/images/userdata/' + headimg.name
                #hospital = bf.cleaned_data['hospital']
                #department = bf.cleaned_data['department']
                #title = bf.cleaned_data['title']
                b = request.session.get("userid")
                Userinfo.objects.filter(id=b).update(headimg=url1)
                return HttpResponse(json.dumps({'info': 'success'}), content_type="application/json")
                #userinfo1 = Userinfo.objects.filter(id=b)
                #return render_to_response('userinfo.html', {'userinfo': userinfo1[0]})
            else:
                return HttpResponseRedirect('/')
        else:
            return render_to_response('userinfo.html')
    else:
        return HttpResponseRedirect('/')


# 查看密码
#def showpwd(request):
#    if "userid" in request.COOKIES:
#        a = request.COOKIES["userid"]
#        userinfo = Userinfo.objects.filter(id=a)
#        return render_to_response('modifypwd.html')
#    else:
#        return HttpResponseRedirect('/userdata/login')


# 修改密码
def modifypassword(request):
    if "userid" in request.session and "identity" in request.session:
        if request.method == "POST":
            bf = Modifypwd(request.POST)
            if bf.is_valid():
                oldpwd = bf.cleaned_data['oldpwd']
                newpwd = bf.cleaned_data['newpwd']
                a = request.session.get("userid")
                user = Userinfo.objects.filter(id=a, password=oldpwd)
                if user:
                    user.update(password=newpwd)
                    #dic = {'info': '密码已重置，请重新登录'}
                    try:
                        del request.session['userid']
                        del request.session['identity']
                    except:
                        pass
                    #response = render_to_response('login.html', dic)
                    return HttpResponse(json.dumps({'info': 'success'}), content_type="application/json")
                    # return response
                else:
                    #dic = {'info': '原密码输入错误！'}
                    #response = render_to_response('modify.html', dic)
                    #return response
                    return HttpResponse(json.dumps({'info': '原密码输入错误！'}), content_type="application/json")
            else:
                return HttpResponseRedirect('/')
        else:
            return render_to_response('userinfo.html')
    else:
        return HttpResponseRedirect('/')


# 修改手机
def modifytelnum(request):
    if "userid" in request.session and "identity" in request.session:
        if request.method == "POST":
            bf = Modifytelnum(request.POST)
            if bf.is_valid():
                oldnum = bf.cleaned_data['oldnum']
                newnum = bf.cleaned_data['newnum']
                a = request.session.get("userid")
                user = Userinfo.objects.filter(id=a, telnum=oldnum)
                user1 = Userinfo.objects.filter(telnum=newnum)
                if user:
                    checknum = bf.cleaned_data['checknum']
                    try:
                        checknum1 = Checknum.objects.filter(telnum=oldnum)[0].checknum
                    except:
                        checknum1 = ''
                    if checknum1 == '' or str(checknum) != checknum1:
                        # dic = {'info': '验证码错误'}
                        # response = render_to_response('modify.html', dic)
                        # return response
                        return HttpResponse(json.dumps({'info': '验证码错误'}), content_type="application/json")
                    elif user1:
                        # dic = {'info': '手机号已存在'}
                        # response = render_to_response('modify.html', dic)
                        # return response
                        return HttpResponse(json.dumps({'info': '手机号已存在'}), content_type="application/json")
                    else:
                        user.update(telnum=newnum)
                        #userinfo1 = Userinfo.objects.filter(id=a)
                        #response = render_to_response('userinfo.html', {'userinfo': userinfo1})
                        #return response
                        return HttpResponse(json.dumps({'info': 'success'}), content_type="application/json")
                else:
                    #dic = {'errors': '原手机号码错误'}
                    #response = render_to_response('modify.html', dic)
                    #return response
                    return HttpResponse(json.dumps({'info': '原手机号码错误'}), content_type="application/json")
            else:
                return HttpResponseRedirect('/')
        else:
            return render_to_response('modify.html')
    else:
        return HttpResponseRedirect('/')


# 收藏
def collect(request):
    if request.method == 'GET':
        a = request.session.get("userid")
        if a:
            try:
                url = request.GET['url']
                title = request.GET['title']
            except:
                return HttpResponseRedirect('/')
            Favourite.objects.create(userid=a, title=title, url=url)
            return HttpResponse(json.dumps({'info': 'success'}), content_type="application/json")
        else:
            return HttpResponseRedirect('/')

    else:
        return HttpResponseRedirect('/')


# 收藏页面
def showcollect(request):
    if request.method == 'GET':
        a = request.session.get("userid")
        if a:
            result = Favourite.objects.filter(userid=a).order_by("addtime")
            objects, page_range = my_pagination(request, result, 20)
            return render_to_response('collection.html', {'objects': objects, 'page_range': page_range},
                                      context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


# 取消收藏
def cancel(request):
    if request.method == 'GET':
        a = request.session.get("userid")
        if a:
            try:
                url = request.GET['url']
            except:
                return HttpResponseRedirect('/')
            res = Favourite.objects.filter(userid=a, url=url)
            if res:
                res[0].delete()
                return HttpResponse(json.dumps({'info': 'success'}), content_type="application/json")
                # response = HttpResponseRedirect('/userdata/showcollect')
                # return response
            else:
                return HttpResponse(json.dumps({'info': 'success'}), content_type="application/json")
                # response = HttpResponseRedirect('/userdata/showcollect')
                # return response
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


# 打分
def scoreclass(request):
    if request.method == 'GET':
        a = request.session.get("userid")
        if a:
            try:
                url = request.GET['url']
                num = request.GET['scorenum']
            except:
                return HttpResponseRedirect('/')
            Score.objects.create(userid=a, scorenum=num, url=url)
            b = Userinfo.objects.filter(id=a)
            newnum = b[0].integralnum + 1
            b.update(integralnum=newnum)
        else:
            return HttpResponseRedirect('/')

    else:
        return HttpResponseRedirect('/')


# 发送验证码
def send_num(request):
    if request.method == 'GET':
        telnum = request.GET['telnum']
        res = sendnum(telnum)
        if res['code'] == 0:
            if Checknum.objects.filter(telnum=telnum):
                Checknum.objects.filter(telnum=telnum).update(checknum=res['num'])
            else:
                Checknum.objects.create(telnum=telnum, checknum=res['num'])
            return HttpResponse(json.dumps({'info': 'success'}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'info': '号码格式有误'}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'info': 'wrong'}), content_type="application/json")


# 畅言
def changlogin(request):
    callback = request.GET.get('callback')
    if "userid" in request.session and "identity" in request.session:
        user_id = request.session.get('userid')
        print type(user_id)
        img_url = 'http://ww4.sinaimg.cn/large/0060lm7Tly1fkiul1adrkj31hc0xc7ei.jpg'
        nickname = str(Userinfo.objects.filter(id=user_id)[0].username)
        print type(nickname)
        profile_url = ''
        result = {
            "is_login": 1,
            "user": {
                "img_url": img_url,
                "nickname": nickname,
                "profile_url": profile_url,
                "user_id": user_id,
                "sign": '#'
            }
        }
        result = '{0}({1})'.format(callback, result)
        return HttpResponse(result)
    else:
        result = {
            "is_login": 0,
        }
        result = '{0}({1})'.format(callback, result)
        return HttpResponse(result)


def my_pagination(request, queryset, display_amount, after_range_num=3, bevor_range_num=2):
    paginator = Paginator(queryset,display_amount)
    try:
        page = int(request.GET["page"])
    except:
        page = 1
    try:
        object = paginator.page(page)
    except (EmptyPage, InvalidPage):
        object = paginator.page(paginator.num_pages)
    except:
        object = paginator.page(1)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+bevor_range_num]
    else:
        page_range = paginator.page_range[0:page+bevor_range_num]
    return object,page_range


