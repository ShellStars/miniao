# coding:utf8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.shortcuts import render, render_to_response
from .models import Universalarticle
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext, loader, Context
# Create your views here.


def article_detail(request, column, pk):
    article = Universalarticle.objects.filter(pk=pk, column=column, published=True)
    if article:
        num = article[0].browser + 1
        article.update(browser=num)
        return render(request, 'article.html', {'article': article[0]})
    else:
        return HttpResponseRedirect('/')


def article(request, column):
    article = Universalarticle.objects.filter(column=column, published=True)
    if article:
        objects, page_range = my_pagination(request, article, 2)
        return render_to_response('article1.html', {'objects':objects,'page_range':page_range},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')

def index(request):
    article = Universalarticle.objects.filter(column='gonggao', published=True)[0:3]
    if article:
        return render(request, 'article2.html', {'article': article})
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

