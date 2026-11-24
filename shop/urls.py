from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("googled004eef4fc688389.html", views.google_site_verification, name="google_site_verification"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("blog/", views.blog_list, name="blog_list"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("disclosure/", views.disclosure_view, name="disclosure"),
]