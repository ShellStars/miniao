# coding:utf8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.shortcuts import render, render_to_response
from .models import Standardarticle, Resourcearticle, Standardclass, Resourcesclass
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext, loader, Context
import pymysql
# Create your views here.


def article_detail(request, column, pk):
    url = request.path.strip('/')
    # url = 'http://127.0.0.1:8000' + request.path
    tmpurl = '/'.join(str(request.path).split('/')[:-1]) + '/'
    article = Standardarticle.objects.filter(pk=pk, column=column, published=True)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='miniao', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from other_standardclass")
    dic1 = dictfetchall(cursor)
    final_list = []
    for i in dic1:
        final_list.append(i)
    final_list.append({u'name': u'下载', u'slug': u'download'})
    relate = Standardarticle.objects.filter(column=column, published=True)[0:2]
    pre_article = Standardarticle.objects.filter(id__lt=pk, published=True)
    if pre_article:
        pre_article = pre_article.order_by('-id')[0]
    else:
        pre_article = Standardarticle.objects.filter(id=pk, published=True)[0]
    next_article = Standardarticle.objects.filter(id__gt=pk, published=True)
    if next_article:
        next_article = next_article[0]
    else:
        next_article = Standardarticle.objects.filter(id=pk, published=True)[0]
    belong = {'name': '其他', 'slug': 'other'}
    column_tmp = Standardclass.objects.filter(slug=column)[0].name
    column1 = {'name': column_tmp, 'slug': column}
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
            return render(request, 'article_detail.html', {'pre_article': pre_article, 'next_article': next_article, 'belong': belong, 'classes': final_list, 'column':column1, 'article': article[0], 'tmpurl': tmpurl, 'relate': relate, 'collect': collect, 'avgnum': avgnum,
                                                    'scorenum': scorenum})
        else:
            return render(request, 'article_detail.html', {'pre_article': pre_article, 'next_article': next_article, 'belong': belong, 'classes': final_list, 'column':column1, 'article': article[0], 'tmpurl': tmpurl, 'relate': relate})
    else:
        return HttpResponseRedirect('/')
def article(request, column):
    tmpurl = str(request.path).strip('/')
    article = Standardarticle.objects.filter(column=column, published=True).order_by("-id")
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='miniao', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from other_standardclass")
    dic1 = dictfetchall(cursor)
    final_list = []
    for i in dic1:
        final_list.append(i)
    final_list.append({u'name': u'下载', u'slug': u'download'})
    belong = 'other'
    column1 = Standardclass.objects.filter(slug=column)[0].name
    objects, page_range = my_pagination(request, article, 2)
    return render_to_response('article_column.html', {'objects':objects, 'belong': belong, 'classes': final_list, 'column':column1, 'page_range':page_range, 'tmpurl':tmpurl},context_instance=RequestContext(request))

def download_cal(request, pk):
    downfile = Resourcearticle.objects.filter(pk=pk, published=True)
    if downfile:
        num = downfile[0].browser + 1
        downfile.update(browser=num)
        return HttpResponse(json.dumps({'info': 'success'}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'info': 'fail'}), content_type="application/json")

def download_album_datail(request, albumname):
    tmpurl = str(request.path).strip('/')
    belong = {'name': '其他', 'slug': 'other'}
    column1 = {'name': '下载', 'slug': 'download'}
    albuminfo = Resourcesclass.objects.filter(slug=albumname)
    album1 = {'name': albuminfo[0].name, 'slug': albumname}
    num = albuminfo[0].browser + 1
    albuminfo.update(browser=num)
    downfile = Resourcearticle.objects.filter(album=albumname, published=True).order_by("-id")
    num = downfile.count()
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='miniao', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from other_standardclass")
    dic1 = dictfetchall(cursor)
    final_list = []
    for i in dic1:
        final_list.append(i)
    final_list.append({u'name': u'下载', u'slug': u'download'})
    if downfile:
        objects, page_range = my_pagination(request, downfile, 2)
        return render(request, 'downfile_detail.html',
                      {'belong': belong, 'column': column1, 'album': album1, 'objects': objects, 'classes': final_list,
                       'page_range': page_range, 'tmpurl': tmpurl, 'albuminfo': albuminfo[0], 'num': num})
    else:
        return HttpResponseRedirect('/')


def download_album(request):
    tmpurl = str(request.path).strip('/')
    belong = {'name': '其他', 'slug': 'other'}
    column_tmp = '下载'
    column1 = {'name': column_tmp, 'slug': 'download'}
    album = Resourcesclass.objects.all()
    albumclass = [i.slug for i in album]
    dic = {}
    for j in albumclass:
        num = Resourcearticle.objects.filter(album=j, published=True).count()
        dic[j] = num
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='miniao', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from other_standardclass")
    dic1 = dictfetchall(cursor)
    final_list = []
    for i in dic1:
        final_list.append(i)
    final_list.append({u'name': u'下载', u'slug': u'download'})
    return render(request, 'video_album.html', {'album': album, 'num': dic, 'belong': belong, 'column': column1, 'classes': final_list, 'tmpurl': tmpurl})






def dictfetchall(cursor):
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]


def index(request):
    tmpurl = str(request.path).strip('/')
    article = Standardarticle.objects.filter(published=True).order_by("-id")
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='miniao', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from other_standardclass")
    dic1 = dictfetchall(cursor)
    final_list = []
    for i in dic1:
        final_list.append(i)
    final_list.append({u'name': u'下载', u'slug': u'download'})
    belong = 'other'
    objects, page_range = my_pagination(request, article, 9)
    return render_to_response('article_index.html', {'objects': objects, 'belong': belong, 'classes': final_list,  'page_range': page_range, 'tmpurl': tmpurl},
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

