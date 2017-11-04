# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@python_2_unicode_compatible
class Userinfo(models.Model):
    Level = (
        (0, u'医生'),
        (1, u'护士'),
        (2, u'学生'),
        (3, u'其它'),
    )
    username = models.CharField('真实姓名', max_length=30)
    sex = models.IntegerField('性别')
    headimg = models.FileField('头像', upload_to='/uploads/images/userdata/', default='/media/uploads/images/userdata/defaultuser.png')
    telnum = models.CharField('手机号', null=False, db_index=True, max_length=15)
    hospital = models.CharField('所在医院', max_length=70, blank=True)
    department = models.CharField('所在科室', max_length=30, blank=True)
    title = models.CharField('医师职称', max_length=30, blank=True)
    password = models.CharField('密码', max_length=30, editable=False)
    identity = models.IntegerField(choices=Level, verbose_name='身份')
    certificate = models.FileField('证书', upload_to='/uploads/images/certificate/', blank=True)
    integralnum = models.IntegerField('积分', default=0, editable=False)
    ispass = models.BooleanField('审核通过', default=False)
    addtime = models.DateTimeField('创建时间', auto_now_add=True, editable=True)
    isfgpwd = models.BooleanField('忘记密码', default=False, editable=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
        ordering = ['username']  # 排序


class Checknum(models.Model):
    telnum = models.CharField('手机号', null=False, db_index=True, max_length=15)
    checknum = models.CharField('短信验证码', null=True, blank=True, max_length=10)


class Favourite(models.Model):
    userid = models.IntegerField('用户id', null=False)
    title = models.CharField('标题名称', max_length=50)
    url = models.URLField('链接地址', max_length=100)
    addtime = models.DateTimeField('收藏时间', auto_now_add=True, editable=True)


class Score(models.Model):
    userid = models.IntegerField('用户id', null=False)
    url = models.URLField('链接地址')
    scorenum = models.CharField('打分', max_length=3)

