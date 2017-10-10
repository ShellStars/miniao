from django.contrib import admin

from .models import Interviewclass, Interviewarticle, Doctorarticle


class InterviewclassAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class InterviewarticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'update_time', 'published')
    search_fields = ('title', 'author')


class DoctorarticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date', 'update_time', 'published')
    search_fields = ('name',)


admin.site.register(Interviewclass, InterviewclassAdmin)
admin.site.register(Interviewarticle, InterviewarticleAdmin)
admin.site.register(Doctorarticle, DoctorarticleAdmin)
