# coding:utf-8
from django.conf.urls import patterns, url, include
from .views import *
from minicms import settings
urlpatterns = patterns('',
    url(r'^$', expertarticle, name='expertarticle'),
    url(r'^zhuanjia/$', expertarticle_tmp, name='expertarticle_tmp'),
    url(r'^zhuanjia/(?P<pk>\d+)/$', expertarticle_detail, name='expertarticle_detail'),
    url(r'^fengfan/$', doctorarticle, name='doctorarticle'),
    url(r'^fengfan/(?P<pk>\d+)/$', doctorarticle_detail, name='doctorarticle_detail'),
    url(r'^zhuanfang/$', interviewarticle, name='interviewarticle'),
    url(r'^zhuanfang/(?P<pk>\d+)/$', interviewarticle_detail, name='interviewarticle_detail'),
    #url(r'^(?P<column>[^/]+)/$', article, name='article'),
    #url(r'^(?P<column>[^/]+)/(?P<pk>\d+)/$', article_detail, name='article_detail'),
)
