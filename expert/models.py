# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse


@python_2_unicode_compatible
class Interviewclass(models.Model):
    name = models.CharField('栏目名称', max_length=256, db_index=True, primary_key=True)
    slug = models.CharField('栏目网址', max_length=256 )

    #def get_absolute_url(self):
    #    return reverse('information', args=(self.name, self.slug ))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '专家风采栏目'
        verbose_name_plural = '专家风采栏目'
        ordering = ['name']  # 排序


@python_2_unicode_compatible
class Interviewarticle(models.Model):
    column = models.ForeignKey(Interviewclass, verbose_name='归属栏目')
    title = models.CharField('标题', max_length=256)
    source = models.CharField('来源', max_length=256)
    author = models.CharField('作者', max_length=256)
    browser = models.IntegerField('浏览量', default=0)
    content = models.TextField('内容', default='', blank=True)
    content = UEditorField('内容', height=300, width=700,
        default=u'', blank=True, imagePath="uploads/images/information/",
        toolbars='besttome', filePath='uploads/files/information/')

    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    published = models.BooleanField('正式发布', default=True)

    #def get_absolute_url(self):
    #    return reverse('infoarticle', args=(self.pk, self.slug))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '专访'
        verbose_name_plural = '专访'


@python_2_unicode_compatible
class Doctorarticle(models.Model):
    midpic = models.ImageField('封面图', upload_to='uploads/images/doctor/')
    name = models.CharField('姓名', max_length=256)
    bigpic = models.ImageField('标题图', upload_to='uploads/images/doctor/')
    smallpic = models.ImageField('头像', upload_to='uploads/images/doctor/',)
    saying = models.CharField('警言', max_length=256)
    introduce = models.TextField('简介')
    content = models.TextField('内容', default='', blank=True)
    content = UEditorField('内容', height=300, width=700,
        default=u'', blank=True, imagePath="uploads/images/information/",
        toolbars='besttome', filePath='uploads/files/information/')
    selfimage = models.TextField('图片', default='', blank=True)
    selfimage = UEditorField('图片', height=300, width=700,
                           default=u'', blank=True, imagePath="uploads/images/doctor/",
                           toolbars='besttome', filePath='uploads/files/doctor/')

    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    published = models.BooleanField('正式发布', default=True)

    #def get_absolute_url(self):
    #    return reverse('infoarticle', args=(self.pk, self.slug))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '大家风范'
        verbose_name_plural = '大家风范'

