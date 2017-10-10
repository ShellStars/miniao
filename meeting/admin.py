from django.contrib import admin

from .models import Meetname, Meetarticle, Meetspecial
from django.utils.safestring import mark_safe


class MeetnameAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class MeetspecialAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image_data')
    readonly_fields = ('image_data',)

    def image_data(self, obj):
        return mark_safe(u'<img src="%s" width="100px" />' % obj.meetimage.url)
    image_data.short_description = 'picture'


class MeetarticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'update_time', 'published')
    search_fields = ('title', 'author')


admin.site.register(Meetname, MeetnameAdmin)
admin.site.register(Meetspecial, MeetspecialAdmin)
admin.site.register(Meetarticle, MeetarticleAdmin)