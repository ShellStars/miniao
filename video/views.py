# coding:utf8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.shortcuts import render, render_to_response
from .models import Videoarticle, Videoclass, Videoalbum
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext, loader, Context
import pymysql
# Create your views here.


def video_detail(request, column, pk):
    if "userid" in request.session and "identity" in request.session:
        identity = request.session.get("identity")
        if identity == 0 or identity == 1 or identity == 2:
            url = request.path.strip('/')
            # url = 'http://127.0.0.1:8000' + request.path
            tmpurl = '/'.join(str(request.path).split('/')[:-1]) + '/'
            video = Videoarticle.objects.filter(pk=pk, column=column, published=True)
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='miniao', charset='utf8')
            cursor = conn.cursor()
            cursor.execute("select * from video_videoclass")
            dic1 = dictfetchall(cursor)
            final_list = []
            for i in dic1:
                final_list.append(i)
            final_list.append({u'name': u'专辑', u'slug': u'zhuanji'})
            relate = Videoarticle.objects.filter(column=column, published=True)[0:2]
            pre_article = Videoarticle.objects.filter(id__lt=pk, published=True)
            if pre_article:
                pre_article = pre_article.order_by('-id')[0]
            else:
                pre_article = Videoarticle.objects.filter(id=pk, published=True)[0]
            next_article = Videoarticle.objects.filter(id__gt=pk, published=True)
            if next_article:
                next_article = next_article[0]
            else:
                next_article = Videoarticle.objects.filter(id=pk, published=True)[0]
            belong = {'name': '视频', 'slug': 'video'}
            column_tmp = Videoclass.objects.filter(slug=column)[0].name
            column1 = {'name': column_tmp, 'slug': column}
            if video:
                num = video[0].browser + 1
                video.update(browser=num)
                conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='miniao',
                                       charset='utf8')
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
                    return render(request, 'video_detail.html',
                                  {'pre_article': pre_article, 'next_article': next_article, 'belong': belong,
                                   'classes': final_list, 'column': column1, 'video': video[0], 'tmpurl': tmpurl,
                                   'relate': relate, 'collect': collect, 'avgnum': avgnum,
                                   'scorenum': scorenum})
                else:
                    return render(request, 'video_detail.html',
                                  {'pre_article': pre_article, 'next_article': next_article, 'belong': belong,
                                   'classes': final_list, 'column': column1, 'video': video[0], 'tmpurl': tmpurl,
                                   'relate': relate, 'avgnum': avgnum})
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def video_album_datail(request, albumname):
    tmpurl = str(request.path).strip('/')
    belong = {'name': '视频', 'slug': 'video'}
    column1 = {'name': '专辑', 'slug': 'zhuanji'}
    albuminfo = Videoalbum.objects.filter(slug=albumname)
    album1 = {'name': albuminfo[0].name, 'slug': albumname}
    num = albuminfo[0].browser + 1
    albuminfo.update(browser=num)
    video = Videoarticle.objects.filter(album=albumname, published=True).order_by("-id")
    num = video.count()
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='miniao', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from video_videoclass")
    dic1 = dictfetchall(cursor)
    final_list = []
    for i in dic1:
        final_list.append(i)
    final_list.append({u'name': u'专辑', u'slug': u'zhuanji'})
    objects, page_range = my_pagination(request, video, 15)
    return render(request, 'video_album_detail.html',
                      {'belong': belong, 'column': column1, 'album': album1, 'objects': objects, 'classes': final_list,
                       'page_range': page_range, 'tmpurl': tmpurl, 'albuminfo': albuminfo[0], 'num': num})


def video_album(request):
    tmpurl = str(request.path).strip('/')
    belong = {'name': '视频', 'slug': 'video'}
    column_tmp = '专辑'
    column1 = {'name': column_tmp, 'slug': 'zhuanji'}
    album = Videoalbum.objects.all()
    albumclass = [i.slug for i in album]
    dic = {}
    for j in albumclass:
        num = Videoarticle.objects.filter(album=j, published=True).count()
        dic[j] = num
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='miniao', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from video_videoclass")
    dic1 = dictfetchall(cursor)
    final_list = []
    for i in dic1:
        final_list.append(i)
    final_list.append({u'name': u'专辑', u'slug': u'zhuanji'})
    return render(request, 'video_album.html', {'album': album, 'num': dic, 'belong': belong, 'column': column1, 'classes': final_list, 'tmpurl': tmpurl})


