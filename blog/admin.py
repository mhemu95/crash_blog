from django.contrib import admin
from .models import Post, Comment, Category

# Register your models here.
class commentInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category', 'published_at', 'status']
    list_filter = ['slug', 'created_at', 'status']
    date_hierarchy = 'published_at'
    ordering = ['status', 'published_at']
    inlines = [commentInline]
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email', 'post', 'created_at']
    list_display = ['name', 'email', 'post', 'created_at']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)

# todo: rewrite the admin file code.
# todo: start from admin.py from book django 4 by example
