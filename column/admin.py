from django.contrib import admin

from .models import Infoarticle, Information


class InformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class InfoarticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'update_time', 'published')
    search_fields = ('title', 'author')


admin.site.register(Information, InformationAdmin)
admin.site.register(Infoarticle, InfoarticleAdmin)