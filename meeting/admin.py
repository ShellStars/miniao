from django.contrib import admin

from .models import Meetname, Meetarticle
from django.utils.safestring import mark_safe


class MeetnameAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class MeetarticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'author', 'browser', 'pub_date', 'published')
    search_fields = ('title',)


admin.site.register(Meetname, MeetnameAdmin)
admin.site.register(Meetarticle, MeetarticleAdmin)