def video(request, column):
    tmpurl = str(request.path).strip('/')
    belong = {'name': '视频', 'slug': 'video'}
    column_tmp = Videoclass.objects.filter(slug=column)[0].name
    column1 = {'name': column_tmp, 'slug': column}
    tmp = request.GET.keys()
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='miniao', charset='utf8')
    cursor = conn.cursor()
    small_classes = {}
    if 'page' in tmp:
        tmp.remove('page')
    dic = []
    if len(tmp) == 0:
        cursor.execute("select * from video_videoarticle where column_id='%s' and published=True order by id desc" % column)
        dic = dictfetchall(cursor)
    elif len(tmp) == 1:
        tmp_key1 = str(tmp[0])
        tmp_val1 = request.GET[tmp_key1]
        cursor.execute("select * from video_videoarticle where %s='%s' and published=True and column_id='%s' order by id desc" % (tmp_key1, tmp_val1, column))
        dic = dictfetchall(cursor)
        for i in request.GET.items():
            small_classes[i[0]] = i[1]
    elif len(tmp) == 2:
        tmp_key1 = str(tmp[0])
        tmp_val1 = request.GET[tmp_key1]
        tmp_key2 = str(tmp[1])
        tmp_val2 = request.GET[tmp_key2]
        cursor.execute("select * from video_videoarticle where %s='%s' and %s='%s' and published=True and column_id='%s' order by id desc" % (
        tmp_key1, tmp_val1, tmp_key2, tmp_val2, column))
        dic = dictfetchall(cursor)
        for i in request.GET.items():
            small_classes[i[0]] = i[1]
    elif len(tmp) == 3:
        tmp_key1 = str(tmp[0])
        tmp_val1 = request.GET[tmp_key1]
        tmp_key2 = str(tmp[1])
        tmp_val2 = request.GET[tmp_key2]
        tmp_key3 = str(tmp[2])
        tmp_val3 = request.GET[tmp_key3]
        cursor.execute("select * from video_videoarticle where %s='%s' and %s='%s' and %s='%s' and published=True and column_id='%s' order by id desc" % (
            tmp_key1, tmp_val1, tmp_key2, tmp_val2, tmp_key3, tmp_val3, column))
        dic = dictfetchall(cursor)
        for i in request.GET.items():
            small_classes[i[0]] = i[1]
    elif len(tmp) == 4:
        tmp_key1 = str(tmp[0])
        tmp_val1 = request.GET[tmp_key1]
        tmp_key2 = str(tmp[1])
        tmp_val2 = request.GET[tmp_key2]
        tmp_key3 = str(tmp[2])
        tmp_val3 = request.GET[tmp_key3]
        tmp_key4 = str(tmp[3])
        tmp_val4 = request.GET[tmp_key4]
        cursor.execute(
            "select * from video_videoarticle where %s='%s' and %s='%s' and %s='%s' and %s='%s' and published=True and column_id='%s' order by id desc" % (
                tmp_key1, tmp_val1, tmp_key2, tmp_val2, tmp_key3, tmp_val3, tmp_key4, tmp_val4, column))
        dic = dictfetchall(cursor)
        for i in request.GET.items():
            small_classes[i[0]] = i[1]
            # article = Videoarticle.objects.filter(tmp_key1=tmp_val1, published=True)
    res = cursor.execute("select distinct disease from video_videoarticle where column_id='%s'" % column)
    row = cursor.fetchmany(res)
    disease = []
    for i in row:
        disease.append(str(i[0]))
    res1 = cursor.execute("select distinct difficulty from video_videoarticle where column_id='%s'" % column)
    row1 = cursor.fetchmany(res1)
    difficulty = []
    for i in row1:
        difficulty.append(str(i[0]))
    res2 = cursor.execute("select distinct other from video_videoarticle where column_id='%s'" % column)
    row2 = cursor.fetchmany(res2)
    other = []
    for i in row2:
        other.append(str(i[0]))
    res3 = cursor.execute("select distinct expert from video_videoarticle where column_id='%s'" % column)
    row3 = cursor.fetchmany(res3)
    expert = []
    for i in row3:
        expert.append(str(i[0]))
    cursor.execute("select * from video_videoclass")
    dic1 = dictfetchall(cursor)
    final_list = []
    for i in dic1:
        final_list.append(i)
    final_list.append({u'name': u'专辑', u'slug': u'zhuanji'})
    large_classes = [{'name_zh': '疾病分类', 'name_en': 'disease'}, {'name_zh': '难度分级', 'name_en': 'difficulty'},
                     {'name_zh': '专家专栏', 'name_en': 'expert'}, {'name_zh': '其他', 'name_en': 'other'}]
    # article = Videoarticle.objects.filter(column='gonggao', published=True)[0:3]
    objects, page_range = my_pagination(request, dic, 15)
    return render(request, 'video_column.html',
                      {'disease': disease, 'difficulty': difficulty, 'other': other, 'expert': expert, 'belong': belong, 'column': column1, 'objects': objects, 'classes': final_list, 'page_range': page_range, 'tmpurl': tmpurl,
                       'large_classes': large_classes, 'small_classes': small_classes})



