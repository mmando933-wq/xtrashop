from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Product

def home_view(request):
    products = Product.objects.order_by('-created_at')
    featured_product = products.first()
    return render(request, 'shop/home.html', {
        'products': products,
        'featured_product': featured_product,
    })

    return render(request, 'shop/home.html', context)

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'shop/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'shop/blog_detail.html', {'post': post})

def disclosure_view(request):
    return render(request, 'shop/disclosure.html')