# coding:utf8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.shortcuts import render, render_to_response
from .models import Assocarticle, Peoplearticle, Dynamicarticle
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
import pymysql
# Create your views here.


def showdetail(request):
    if request.method == "GET":
        info = Assocarticle.objects.all()[0]
        zhuwei = Peoplearticle.objects.filter(level=0)
        fuzhuwei = Peoplearticle.objects.filter(level=1)
        huiyuan = Peoplearticle.objects.filter(level=2)
        return render(request, 'article.html', {'info': info, 'zhuwei': zhuwei, 'fuzhuwei': fuzhuwei, 'huiyuan': huiyuan})
    else:
        return HttpResponseRedirect('/')


def article_detail(request, column, pk):
    url = 'http://127.0.0.1:8000' + request.path
    tmpurl = '/'.join(str(request.path).split('/')[:-1]) + '/'
    article = Dynamicarticle.objects.filter(pk=pk, column=column, published=True)
    classes = [{'column':'动态', 'slug': 'dongtai'}]
    relate = Dynamicarticle.objects.filter(column=column, published=True)[0:6]
    belong = 'association'
    column1 = '动态'
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
            return render(request, 'article_detail.html', {'belong': belong, 'classes': classes, 'column':column1, 'article': article[0], 'tmpurl': tmpurl, 'relate': relate, 'collect': collect, 'avgnum': avgnum,
                                                    'scorenum': scorenum})
        else:
            return render(request, 'article_detail.html', {'belong': belong, 'classes': classes, 'column':column1, 'article': article[0], 'tmpurl': tmpurl, 'relate': relate})
    else:
        return HttpResponseRedirect('/')


"""def special(request):
    article = Dynamicarticle.objects.filter(published=True)
    if article:
        objects, page_range = my_pagination(request, article, 2)
        return render_to_response('meeting.html', {'objects': objects, 'page_range': page_range},
                                  context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')
"""
def article(request, column):
    tmpurl = str(request.path).strip('/')
    article = Dynamicarticle.objects.filter(column=column, published=True)
    classes = [{'column':'动态', 'slug': 'dongtai'}]
    belong = 'association'
    column1 = '动态'
    objects, page_range = my_pagination(request, article, 2)
    return render_to_response('article_column.html', {'objects':objects, 'belong': belong, 'classes': classes, 'column':column1, 'page_range':page_range, 'tmpurl':tmpurl},context_instance=RequestContext(request))


def index(request):
    tmpurl = str(request.path).strip('/')
    article = Dynamicarticle.objects.filter(published=True)[0:6]
    associntro = Assocarticle.objects.all()[0]
    # people = Peoplearticle.objects.all()
    zhuwei = Peoplearticle.objects.filter(level=0)
    fuzhuwei = Peoplearticle.objects.filter(level=1)
    huiyuan = Peoplearticle.objects.filter(level=2)
    # objects, page_range = my_pagination(request, article, 9)
    return render_to_response('article_associntro.html', {'dynamic': article, 'tmpurl': tmpurl, 'associntro': associntro, 'zhuwei': zhuwei, 'fuzhuwei': fuzhuwei, 'huiyuan': huiyuan},
                              context_instance=RequestContext(request))


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

