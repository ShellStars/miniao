# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse
from bs4 import BeautifulSoup


@python_2_unicode_compatible
class Assocclass(models.Model):
    name = models.CharField('学会名称', max_length=20)
    slug = models.CharField('学会网址', max_length=30, db_index=True, primary_key=True)

    #def get_absolute_url(self):
    #    return reverse('information', args=(self.name, self.slug ))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '学会栏目'
        verbose_name_plural = '学会栏目'
        ordering = ['name']  # 排序

@python_2_unicode_compatible
class Peoplearticle(models.Model):
    Area_Level = (
        (0, u'主委'),
        (1, u'副主委'),
        (2, u'会员'),
    )
    # column = models.ForeignKey(Peopleclass, verbose_name='归属栏目')
    assoccolumn = models.ForeignKey(Assocclass, verbose_name='所属学会')
    level = models.IntegerField(choices=Area_Level, verbose_name='等级')
    name = models.CharField('姓名', max_length=30)
    pic = models.ImageField('头像', upload_to='uploads/images/doctor/')
    hospital = models.CharField('医院', max_length=70)
    introduce = models.TextField('简介', default='', blank=True)
    specialty = models.TextField('技术特长', default='', blank=True)
    postscript = models.TextField('编后语', default='', blank=True)
    url = models.CharField('链接地址', max_length=100, default='')
    weixinpic = models.ImageField('微信二维码', upload_to='uploads/images/doctor/', blank=True)
    weibopic = models.ImageField('微博二维码', upload_to='uploads/images/doctor/', blank=True)

    #def get_absolute_url(self):
    #    return reverse('infoarticle', args=(self.pk, self.slug))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '编委'
        verbose_name_plural = '编委'


@python_2_unicode_compatible
class Assocarticle(models.Model):
    assoccolumn = models.ForeignKey(Assocclass, verbose_name='所属学会')
    associntro = models.TextField('学会简介', default='')
    constitution = models.TextField('章程', default='')
    pic = models.ImageField('会徽', upload_to='uploads/images/doctor/')
    picintro = models.TextField('会徽简介', default='')
    url = models.CharField('网址链接', max_length=100, default='')
    weixinpic = models.ImageField('微信二维码', upload_to='uploads/images/doctor/')
    weibopic = models.ImageField('微博二维码', upload_to='uploads/images/doctor/')

    #def get_absolute_url(self):
    #    return reverse('infoarticle', args=(self.pk, self.slug))

    def __str__(self):
        return self.picintro

    class Meta:
        verbose_name = '学会简介'
        verbose_name_plural = '学会简介'



@python_2_unicode_compatible
class Dynamicarticle(models.Model):
    assoccolumn = models.ForeignKey(Assocclass, verbose_name='所属学会')
    column = models.CharField('动态', default='dongtai', max_length=10, editable=False)
    title = models.CharField('标题', max_length=40)
    source = models.CharField('来源', max_length=20)
    author = models.CharField('作者', max_length=20)
    browser = models.IntegerField('浏览量', default=0, editable=False)
    keyword = models.CharField('关键词', max_length=30, blank=True)
    tag = models.CharField('标签', max_length=30, blank=True)
    content = models.TextField('内容', default='', blank=True)
    content = UEditorField('内容', height=300, width=700,
        default=u'', blank=True, imagePath="uploads/images/article/",
        toolbars='besttome', filePath='uploads/files/article/')
    def fengmian(self):
        html = self.content
        soup = BeautifulSoup(html, "html.parser")
        try:
            picurl = soup.img["src"]
        except:
            picurl = "/media/defaultpic.jpg"
        return picurl
    picurl = property(fengmian)
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    published = models.BooleanField('正式发布', default=True)

    #def get_absolute_url(self):
    #    return reverse('infoarticle', args=(self.pk, self.slug))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '动态'
        verbose_name_plural = '动态'



