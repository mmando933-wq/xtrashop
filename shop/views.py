from pathlib import Path
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import BlogPost, Product, SponsorBanner


def google_site_verification(request):
    file_path = Path(__file__).resolve().parent / "googled004eef4fc688389.html"
    if not file_path.exists():
        raise Http404("Verification file not found")
    return HttpResponse(
        file_path.read_text(encoding="utf-8"),
        content_type="text/html; charset=utf-8",
    )


def home_view(request):
    products = Product.objects.order_by("-created_at")

    featured_with_img = (
        products.filter(is_featured=True)
        .exclude(image_url__isnull=True)
        .exclude(image_url="")
        .first()
    )
    featured_any = products.filter(is_featured=True).first()
    fallback_with_img = (
        products.exclude(image_url__isnull=True)
        .exclude(image_url="")
        .first()
    )

    featured_product = featured_with_img or featured_any or fallback_with_img or products.first()
    sponsor_banner = SponsorBanner.objects.filter(is_active=True).order_by("-created_at").first()

    return render(
        request,
        "shop/home.html",
        {
            "products": products,
            "featured_product": featured_product,
            "sponsor_banner": sponsor_banner,
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