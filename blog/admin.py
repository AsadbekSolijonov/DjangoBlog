from django.contrib import admin
from blog.models import Blog, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'body_field', 'created', 'updated')
    list_display_links = ['title', 'created']
    list_filter = ['title']

    def body_field(self, obj):
        return self._shorten_text(obj.body)

    body_field.short_description = 'body'

    def _shorten_text(self, text, length=10):
        if len(text) > length:
            return f'{text[:length]}...'
        return text
