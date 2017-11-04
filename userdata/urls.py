# coding:utf-8
from django.conf.urls import patterns, url
from .views import *
from minicms import settings
urlpatterns = patterns('',
    url(r'^$', login),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^sendpwdnum/$', sendpwdnum, name='sendpwdnum'),
    url(r'^resetpwd/$', resetpwd, name='resetpwd'),
    # url(r'^index/$', index, name='index'),
    url(r'^navigationinfo/$', navigationinfo, name='navigationinfo'),
    url(r'^show/$', show, name='show'),
    url(r'^modify/$', modify, name='modify'),
    url(r'^modifypassword/$', modifypassword, name='modifypassword'),
    url(r'^modifytelnum/$', modifytelnum, name='modifytelnum'),
    url(r'^collect/$', collect, name='collect'),
    url(r'^send_num/$', send_num, name='send_num'),
    url(r'^changlogin/$', changlogin, name='changlogin'),
)
