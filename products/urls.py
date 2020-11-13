from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url(r'home', views.index, name='home'),
    url(r'search', views.search, name='search_product'),
    url(r'^(?P<product>[0-9]+)/$', views.products_list, name="products_list"),
    url(r'^product_detail/(?P<product>[0-9]+)/$', views.product_view, name='product_detail'),
    url(r'history', views.history, name='history'),
    url(r'mentions_legales', views.mentions_legales, name='mentions_legales'),
]