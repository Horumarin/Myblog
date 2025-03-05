from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import BlogPost


class BlogPostAdmin(MarkdownxModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "content")
    list_filter = ("created_at",)


admin.site.register(BlogPost, BlogPostAdmin)  # ここが修正ポイント！
