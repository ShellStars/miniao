from django.contrib import admin

from .models import Peoplearticle, Assocarticle, Dynamicarticle



class PeoplearticleAdmin(admin.ModelAdmin):
    list_display = ('level', 'name', 'hospital')

class AssocarticleAdmin(admin.ModelAdmin):
    list_display = ('associntro',)

class DynamicarticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'author', 'browser', 'pub_date', 'published')
    search_fields = ('title',)


admin.site.register(Peoplearticle, PeoplearticleAdmin)
admin.site.register(Assocarticle, AssocarticleAdmin)
admin.site.register(Dynamicarticle, DynamicarticleAdmin)