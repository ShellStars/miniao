from django.contrib import admin

from .models import Srucoclass, Srucoarticle


class SrucoclassAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class SrucoarticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'author', 'browser', 'pub_date', 'published')
    search_fields = ('title',)


admin.site.register(Srucoclass, SrucoclassAdmin)
admin.site.register(Srucoarticle, SrucoarticleAdmin)