def dictfetchall(cursor):
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]


def index(request):
    tmpurl = str(request.path).strip('/')
    tmp = request.GET.keys()
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='miniao', charset='utf8')
    cursor = conn.cursor()
    small_classes = {}
    if 'page' in tmp:
        tmp.remove('page')
    dic = []
    if len(tmp) == 0:
        cursor.execute("select * from video_videoarticle where published=True order by id desc")
        dic = dictfetchall(cursor)
    elif len(tmp) == 1:
        tmp_key1 = str(tmp[0])
        tmp_val1 = request.GET[tmp_key1]
        cursor.execute("select * from video_videoarticle where %s='%s' and published=True order by id desc" % (tmp_key1, tmp_val1))
        dic = dictfetchall(cursor)
        for i in request.GET.items():
            small_classes[i[0]] = i[1]
    elif len(tmp) == 2:
        tmp_key1 = str(tmp[0])
        tmp_val1 = request.GET[tmp_key1]
        tmp_key2 = str(tmp[1])
        tmp_val2 = request.GET[tmp_key2]
        cursor.execute("select * from video_videoarticle where %s='%s' and %s='%s' and published=True order by id desc" % (tmp_key1, tmp_val1, tmp_key2, tmp_val2))
        dic = dictfetchall(cursor)
        for i in request.GET.items():
            small_classes[i[0]] = i[1]
    elif len(tmp) == 3:
        tmp_key1 = str(tmp[0])
        tmp_val1 = request.GET[tmp_key1]
        tmp_key2 = str(tmp[1])
        tmp_val2 = request.GET[tmp_key2]
        tmp_key3 = str(tmp[2])
        tmp_val3 = request.GET[tmp_key3]
        cursor.execute("select * from video_videoarticle where %s='%s' and %s='%s' and %s='%s' and published=True order by id desc" % (
        tmp_key1, tmp_val1, tmp_key2, tmp_val2, tmp_key3, tmp_val3))
        dic = dictfetchall(cursor)
        for i in request.GET.items():
            small_classes[i[0]] = i[1]
    elif len(tmp) == 4:
        tmp_key1 = str(tmp[0])
        tmp_val1 = request.GET[tmp_key1]
        tmp_key2 = str(tmp[1])
        tmp_val2 = request.GET[tmp_key2]
        tmp_key3 = str(tmp[2])
        tmp_val3 = request.GET[tmp_key3]
        tmp_key4 = str(tmp[3])
        tmp_val4 = request.GET[tmp_key4]
        cursor.execute("select * from video_videoarticle where %s='%s' and %s='%s' and %s='%s' and %s='%s' and published=True order by id desc" % (
                    tmp_key1, tmp_val1, tmp_key2, tmp_val2, tmp_key3, tmp_val3, tmp_key4, tmp_val4))
        dic = dictfetchall(cursor)
        for i in request.GET.items():
            small_classes[i[0]] = i[1]
        # article = Videoarticle.objects.filter(tmp_key1=tmp_val1, published=True)
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
    cursor.execute("select * from video_videoclass")
    dic1 = dictfetchall(cursor)
    final_list = []
    for i in dic1:
        final_list.append(i)
    final_list.append({u'name': u'专辑', u'slug': u'zhuanji'})
    large_classes = [{'name_zh': '疾病分类', 'name_en': 'disease'}, {'name_zh': '难度分级', 'name_en': 'difficulty'},
                       {'name_zh': '专家专栏', 'name_en': 'expert'}, {'name_zh': '其他', 'name_en': 'other'}]
    # article = Videoarticle.objects.filter(column='gonggao', published=True)[0:3]
    objects, page_range = my_pagination(request, dic, 15)
    return render(request, 'video_index.html', {'disease': disease, 'difficulty': difficulty, 'other': other, 'expert': expert, 'objects': objects, 'classes': final_list, 'page_range': page_range, 'tmpurl': tmpurl, 'large_classes': large_classes, 'small_classes': small_classes})

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

