# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse


@python_2_unicode_compatible
class Srucoclass(models.Model):
    name = models.CharField('栏目名称', max_length=20)
    slug = models.CharField('栏目网址', max_length=30, db_index=True, primary_key=True)

    #def get_absolute_url(self):
    #    return reverse('information', args=(self.name, self.slug ))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SRUCO栏目'
        verbose_name_plural = 'SRUCO栏目'
        ordering = ['name']  # 排序


@python_2_unicode_compatible
class Srucoarticle(models.Model):
    column = models.ForeignKey(Srucoclass, verbose_name='归属栏目')
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

    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    published = models.BooleanField('正式发布', default=True)

    #def get_absolute_url(self):
    #    return reverse('infoarticle', args=(self.pk, self.slug))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'SRUCO'
        verbose_name_plural = 'SRUCO'
