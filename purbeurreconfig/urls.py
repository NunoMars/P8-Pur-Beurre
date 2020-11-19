from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from products.views import index

"""allouer les views"""
urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls, name="admin"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("products/", include("products.urls"), name="products"),
    path("accounts/", include("accounts.urls"), name="accounts"),
]

