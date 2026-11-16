from django.contrib import admin
from .models import Product, BlogPost

# Mendaftarkan Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')

# Mendaftarkan BlogPost agar muncul di admin
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')