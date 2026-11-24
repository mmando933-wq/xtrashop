from django.http import HttpResponse
from django.urls import path
from . import views

app_name = "shop"


def google_verify(request):
    return HttpResponse(
        "google-site-verification: googled004eef4fc688389.html",
        content_type="text/html; charset=utf-8",
    )


urlpatterns = [
    path("", views.home_view, name="home"),
    path("googled004eef4fc688389.html", google_verify, name="google_verify"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("blog/", views.blog_list, name="blog_list"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("disclosure/", views.disclosure_view, name="disclosure"),
]