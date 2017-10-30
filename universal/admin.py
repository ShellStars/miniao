from django.contrib import admin

from .models import Universalclass, Universalarticle


class UniversalclassAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class UniversalarticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'author', 'pub_date', 'update_time', 'published')
    search_fields = ('title', 'author')


admin.site.register(Universalclass, UniversalclassAdmin)
admin.site.register(Universalarticle, UniversalarticleAdmin)