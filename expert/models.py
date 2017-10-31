# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse


@python_2_unicode_compatible
class Interviewarticle(models.Model):
    column = models.CharField('专访', default='zhuanfang', max_length=10, editable=False)
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
        verbose_name = '专访'
        verbose_name_plural = '专访'


@python_2_unicode_compatible
class Doctorarticle(models.Model):
    column = models.CharField('大家风范', default='fengfan', max_length=10, editable=False)
    midpic = models.ImageField('封面图', upload_to='uploads/images/doctor/')
    name = models.CharField('姓名', max_length=30)
    bigpic = models.ImageField('主图', upload_to='uploads/images/doctor/')
    smallpic = models.ImageField('嘉宾头像', upload_to='uploads/images/doctor/',)
    saying = models.CharField('摘要', max_length=70)
    introduce = models.TextField('文字介绍')
    postscript = models.TextField('编后语')
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


class Videotag(models.Model):
    contact = models.ForeignKey(Doctorarticle, blank=True)
    title = models.CharField('标题', max_length=50, blank=True)
    video = models.FileField('视频', upload_to="uploads/video/doctor/", help_text='mp4only', blank=True)

    def __unicode__(self):
        return self.title


class Articletag(models.Model):
    contact = models.ForeignKey(Doctorarticle)
    title = models.CharField('标题', max_length=50)
    maininfo = models.TextField('内容', default='')

    def __unicode__(self):
        return self.title


class Pictag(models.Model):
    contact = models.ForeignKey(Doctorarticle)
    title = models.CharField('标题', max_length=50)
    pic = models.ImageField('图片', upload_to="uploads/images/doctor/", help_text='jpgonly')

    def __unicode__(self):
        return self.title


@python_2_unicode_compatible
class Expertarticle(models.Model):
    column = models.CharField('专家', default='zhuanjia', max_length=10, editable=False)
    name = models.CharField('姓名', max_length=30)
    ranks = models.CharField('职称', max_length=10)
    province = models.CharField('省份', max_length=10)
    city = models.CharField('城市', max_length=20)
    zan = models.IntegerField('赞', default=0, editable=False)
    hospital = models.CharField('医院', max_length=50)
    department = models.CharField('所在科室', max_length=30)
    midpic = models.ImageField('封面图', upload_to='uploads/images/doctor/')
    smallpic = models.ImageField('专家头像', upload_to='uploads/images/doctor/')
    introduce = models.TextField('文字介绍')
    specialty = models.TextField('技术特长')
    postscript = models.TextField('编后语')
    weixinpic = models.ImageField('微信二维码', upload_to='uploads/images/doctor/', blank=True)
    weibopic = models.ImageField('微博二维码', upload_to='uploads/images/doctor/', blank=True)
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    published = models.BooleanField('正式发布', default=True)

    #def get_absolute_url(self):
    #    return reverse('infoarticle', args=(self.pk, self.slug))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '专家'
        verbose_name_plural = '专家'


@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField('姓名', max_length=30)
    content = models.TextField('评论内容')
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    published = models.BooleanField('审核通过', default=False)

    #def get_absolute_url(self):
    #    return reverse('infoarticle', args=(self.pk, self.slug))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '审核'
        verbose_name_plural = '审核'






