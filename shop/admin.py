from django.contrib import admin
from .models import BlogPost, Product

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_name', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'summary')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')  # Menggunakan 'name' khusus untuk Product
    search_fields = ('name', 'description')