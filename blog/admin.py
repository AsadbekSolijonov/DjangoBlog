from django.contrib import admin
from blog.models import Blog


# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'body', 'created', 'updated')
    list_display_links = ['title', 'body', 'created']
    list_filter = ['title']
