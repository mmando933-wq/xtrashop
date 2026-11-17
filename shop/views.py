from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Product  # <-- Pastikan Product ikut di-import di sini

def home_view(request):
    latest_posts = BlogPost.objects.all().order_by('-created_at')[:3] # Mengambil 3 blog terbaru
    products = Product.objects.all().order_by('-created_at')          # <-- Tambahan: Mengambil semua produk
    
    context = {
        'latest_posts': latest_posts,
        'products': products,                                         # <-- Tambahan: Dikirim ke halaman HTML
    }
    return render(request, 'shop/home.html', context)

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'shop/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'shop/blog_detail.html', {'post': post})

def disclosure_view(request):
    return render(request, 'shop/disclosure.html')