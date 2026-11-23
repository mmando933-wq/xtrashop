from django.contrib import admin
from .models import BlogPost, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_featured", "created_at")
    list_editable = ("is_featured",)
    search_fields = ("name", "description")
    list_filter = ("is_featured", "created_at")


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category_name", "created_at")
    search_fields = ("title", "category_name", "summary", "content")
    prepopulated_fields = {"slug": ("title",)}