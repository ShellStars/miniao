# coding:utf-8
from django.conf.urls import patterns, url, include
from .views import *
from minicms import settings
urlpatterns = patterns('',
    url(r'^$', index, name='videoindex'),
    url(r'^zhuanji/$', video_album, name='video_album'),
    url(r'^(?P<column>[^/]+)/$', video, name='video'),
    url(r'^zhuanji/(?P<albumname>[^/]+)$', video_album_datail, name='video_album_datail'),
    url(r'^(?P<column>[^/]+)/(?P<pk>\d+)/$', video_detail, name='video_detail'),
    url(r'^zan/$', zan, name='zan'),
    #url(r'^(?P<column>[^/]+)/$', article, name='article'),
    #url(r'^(?P<column>[^/]+)/(?P<pk>\d+)/$', article_detail, name='article_detail'),
)