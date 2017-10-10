# coding:utf8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from .models import Userinfo, Checknum
from PIL import Image
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 用户
class UserForm(forms.Form):
    username = forms.CharField()
    sex = forms.BooleanField()
    telnum = forms.IntegerField()
    checknum = forms.IntegerField()
    email = forms.EmailField()
    hospital = forms.CharField()
    department = forms.CharField()
    title = forms.CharField()
    password = forms.CharField()
    identity = forms.IntegerField()
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
    email = forms.EmailField()
    hospital = forms.CharField()
    department = forms.CharField()
    title = forms.CharField()


# 修改密码
class Modifypwd(forms.Form):
    oldpwd = forms.EmailField()
    newpwd = forms.EmailField()



# 注册
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST, request.FILES)
        if uf.is_valid():
            telnum = uf.cleaned_data['telnum']
            checknum = uf.cleaned_data['checknum']
            email = uf.cleaned_data['email']
            errors = []
            telnum1 = Userinfo.objects.filter(telnum=telnum)
            email1 = Userinfo.objects.filter(email=email)
            try:
                checknum1 = Checknum.objects.filter(telnum=telnum)[0].checknum
            except:
                checknum1 = ''
            if len(telnum1) > 0 or len(email1) > 0:
                errors.append('用户已存在')
                return render_to_response('register.html', {'errors': errors[0]})
            elif checknum1 == '' or checknum != checknum1:
                errors.append('验证码错误')
                return render_to_response('register.html', {'errors': errors[0]})
            else:
                username = uf.cleaned_data['username']
                password = uf.cleaned_data['password']
                sex = uf.cleaned_data['sex']
                hospital = uf.cleaned_data['hospital']
                department = uf.cleaned_data['department']
                title = uf.cleaned_data['title']
                identity = uf.cleaned_data['identity']
                certificate = request.FILES["certificate"]
                img = Image.open(certificate)
                url = BASE_DIR + '/media/uploads/images/certificate/' + certificate.name
                img.save(url, "jpeg")
                user = Userinfo()
                user.username = username
                user.password = password
                user.sex = sex
                user.telnum = telnum
                user.email = email
                user.hospital = hospital
                user.department = department
                user.title = title
                user.identity = identity
                Userinfo.objects.create(username=username, password=password, sex=sex, telnum=telnum,
                                        email=email, hospital=hospital, department=department, title=title,
                                        identity=identity, certificate=url)
                Checknum.objects.filter(telnum=telnum).delete()
                errors = []
                errors.append("注册成功，请重新登录")
                return render_to_response('login.html', {'errors': errors[0]})
        else:
            errors = []
            errors.append("填写信息不完整")
            return render_to_response('register.html', {'errors': errors[0]})
    else:
        return render_to_response('register.html')


# 登录
def login(request):
    if request.method == "POST":
        af = Login(request.POST)
        if af.is_valid():
            telnum = af.cleaned_data['telnum']
            password = af.cleaned_data['password']
            errors = []
            user = Userinfo.objects.filter(telnum=telnum, password=password)
            if user:
                response = HttpResponseRedirect('/userdata/')
                response.set_cookie('telnum',telnum)
                return response
            else:
                errors.append('您输入的密码有误')
                return render_to_response('login.html', {'errors': errors[0]})
        else:
            errors = []
            errors.append("您输入的密码有误")
            return render_to_response('login.html', {'errors': errors[0]})
    else:
        return render_to_response('login.html')

# 退出
def logout(request):
    response = HttpResponseRedirect('/userdata/login')
    response.delete_cookie('username')
    response.delete_cookie('seller')
    return response


# 忘记密码
def forgetpwd(request):
    return render_to_response('forgetpwd.html')


def modifypwd(request):
    return render_to_response('modifypwd.html')


