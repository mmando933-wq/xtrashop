# my_shop/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),  # <-- Menghubungkan halaman utama ke aplikasi shop
]

