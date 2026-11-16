from django.db import models
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Judul Artikel / Ulasan")
    slug = models.SlugField(unique=True, blank=True)
    category_name = models.CharField(max_length=100, verbose_name="Kategori / Nama Produk", default="Produk Pilihan")
    price = models.CharField(max_length=50, verbose_name="Perkiraan Harga", default="Rp 0")
    affiliate_url = models.URLField(max_length=500, verbose_name="Link Afiliasi (Shopee / Tokopedia)")
    image_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="URL Foto Produk")
    summary = models.TextField(verbose_name="Ringkasan Singkat")
    content = models.TextField(verbose_name="Ulasan Lengkap")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Tanggal Dibuat")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nama Produk")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Harga")
    affiliate_link = models.URLField(max_length=500, verbose_name="Link Afiliasi Shopee/Tokopedia")
    description = models.TextField(blank=True, null=True, verbose_name="Deskripsi")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title