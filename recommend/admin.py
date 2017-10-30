from django.contrib import admin

from .models import Recommendclass, Recommendarticle


class RecommendclassAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class RecommendarticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'author', 'browser', 'pub_date', 'published')
    search_fields = ('title',)


admin.site.register(Recommendclass, RecommendclassAdmin)
admin.site.register(Recommendarticle, RecommendarticleAdmin)