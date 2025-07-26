from django.contrib import admin

from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'content', 'date_created']
    search_fields = ('title',)
    list_filter = ['author']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Blog, BlogAdmin)
