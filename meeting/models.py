# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@python_2_unicode_compatible
class Meetname(models.Model):
    name = models.CharField('栏目名称', max_length=256, db_index=True, primary_key=True)
    slug = models.CharField('栏目网址', max_length=256 )

    #def get_absolute_url(self):
    #    return reverse('information', args=(self.name, self.slug ))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '会议栏目'
        verbose_name_plural = '会议栏目'
        ordering = ['name']  # 排序


@python_2_unicode_compatible
class Meetspecial(models.Model):
    title = models.CharField('专题标题', max_length=256, db_index=True)
    slug = models.CharField('专题网址', max_length=256)
    meetimage = models.ImageField(upload_to='uploads/images/meetspecial/')

    #def get_absolute_url(self):
    #    return reverse('information', args=(self.name, self.slug ))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '会议专题'
        verbose_name_plural = '会议专题'
        ordering = ['title']  # 排序


@python_2_unicode_compatible
class Meetarticle(models.Model):
    column = models.ForeignKey(Meetname, verbose_name='归属栏目')
    title = models.CharField('标题', max_length=256)
    source = models.CharField('来源', max_length=256)
    author = models.CharField('作者', max_length=256)
    browser = models.IntegerField('浏览量')
    content = models.TextField('内容', default='', blank=True)
    content = UEditorField('内容', height=300, width=700,
        default=u'', blank=True, imagePath="uploads/images/meeting/",
        toolbars='besttome', filePath='uploads/files/information/')

    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    published = models.BooleanField('正式发布', default=True)

    #def get_absolute_url(self):
    #    return reverse('infoarticle', args=(self.pk, self.slug))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '会议'
        verbose_name_plural = '会议'

def delete_Meetspecial(sender, instance, **kwargs):
    instance.meetimage.delete(save=False)
models.signals.post_delete.connect(delete_Meetspecial, sender=Meetspecial)

