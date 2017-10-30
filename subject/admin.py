from django.contrib import admin

from .models import Subjectclass, Subjectarticle


class SubjectclassAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class SubjectarticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'author', 'browser', 'pub_date', 'published')
    search_fields = ('title',)


admin.site.register(Subjectclass, SubjectclassAdmin)
admin.site.register(Subjectarticle, SubjectarticleAdmin)