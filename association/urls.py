# coding:utf-8
from django.conf.urls import patterns, url, include
from .views import *
from minicms import settings
urlpatterns = patterns('',
    url(r'^special/$', special, name='special'),
    url(r'^(?P<column>[^/]+)/(?P<pk>\d+)/$', article_detail, name='article_detail'),
)
