from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category_name = models.CharField(max_length=100)
    summary = models.TextField()
    content = models.TextField()
    image_url = models.URLField(max_length=500, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=100)
    affiliate_link = models.URLField(max_length=500)
    description = models.TextField()
    image_url = models.URLField(max_length=500, blank=True, null=True)  # <-- Kolom link gambar Shopee/Tokopedia
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name