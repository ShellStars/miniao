# coding:utf8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.shortcuts import render, render_to_response
from .models import Srucoarticle, Srucoclass
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext, loader, Context
import pymysql
# Create your views here.


def article_detail(request, column, pk):
    url = request.path.strip('/')
    # url = 'http://127.0.0.1:8000' + request.path
    tmpurl = '/'.join(str(request.path).split('/')[:-1]) + '/'
    article = Srucoarticle.objects.filter(pk=pk, column=column, published=True)
    classes = Srucoclass.objects.all()
    relate = Srucoarticle.objects.filter(column=column, published=True)[0:2]
    pre_article = Srucoarticle.objects.filter(id__lt=pk, published=True)
    if pre_article:
        pre_article = pre_article.order_by('-id')[0]
    else:
        pre_article = Srucoarticle.objects.filter(id=pk, published=True)[0]
    next_article = Srucoarticle.objects.filter(id__gt=pk, published=True)
    if next_article:
        next_article = next_article[0]
    else:
        next_article = Srucoarticle.objects.filter(id=pk, published=True)[0]
    belong = {'name': 'SRUCO', 'slug': 'sruco'}
    column_tmp = Srucoclass.objects.filter(slug=column)[0].name
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
            return render(request, 'article_detail.html', {'pre_article': pre_article, 'next_article': next_article, 'belong': belong, 'classes': classes, 'column':column1, 'article': article[0], 'tmpurl': tmpurl, 'relate': relate, 'collect': collect, 'avgnum': avgnum,
                                                    'scorenum': scorenum})
        else:
            return render(request, 'article_detail.html', {'pre_article': pre_article, 'next_article': next_article, 'belong': belong, 'classes': classes, 'column':column1, 'article': article[0], 'tmpurl': tmpurl, 'relate': relate, 'avgnum': avgnum})
    else:
        return HttpResponseRedirect('/')


def article(request, column):
    tmpurl = str(request.path).strip('/')
    article = Srucoarticle.objects.filter(column=column, published=True).order_by("-id")
    classes = Srucoclass.objects.all()
    belong = 'sruco'
    column1 = Srucoclass.objects.filter(slug=column)[0].name
    objects, page_range = my_pagination(request, article, 15)
    return render_to_response('article_column.html', {'objects':objects, 'belong': belong, 'classes': classes, 'column':column1, 'page_range':page_range, 'tmpurl':tmpurl},context_instance=RequestContext(request))


def index(request):
    tmpurl = str(request.path).strip('/')
    article = Srucoarticle.objects.filter(published=True).order_by("-id")
    classes = Srucoclass.objects.all()
    belong = 'sruco'
    objects, page_range = my_pagination(request, article, 15)
    return render_to_response('article_index.html', {'objects': objects, 'belong': belong, 'classes': classes,  'page_range': page_range, 'tmpurl': tmpurl},
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

