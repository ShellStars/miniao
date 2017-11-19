# coding:utf8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.shortcuts import render, render_to_response
from .models import Magearticle, Mageinfo, Magaclass
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext, loader, Context
import pymysql

# Create your views here.


def article_detail(request, magacolumn, column, pk):
    url = request.path.strip('/')
    # url = 'http://127.0.0.1:8000' + request.path
    tmpurl = '/'.join(str(request.path).split('/')[:-1]) + '/'
    article = Magearticle.objects.filter(pk=pk, magacolumn=magacolumn, column=column, published=True)
    classes = [{'column':'动态', 'slug': 'dongtai'}]
    relate = Magearticle.objects.filter(magacolumn=magacolumn, column=column, published=True)[0:2]
    pre_article = Magearticle.objects.filter(id__lt=pk, magacolumn=magacolumn, published=True)
    if pre_article:
        pre_article = pre_article.order_by('-id')[0]
    else:
        pre_article = Magearticle.objects.filter(id=pk, magacolumn=magacolumn, published=True)[0]
    next_article = Magearticle.objects.filter(id__gt=pk, magacolumn=magacolumn, published=True)
    if next_article:
        next_article = next_article[0]
    else:
        next_article = Magearticle.objects.filter(id=pk, magacolumn=magacolumn, published=True)[0]
    belong = {'name': '杂志', 'slug': 'magazine'}
    column_tmp = '动态'
    name1 = Magaclass.objects.filter(slug=magacolumn)[0].name
    second = {'name': name1, 'slug': magacolumn}
    column1 = {'name': column_tmp, 'slug': column}
    if article:
        num = article[0].browser + 1
        article.update(browser=num)
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='miniao', charset='utf8')
        cursor = conn.cursor()
        cursor.execute("select avg(scorenum) from userdata_score where url='%s'" % url)
        row1 = cursor.fetchone()
        if row1[0]:
            avgnum = row1[0]
        else:
            avgnum = 5
        if "userid" in request.session and "identity" in request.session:

            userid = request.session.get("userid")
            cursor.execute("select * from userdata_favourite where userid=%s and url='%s'" % (userid, url))
            row = cursor.fetchone()
            if row:
                collect = True
            else:
                collect = False

            cursor.execute("select scorenum from userdata_score where userid=%s and url='%s'" % (userid, url))
            row2 = cursor.fetchone()
            if row2:
                scorenum = '%.1f' % float(row2[0])
            else:
                scorenum = False
            return render(request, 'magazine_detail.html', {'pre_article': pre_article, 'next_article': next_article, 'belong': belong, 'classes': classes, 'column':column1, 'article': article[0], 'tmpurl': tmpurl, 'relate': relate, 'collect': collect, 'avgnum': avgnum,
                                                    'scorenum': scorenum, 'second':second})
        else:
            return render(request, 'magazine_detail.html', {'pre_article': pre_article, 'next_article': next_article, 'belong': belong, 'classes': classes, 'column':column1, 'article': article[0], 'tmpurl': tmpurl, 'relate': relate, 'avgnum': avgnum, 'second': second})
    else:
        return HttpResponseRedirect('/')


"""def article(request, column):
    tmpurl = str(request.path).strip('/')
    article = Magearticle.objects.filter(column=column, published=True)
    classes = [{'column':'动态', 'slug': 'dongtai'}]
    belong = 'magazine'
    column1 = '动态'
    objects, page_range = my_pagination(request, article, 2)
    return render_to_response('article_column.html', {'objects':objects, 'belong': belong, 'classes': classes, 'column':column1, 'page_range':page_range, 'tmpurl':tmpurl},context_instance=RequestContext(request))
"""
def article(request, magacolumn, column):
    url = '/magazine/'+magacolumn+'/'
    return HttpResponseRedirect(url)

def index(request, magacolumn):
    tmpurl = str(request.path).strip('/')
    article = Magearticle.objects.filter(magacolumn=magacolumn, published=True).order_by("-id")
    belong = {'name': '杂志', 'slug': 'magazine'}
    column1 = {'name':'动态', 'slug': 'dongtai'}
    name = Magaclass.objects.filter(slug=magacolumn)[0].name
    info = Mageinfo.objects.filter(magacolumn=magacolumn)[0:1]
    objects, page_range = my_pagination(request, article, 15)
    return render_to_response('article_magazine.html', {'name':name, 'objects': objects, 'belong': belong, 'info': info, 'column': column1,  'page_range': page_range, 'tmpurl': tmpurl},
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