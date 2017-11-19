from django.contrib import admin

from .models import Standardclass, Standardarticle, Resourcearticle, Resourcesclass, Lunbopic
from django.utils.safestring import mark_safe


class StandardclassAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class ResourcesclassAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


"""class FriendAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image_data')
    readonly_fields = ('image_data',)

    def image_data(self, obj):
        return mark_safe(u'<img src="%s" width="100px" />' % obj.friendimage.url)
    image_data.short_description = 'picture'
"""

class StandardarticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'author', 'browser', 'pub_date', 'published')
    search_fields = ('title',)


class ResourcearticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'update_time', 'published')
    search_fields = ('title', 'author')


class LunbopicAdmin(admin.ModelAdmin):
    list_display = ('lunbopic', 'pub_date', 'published')


admin.site.register(Lunbopic, LunbopicAdmin)
admin.site.register(Standardclass, StandardclassAdmin)
admin.site.register(Resourcesclass, ResourcesclassAdmin)
admin.site.register(Standardarticle, StandardarticleAdmin)
admin.site.register(Resourcearticle, ResourcearticleAdmin)