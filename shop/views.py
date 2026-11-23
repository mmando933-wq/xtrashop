from django.shortcuts import get_object_or_404, render
from .models import BlogPost, Product


def home_view(request):
    products = Product.objects.order_by("-created_at")
    featured_product = (
        products.exclude(image_url__isnull=True)
        .exclude(image_url="")
        .first()
        or products.first()
    )
    return render(
        request,
        "shop/home.html",
        {
            "products": products,
            "featured_product": featured_product,
        },
    )


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "shop/product_detail.html", {"product": product})


def blog_list(request):
    posts = BlogPost.objects.order_by("-created_at")
    return render(request, "shop/blog_list.html", {"posts": posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, "shop/blog_detail.html", {"post": post})


def disclosure_view(request):
    return render(request, "shop/disclosure.html")