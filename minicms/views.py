# coding:utf-8
"""
    author:Lindow
    date:2017/10/22
"""
from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader, Context
from bs4 import BeautifulSoup
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
