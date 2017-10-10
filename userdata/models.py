# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@python_2_unicode_compatible
class Userinfo(models.Model):
    name = models.CharField('真实姓名', max_length=256)
    sex = models.CharField('性别', max_length=50)
    telnum = models.IntegerField('手机号', null=False, db_index=True, unique=True)
    email = models.EmailField('电子邮箱')
    hospital = models.CharField('所在医院', max_length=256)
    department = models.CharField('所在科室', max_length=256)
    title = models.CharField('医师职称', max_length=256)
    password = models.CharField('密码', max_length=256)
    identity = models.CharField('身份', max_length=256)
    certificate = models.FileField('证书', upload_to=BASE_DIR + '/media/uploads/images/certificate/', max_length=256)
    addtime = models.DateTimeField('创建时间', auto_now_add=True, editable=True)
    isfgpwd = models.BooleanField('忘记密码', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
        ordering = ['name']  # 排序


class Checknum(models.Model):
    telnum = models.IntegerField('手机号', null=False, db_index=True, unique=True  )
    checknum = models.IntegerField('短信验证码', null=True, blank=True)