"""minicms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from views import *
from DjangoUeditor import urls as DjangoUeditor_urls
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^search/$', search, name='search'),
    #url(r'^column/(?P<column_slug>[^/]+)/$', 'news.views.column_detail', name='column'),
    #url(r'^news/(?P<pk>\d+)/(?P<article_slug>[^/]+)/$', 'news.views.article_detail', name='article'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ueditor/', include(DjangoUeditor_urls)),
    url(r'userdata/', include('userdata.urls')),
    url(r'article/', include('article.urls')),
    url(r'column/', include('column.urls')),
    url(r'meeting/', include('meeting.urls')),
    url(r'association/', include('association.urls')),
    url(r'expert/', include('expert.urls')),
    url(r'magazine/', include('magazine.urls')),
    url(r'video/', include('video.urls')),
    url(r'guide/', include('guide.urls')),
    url(r'nursing/', include('nursing.urls')),
    url(r'recommend/', include('recommend.urls')),
    url(r'sruco/', include('sruco.urls')),
    url(r'subject/', include('subject.urls')),
    url(r'universal/', include('universal.urls')),
    # url(r'$', test, name='test'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)