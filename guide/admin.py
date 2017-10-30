from django.contrib import admin

from .models import Guideclass, Guidearticle


class GuideclassAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class GuidearticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'author', 'browser', 'pub_date', 'published')
    search_fields = ('title',)


admin.site.register(Guideclass, GuideclassAdmin)
admin.site.register(Guidearticle, GuidearticleAdmin)