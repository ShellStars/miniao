# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from storage import ContentTypeRestrictedFileField
from DjangoUeditor.models import UEditorField
from bs4 import BeautifulSoup


@python_2_unicode_compatible
class Videoclass(models.Model):
    name = models.CharField('栏目名称', max_length=20)
    slug = models.CharField('栏目网址', max_length=30, db_index=True, primary_key=True)

    #def get_absolute_url(self):
    #    return reverse('information', args=(self.name, self.slug ))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '视频栏目'
        verbose_name_plural = '视频栏目'
        ordering = ['name']  # 排序


@python_2_unicode_compatible
class Videoalbum(models.Model):
    name = models.CharField('专辑名称', max_length=20)
    slug = models.CharField('专辑网址', max_length=30, db_index=True, primary_key=True)
    intro = models.TextField('专辑简介', default='')
    pic = models.ImageField('封面', upload_to="uploads/images/video/")
    browser = models.IntegerField('访问量', default=0, editable=False)

    #def get_absolute_url(self):
    #    return reverse('information', args=(self.name, self.slug ))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '专辑栏目'
        verbose_name_plural = '专辑栏目'
        ordering = ['name']  # 排序

@python_2_unicode_compatible
class Videoarticle(models.Model):
    Level = (
        ('初级', u'初级'),
        ('中级', u'中级'),
        ('高级', u'高级'),
    )
    column = models.ForeignKey(Videoclass, verbose_name='归属栏目')
    title = models.CharField('标题', max_length=40)
    source = models.CharField('来源', max_length=20)
    author = models.CharField('作者', max_length=20)
    browser = models.IntegerField('浏览量', default=0, editable=False)
    disease = models.CharField('疾病分类', max_length=20, blank=True)
    difficulty = models.CharField(choices=Level, verbose_name='难度等级', max_length=10)
    album = models.ForeignKey(Videoalbum, verbose_name='归属专辑')
    expert = models.CharField('专家名称', max_length=20)
    other = models.CharField('其他', max_length=20, blank=True)
    zan = models.IntegerField('赞', default=0, editable=False)
    # smallpic = models.ImageField('封面', upload_to="uploads/images/video/")
    content1 = models.TextField('封面', default='')
    content1 = UEditorField('封面', height=300, width=700,
                            default=u'', imagePath="uploads/images/video/",
                            toolbars='imageonly', filePath='uploads/files/video/')

    def fengmian1(self):
        html = self.content1
        soup = BeautifulSoup(html, "html.parser")
        try:
            smallpic = soup.img["src"]
        except:
            smallpic = ""
        return smallpic

    smallpic = property(fengmian1)
    introduction = models.TextField('简介', default='', blank=True)
    #video = models.FileField('视频', upload_to='uploads/files/video/')
    #video = ContentTypeRestrictedFileField(
    #    verbose_name='视频',
    #    upload_to='uploads/files/video/',
    #    content_types=['video/mp4'],
    #    max_upload_size=429916160,
    #)
    content = models.TextField('视频', default='')
    content = UEditorField('视频', height=300, width=700,
                           default=u'', imagePath="uploads/images/article/",
                           toolbars='videoonly', filePath='uploads/files/video/')

    def fengmian(self):
        html = self.content
        soup = BeautifulSoup(html, "html.parser")
        try:
            video = soup.video["src"]
        except:
            video = ""
        return video
    video = property(fengmian)
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    published = models.BooleanField('正式发布', default=True)

    #def get_absolute_url(self):
    #    return reverse('infoarticle', args=(self.pk, self.slug))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = '视频'
