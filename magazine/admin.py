from django.contrib import admin

from .models import Magearticle, Mageinfo


class MageinfoAdmin(admin.ModelAdmin):
    list_display = ('info',)
    # search_fields = ('title',)


class MagearticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'author', 'browser', 'pub_date', 'published')
    search_fields = ('title',)


admin.site.register(Mageinfo, MageinfoAdmin)
admin.site.register(Magearticle, MagearticleAdmin)
