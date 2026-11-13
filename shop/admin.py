from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_name', 'price', 'created_at')
    prepopulated_fields = {'slug': ('title',)}