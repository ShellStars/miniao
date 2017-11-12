# coding:utf-8
from django.conf.urls import patterns, url, include
from .views import *
from minicms import settings
urlpatterns = patterns('',
    url(r'^$', index, name='otherindex'),
    url(r'^download/$', download_album, name='download_album'),
    url(r'^download/(?P<albumname>[^/]+)$', download_album_datail, name='download_album_datail'),
    url(r'^download/(?P<pk>\d+)/$', download_cal, name='download_cal'),
    url(r'^(?P<column>[^/]+)/$', article, name='article'),
    url(r'^(?P<column>[^/]+)/(?P<pk>\d+)/$', article_detail, name='article_detail'),
    # url(r'^zan/$', zan, name='zan'),
    #url(r'^(?P<column>[^/]+)/$', article, name='article'),
    #url(r'^(?P<column>[^/]+)/(?P<pk>\d+)/$', article_detail, name='article_detail'),
)