from django.contrib import admin

from .models import Magearticle

class MagearticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'author', 'browser', 'pub_date', 'published')
    search_fields = ('title',)


admin.site.register(Magearticle, MagearticleAdmin)
