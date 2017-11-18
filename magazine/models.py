# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse


@python_2_unicode_compatible
class Magaclass(models.Model):
    name = models.CharField('杂志名称', max_length=20)
    slug = models.CharField('杂志网址', max_length=30, db_index=True, primary_key=True)

    #def get_absolute_url(self):
    #    return reverse('information', args=(self.name, self.slug ))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '杂志栏目'
        verbose_name_plural = '杂志栏目'
        ordering = ['name']  # 排序


@python_2_unicode_compatible
class Mageinfo(models.Model):
    magacolumn = models.ForeignKey(Magaclass, verbose_name='所属杂志')
    info = models.TextField('杂志简介', default='')
    pic = models.ImageField('杂志徽章', upload_to='uploads/images/article/')

    #def get_absolute_url(self):
    #    return reverse('infoarticle', args=(self.pk, self.slug))

    def __str__(self):
        return self.info

    class Meta:
        verbose_name = '杂志简介'
        verbose_name_plural = '杂志简介'

@python_2_unicode_compatible
class Magearticle(models.Model):
    magacolumn = models.ForeignKey(Magaclass, verbose_name='所属杂志')
    column = models.CharField('动态', default='dongtai', max_length=10, editable=False)
    title = models.CharField('标题', max_length=40)
    source = models.CharField('来源', max_length=20)
    author = models.CharField('作者', max_length=20)
    browser = models.IntegerField('浏览量', default=0, editable=False)
    keyword = models.CharField('关键词', max_length=30, blank=True)
    tag = models.CharField('标签', max_length=30, blank=True)
    picurl = models.ImageField('封面图片', upload_to="uploads/images/article/")
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
        verbose_name = '动态'
        verbose_name_plural = '动态'