# 发送修改密码验证码
def sendpwdnum(request):
    if request.method == "POST":
        bf = ForgetpwdForm(request.POST)
        if bf.is_valid():
            telnum = bf.cleaned_data['telnum']
            checknum = bf.cleaned_data['checknum']
            errors = []
            telnum1 = Userinfo.objects.filter(telnum=telnum)
            try:
                checknum1 = Checknum.objects.filter(telnum=telnum)[0].checknum
            except:
                checknum1 = ''
            if len(telnum1) == 0:
                errors.append('未注册')
                return render_to_response('forgetpwd.html', {'errors': errors[0]})
            elif checknum1 == '' or checknum != checknum1:
                errors.append('验证码错误')
                return render_to_response('forgetpwd.html', {'errors': errors[0]})
            else:
                response = HttpResponseRedirect('/resetpwd')
                response.set_cookie('telnum', telnum)
                Checknum.objects.filter(telnum=telnum).delete()
                return response
        else:
            errors = []
            errors.append("您输入的信息错误")
            return render_to_response('forgetpwd.html', {'errors':errors[0]})
    else:
        return HttpResponseRedirect('/forgetpwd')


def resetpwd(request):
    if "telnum" in request.COOKIES:
        if request.method == "POST":
            bf = PwdForm(request.POST)
            if bf.is_valid():
                password = bf.cleaned_data['password']
                errors = []
                a = request.COOKIES["telnum"]
                Userinfo.objects.filter(telnum=a).update(password=password)
                errors.append("密码已重置，请重新登录")
                return render_to_response('login.html', {'errors': errors[0]})
            else:
                errors = []
                errors.append("您输入的信息错误")
                return render_to_response('forgetpwd.html', {'errors': errors[0]})
        else:
            return HttpResponseRedirect('/userdata/modifypwd')

    else:
        return HttpResponseRedirect('/userdata/forgetpwd')


# 查看个人信息
def show(request):
    if "telnum" in request.COOKIES:
        a = request.COOKIES["telnum"]
        userinfo = Userinfo.objects.filter(telnum=a)
        #cc = userinfo[0].username
        return render_to_response('userinfo.html', {'userinfo':userinfo})
    else:
        return HttpResponseRedirect('/userdata/login')


# 修改个人信息
def modify(request):
    if request.method == "POST":
        bf = Modify(request.POST)
        if bf.is_valid():
            email = bf.cleaned_data['email']
            hospital = bf.cleaned_data['hospital']
            department = bf.cleaned_data['department']
            title = bf.cleaned_data['title']
            b = request.COOKIES["telnum"]
            Userinfo.objects.filter(telnum=b).update(email=email, hospital=hospital,
                                                     department=department, title=title)
        else:
            error = ['信息不正确']
            return render_to_response('modify.html', error[0])
    else:
        return HttpResponseRedirect('/')


#查看密码
def showpwd(request):
    if "telnum" in request.COOKIES:
        a = request.COOKIES["telnum"]
        userinfo = Userinfo.objects.filter(telnum=a)
        return render_to_response('modifypwd.html', {'userinfo':userinfo})
    else:
        return HttpResponseRedirect('/userdata/login')


# 修改密码
def modifypassword(request):
    if request.method == "POST":
        bf = Modifypwd(request.POST)
        if bf.is_valid():
            oldpwd = bf.cleaned_data['oldpwd']
            newpwd = bf.cleaned_data['newpwd']
            errors = []
            a = request.COOKIES["telnum"]
            user = Userinfo.objects.filter(telnum=a, password=oldpwd)
            userinfo = Userinfo.objects.filter(telnum=a)
            if user:
                user.update(password=newpwd)
                errors.append("密码已重置，请重新登录！")
                return render_to_response('login.html', {'errors':errors[0]})
            else:
                errors.append("原密码输入错误！")
                dic = {'errors': errors[0], 'username':userinfo}
                return render_to_response('modifypwd.html', dic)
        else:
            return HttpResponseRedirect('/userdata/login')
    else:
        return HttpResponseRedirect('/userdata/login')




