from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url('home', views.index, name='home'),
    url("proposed_products", views.get_products_choice, name="products_list"),
    url('^(?P<product>[0-9]+)/$', views.product_view, name='product_detail'),
    url('history', views.history, name='history'),
]