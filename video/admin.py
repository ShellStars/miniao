from django.contrib import admin

from .models import Videoclass, Videoarticle, Videoalbum
from django.utils.safestring import mark_safe


class VideoclassAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class VideoalbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class VideoarticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'author', 'browser', 'pub_date', 'published')
    search_fields = ('title',)


admin.site.register(Videoclass, VideoclassAdmin)
admin.site.register(Videoalbum, VideoalbumAdmin)
admin.site.register(Videoarticle, VideoarticleAdmin)