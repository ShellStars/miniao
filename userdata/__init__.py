# coding:utf-8
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from userdata.models import Userinfo
from .views import sendpass
@receiver(post_init, sender=Userinfo)
def post_init_func(instance, sender, **kwargs):
    instance.__original = instance.ispass
@receiver(post_save, sender=Userinfo)
def post_save_func(instance, sender,**kwargs):
    if instance.__original == False and instance.ispass == True:
        telnum = instance.telnum
        username = instance.username
        sendpass(telnum, username)
