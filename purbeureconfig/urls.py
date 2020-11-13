from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from products.views import index

"""allouer les views"""
urlpatterns = [
    url(r"^$", index, name="index"),
    path(r"admin/", admin.site.urls, name="admin"),
    path(r"accounts/", include("django.contrib.auth.urls")),
    path(r"products/", include("products.urls"), name="products"),
    path(r"accounts/", include("accounts.urls"), name="accounts"),
]
