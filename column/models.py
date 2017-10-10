# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse


@python_2_unicode_compatible
class Information(models.Model):
    name = models.CharField('栏目名称', max_length=256, db_index=True, primary_key=True)
    slug = models.CharField('栏目网址', max_length=256 )

    #def get_absolute_url(self):
    #    return reverse('information', args=(self.name, self.slug ))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '资讯栏目'
        verbose_name_plural = '资讯栏目'
        ordering = ['name']  # 排序


@python_2_unicode_compatible
class Infoarticle(models.Model):
    column = models.ForeignKey(Information, verbose_name='归属栏目')
    title = models.CharField('标题', max_length=256)
    source = models.CharField('来源', max_length=256)
    author = models.CharField('作者', max_length=256)
    browser = models.IntegerField('浏览量')
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
        verbose_name = '资讯'
        verbose_name_plural = '资讯'

