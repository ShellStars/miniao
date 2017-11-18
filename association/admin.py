from django.contrib import admin

from .models import Peoplearticle, Assocarticle, Dynamicarticle, Assocclass


class AssocclassAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class PeoplearticleAdmin(admin.ModelAdmin):
    list_display = ('assoccolumn', 'level', 'name', 'hospital')

class AssocarticleAdmin(admin.ModelAdmin):
    list_display = ('assoccolumn', 'associntro',)

class DynamicarticleAdmin(admin.ModelAdmin):
    list_display = ('assoccolumn', 'title', 'column', 'author', 'browser', 'pub_date', 'published')
    search_fields = ('title',)


admin.site.register(Assocclass, AssocclassAdmin)
admin.site.register(Peoplearticle, PeoplearticleAdmin)
admin.site.register(Assocarticle, AssocarticleAdmin)
admin.site.register(Dynamicarticle, DynamicarticleAdmin)