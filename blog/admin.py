from django.contrib import admin
from blog.models import Blog, Category, Comment, ClientInfo


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'cat_desc', 'created', 'updated')

    def cat_desc(self, obj):
        return self.short_description(obj.description)

    @staticmethod
    def short_description(text, length=10):
        if len(text) > length:
            return f"{text[:length]}..."
        return text


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'body_field', 'created', 'updated', 'image')

    # list_display_links = ['blog_title', 'created']
    # list_filter = ['blog_title']

    def blog_title(self, obj):
        return self._shorten_text(obj.title)

    def body_field(self, obj):
        return self._shorten_text(obj.body)

    body_field.short_description = 'body'

    @staticmethod
    def _shorten_text(text, length=10):
        if len(text) > length:
            return f'{text[:length]}...'
        return text


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'author', 'message', 'created', 'updated')


@admin.register(ClientInfo)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'email', 'phone_number', 'message', 'created')
