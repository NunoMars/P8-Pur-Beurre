from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path("", views.get_products_choice),
    path("product/", views.product_view),
]