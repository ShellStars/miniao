# coding:utf-8
from django.conf.urls import patterns, url
from .views import *
from minicms import settings
urlpatterns = patterns('',
    url(r'^$', register, name='register'),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login),
)
