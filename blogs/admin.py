from django.contrib import admin

from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'content', 'date_created']
    search_fields = ('title',)
    list_filter = ['author']

admin.site.register(Blog, BlogAdmin)
