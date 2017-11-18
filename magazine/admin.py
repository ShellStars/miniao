from django.contrib import admin

from .models import Magearticle, Mageinfo, Magaclass


class MagaclassAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class MageinfoAdmin(admin.ModelAdmin):
    list_display = ('magacolumn', 'info',)
    # search_fields = ('title',)


class MagearticleAdmin(admin.ModelAdmin):
    list_display = ('magacolumn', 'title', 'column', 'author', 'browser', 'pub_date', 'published')
    search_fields = ('title',)


admin.site.register(Magaclass, MagaclassAdmin)
admin.site.register(Mageinfo, MageinfoAdmin)
admin.site.register(Magearticle, MagearticleAdmin)
