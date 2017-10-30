from django.contrib import admin

from .models import Nursingclass, Nursingarticle


class NursingclassAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class NursingarticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'author', 'browser', 'pub_date', 'published')
    search_fields = ('title',)


admin.site.register(Nursingclass, NursingclassAdmin)
admin.site.register(Nursingarticle, NursingarticleAdmin)