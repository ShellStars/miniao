# coding:utf8
from django.contrib import admin

from .models import Interviewarticle, Doctorarticle, Videotag, Articletag, Pictag, Expertarticle, Comment


class VideotagInline(admin.TabularInline):
    model = Videotag
    extra = 0
    can_delete = False
    verbose_name = '视频'
    verbose_name_plural = '视频集锦'


class ArticletagInline(admin.TabularInline):
    model = Articletag
    extra = 0
    can_delete = False
    verbose_name = '文章'
    verbose_name_plural = '专家说'


class PictagInline(admin.TabularInline):
    model = Pictag
    extra = 0
    can_delete = False
    verbose_name = '图片'
    verbose_name_plural = '嘉宾风采'



class InterviewarticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'update_time', 'published')
    search_fields = ('title', 'author')


class DoctorarticleAdmin(admin.ModelAdmin):
    inlines = [VideotagInline, ArticletagInline, PictagInline]  # Inline
    fieldsets = (
        ['Main', {
            'fields': ('midpic', 'name', 'bigpic', 'smallpic', 'saying', 'introduce', 'postscript'),
        }],

    )
    list_display = ('name', 'pub_date', 'published')
    search_fields = ('name',)


class ExpertarticleAdmin(admin.ModelAdmin):
    fieldsets = [

        (None, {
            'fields': ['name', 'ranks', 'province', 'city', 'hospital', 'department', 'midpic', 'smallpic', 'introduce',
                       'specialty', 'postscript', 'weixinpic', 'weibopic', 'published']}),

        ('首页显示', {'fields': ['shouye', 'weizhi'], 'classes': ['collapse']})

    ]
    list_display = ('name', 'province', 'zan', 'pub_date', 'published')
    search_fields = ('name',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date', 'published')
    search_fields = ('name',)

admin.site.register(Interviewarticle, InterviewarticleAdmin)
admin.site.register(Doctorarticle, DoctorarticleAdmin)
admin.site.register(Expertarticle, ExpertarticleAdmin)
admin.site.register(Comment, CommentAdmin)
