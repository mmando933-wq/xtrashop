from django.db import models
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Judul Artikel / Ulasan")
    slug = models.SlugField(unique=True, blank=True)
    
    # Label Kategori Produk (Contoh: Gadget & Perangkat Kerja, Elektronik, dll)
    category_name = models.CharField(max_length=100, verbose_name="Kategori / Nama Produk", default="Produk Pilihan")
    
    # Harga Produk (Format teks bebas, misal: Rp 1.500.000)
    price = models.CharField(max_length=50, verbose_name="Perkiraan Harga", default="Rp 0")
    
    # Tautan Afiliasi Lokal (Shopee / Tokopedia)
    affiliate_url = models.URLField(max_length=500, verbose_name="Link Afiliasi (Shopee / Tokopedia)")
    
    # URL Gambar Produk
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