from django.contrib import admin

from .models import Guideclass, Guidearticle


class GuideclassAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class GuidearticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'update_time', 'published')
    search_fields = ('title', 'author')


admin.site.register(Guideclass, GuideclassAdmin)
admin.site.register(Guidearticle, GuidearticleAdmin)