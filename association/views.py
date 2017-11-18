# coding:utf8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.shortcuts import render, render_to_response
from .models import Assocarticle, Peoplearticle, Dynamicarticle, Assocclass
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
import pymysql
# Create your views here.


"""def showdetail(request):
    if request.method == "GET":
        info = Assocarticle.objects.all()[0]
        zhuwei = Peoplearticle.objects.filter(level=0)
        fuzhuwei = Peoplearticle.objects.filter(level=1)
        huiyuan = Peoplearticle.objects.filter(level=2)
        return render(request, 'article.html', {'info': info, 'zhuwei': zhuwei, 'fuzhuwei': fuzhuwei, 'huiyuan': huiyuan})
    else:
        return HttpResponseRedirect('/')"""


def article_detail(request, assoccolumn, column, pk):
    url = request.path.strip('/')
    # url = 'http://127.0.0.1:8000' + request.path
    tmpurl = '/'.join(str(request.path).split('/')[:-1]) + '/'
    article = Dynamicarticle.objects.filter(pk=pk, assoccolumn=assoccolumn, column=column, published=True)
    classes = [{'column':'动态', 'slug': 'dongtai'}]
    name1 = Assocclass.objects.filter(slug=magacolumn)[0].name
    second = {'name': name1, 'slug': magacolumn}
    relate = Dynamicarticle.objects.filter(assoccolumn=assoccolumn, column=column, published=True)[0:2]
    pre_article = Dynamicarticle.objects.filter(id__lt=pk, assoccolumn=assoccolumn, published=True)
    if pre_article:
        pre_article = pre_article.order_by('-id')[0]
    else:
        pre_article = Dynamicarticle.objects.filter(id=pk, assoccolumn=assoccolumn, published=True)[0]
    next_article = Dynamicarticle.objects.filter(id__gt=pk, assoccolumn=assoccolumn, published=True)
    if next_article:
        next_article = next_article[0]
    else:
        next_article = Dynamicarticle.objects.filter(id=pk, assoccolumn=assoccolumn, published=True)[0]
    belong = {'name': '学会', 'slug': 'association'}
    column_tmp = '动态'
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
            return render(request, 'association_detail.html', {'pre_article': pre_article, 'next_article': next_article, 'belong': belong, 'classes': classes, 'column':column1, 'article': article[0], 'tmpurl': tmpurl, 'relate': relate, 'collect': collect, 'avgnum': avgnum,
                                                    'scorenum': scorenum, 'second':second})
        else:
            return render(request, 'association_detail.html', {'pre_article': pre_article, 'next_article': next_article, 'belong': belong, 'classes': classes, 'column':column1, 'article': article[0], 'tmpurl': tmpurl, 'relate': relate, 'avgnum': avgnum, 'second':second})
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
def article(request, assoccolumn, column):
    tmpurl = str(request.path).strip('/')
    article = Dynamicarticle.objects.filter(assoccolumn=assoccolumn, column=column, published=True).order_by("-id")
    associntro = Assocarticle.objects.filter(assoccolumn=assoccolumn)[0:1]
    belong = {'name': '学会', 'slug': 'association'}
    column1 = {'name': '动态', 'slug': 'dongtai'}
    objects, page_range = my_pagination(request, article, 15)
    return render_to_response('dongtai_index.html', {'objects':objects, 'belong': belong, 'info': associntro, 'column':column1, 'page_range':page_range, 'tmpurl':tmpurl},context_instance=RequestContext(request))


def index(request, assoccolumn):
    tmpurl = str(request.path).strip('/')
    article = Dynamicarticle.objects.filter(assoccolumn=assoccolumn, published=True).order_by("-id")[0:6]
    associntro = Assocarticle.objects.filter(assoccolumn=assoccolumn)[0:1]
    # people = Peoplearticle.objects.all()
    zhuwei = Peoplearticle.objects.filter(assoccolumn=assoccolumn, level=0)
    fuzhuwei = Peoplearticle.objects.filter(assoccolumn=assoccolumn, level=1)
    huiyuan = Peoplearticle.objects.filter(assoccolumn=assoccolumn, level=2)
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

