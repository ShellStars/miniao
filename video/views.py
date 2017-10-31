# coding:utf8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.shortcuts import render, render_to_response
from .models import Videoarticle
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext, loader, Context
import pymysql
# Create your views here.


def article_detail(request, column, pk):
    url = 'http://127.0.0.1:8000' + request.path
    article = Videoarticle.objects.filter(pk=pk, column=column, published=True)
    if article:
        num = article[0].browser + 1
        article.update(browser=num)
        if "userid" in request.session and "identity" in request.session:
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='miniao', charset='utf8')
            cursor = conn.cursor()
            userid = request.session.get("userid")
            cursor.execute("select * from userdata_favourite where userid=%s and url='%s'" % (userid, url))
            row = cursor.fetchone()
            if row:
                collect = True
            else:
                collect = False
            cursor.execute("select avg(scorenum) from userdata_score where url='%s'" % url)
            row1 = cursor.fetchone()
            if row1[0]:
                avgnum = row1[0]
            else:
                avgnum = 0
            cursor.execute("select scorenum from userdata_score where userid=%s and url='%s'" % (userid, url))
            row2 = cursor.fetchone()
            if row2:
                scorenum = '%.1f' % float(row2[0])
            else:
                scorenum = False
            return render(request, 'article.html', {'article': article[0], 'collect': collect, 'avgnum': avgnum,
                                                    'scorenum': scorenum})
        else:
            return render(request, 'article.html', {'article': article[0]})
    else:
        return HttpResponseRedirect('/')


def article(request, column):
    tmpurl = str(request.path).strip('/')
    article = Videoarticle.objects.filter(column=column, published=True)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='miniao', charset='utf8')
    cursor = conn.cursor()
    res = cursor.execute("select distinct disease from video_videoarticle")
    row = cursor.fetchmany(res)
    disease = []
    for i in row:
        disease.append(str(i[0]))
    res1 = cursor.execute("select distinct difficulty from video_videoarticle")
    row1 = cursor.fetchmany(res1)
    difficulty = []
    for i in row1:
        difficulty.append(str(i[0]))
    res2 = cursor.execute("select distinct other from video_videoarticle")
    row2 = cursor.fetchmany(res2)
    other = []
    for i in row2:
        other.append(str(i[0]))
    res3 = cursor.execute("select distinct expert from video_videoarticle")
    row3 = cursor.fetchmany(res3)
    expert = []
    for i in row3:
        expert.append(str(i[0]))
    if article:
        objects, page_range = my_pagination(request, article, 2)
        return render_to_response('article1.html', {'objects':objects,'page_range':page_range, 'tmpurl':tmpurl, 'disease':disease, 'difficulty':difficulty, 'other':other, 'expert':expert},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')

def index(request):
    article = Videoarticle.objects.filter(column='gonggao', published=True)[0:3]
    if article:
        return render(request, 'article2.html', {'article': article})
    else:
        return HttpResponseRedirect('/')

# 赞
def zan(request):
    if request.method == 'GET':
        try:
            url = request.GET['url']
        except:
            return HttpResponseRedirect('/')
        expertid = str(url).strip('/').split('/')[-1]
        tmp = Videoarticle.objects.filter(id=expertid)
        ori = tmp[0].zan
        tmp.update(zan=ori+1)
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
