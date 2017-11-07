# coding:utf-8
from django.conf.urls import patterns, url
from .views import *
from minicms import settings
urlpatterns = patterns('',
    url(r'^$', index, name='index1'),
    url(r'^(?P<column>[^/]+)/$', article, name='article'),
    url(r'^(?P<column>[^/]+)/(?P<pk>\d+)/$', article_detail, name='article_detail'),
)
