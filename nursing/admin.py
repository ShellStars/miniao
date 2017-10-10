from django.contrib import admin

from .models import Nursingclass, Nursingarticle


class NursingclassAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class NursingarticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'update_time', 'published')
    search_fields = ('title', 'author')


admin.site.register(Nursingclass, NursingclassAdmin)
admin.site.register(Nursingarticle, NursingarticleAdmin)