from django.contrib import admin

from .models import Articleclass, Artiarticle


class ArticleclassAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class ArtiarticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'author', 'browser', 'pub_date', 'published')
    search_fields = ('title',)


admin.site.register(Articleclass, ArticleclassAdmin)
admin.site.register(Artiarticle, ArtiarticleAdmin)