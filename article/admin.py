from django.contrib import admin

from .models import Articleclass, Artiarticle


class ArticleclassAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class ArtiarticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'update_time', 'published')
    search_fields = ('title', 'author')


admin.site.register(Articleclass, ArticleclassAdmin)
admin.site.register(Artiarticle, ArtiarticleAdmin)