from django.contrib import admin

from .models import Userinfo


class UserinfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'sex', 'telnum', 'identity', 'integralnum', 'addtime', 'ispass', 'isfgpwd')


admin.site.register(Userinfo, UserinfoAdmin)