from django.contrib import admin

from .models import Infoarticle, Information


class InformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class InfoarticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'author', 'browser', 'pub_date', 'published')
    search_fields = ('title',)


admin.site.register(Information, InformationAdmin)
admin.site.register(Infoarticle, InfoarticleAdmin)