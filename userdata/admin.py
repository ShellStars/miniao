from django.contrib import admin

from .models import Userinfo


class UserinfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'telnum', 'email', 'hospital', 'department', 'title', 'identity', 'certificate',
                    'isfgpwd')


admin.site.register(Userinfo, UserinfoAdmin)