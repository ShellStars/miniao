# coding:utf-8
"""
    author:Lindow
    date:2017/10/22
"""
from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader, Context
from bs4 import BeautifulSoup
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from expert.models import Expertarticle
from article.models import Artiarticle
from video.models import Videoarticle
import pymysql


def dictfetchall(cursor):
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]


def index(request):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='miniao', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from video_videoclass")
    dic1 = dictfetchall(cursor)
    video_list = []
    for i in dic1:
        video_list.append(i)
    video_list.append({u'name': u'专辑', u'slug': u'zhuanji'})
    cursor.execute("select * from expert_expertarticle where published=True limit 18")
    expertinfo = dictfetchall(cursor)
    cursor.execute(
        "select * from meeting_meetarticle where column_id='yugao' and published=True order by id desc limit 5")
    yugaoinfo = dictfetchall(cursor)
    cursor.execute("select * from column_infoarticle where published=True order by id desc limit 5")
    zixuninfo = dictfetchall(cursor)
    for i in zixuninfo:
        soup = BeautifulSoup(i['content'], "html.parser")
        try:
            picurl = soup.img["src"]
        except:
            picurl = "/media/defaultpic.jpg"
        i['picurl'] = picurl
    cursor.execute("select * from video_videoarticle where published=True order by browser desc limit 5")
    shipininfo = dictfetchall(cursor)
    return render_to_response('index.html',
                              {'video_list': video_list, 'expertinfo': expertinfo, 'yugaoinfo': yugaoinfo, 'zixuninfo': zixuninfo, 'shipininfo': shipininfo},
                              context_instance=RequestContext(request))


def search(request):
    if "type" in request.GET and "value" in request.GET:
        type1 = request.GET["type"]
        value1 = request.GET["value"]
        if value1 == '':
            target = '/'+type1+'/'
            return HttpResponseRedirect(target)
        else:
            if type1 == "expert":
                article = Expertarticle.objects.filter(name__contains=value1, published=True).order_by("-id")
                objects, page_range = my_pagination(request, article, 50)
                return render_to_response('search_expert.html',
                                          {'objects': objects, 'page_range': page_range, 'type': type1, 'value': value1},
                                          context_instance=RequestContext(request))
            elif type1 == "article":
                article = Artiarticle.objects.filter(title__contains=value1, published=True).order_by("-id")
                objects, page_range = my_pagination(request, article, 50)
                return render_to_response('search_article.html',
                                          {'objects': objects, 'page_range': page_range, 'type': type1,
                                           'value': value1},
                                          context_instance=RequestContext(request))
            elif type1 == "video":
                article = Videoarticle.objects.filter(title__contains=value1, published=True).order_by("-id")
                objects, page_range = my_pagination(request, article, 50)
                return render_to_response('search_video.html',
                                          {'objects': objects, 'page_range': page_range, 'type': type1,
                                           'value': value1},
                                          context_instance=RequestContext(request))
            else:
                return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


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
