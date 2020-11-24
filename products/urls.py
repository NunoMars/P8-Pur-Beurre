from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url("home", views.index, name="home"),
    url("contact", views.contact, name="contact"),
    url("search", views.search, name="search_product"),
    url(r"^(?P<product>[0-9]+)/$", views.products_list, name="products_list"),
    url(
        r"^product_detail/(?P<product>[0-9]+)/$",
        views.product_view,
        name="product_detail",
    ),
    url("history", views.history, name="history"),
    url("mentions_legales", views.mentions_legales, name="mentions_legales"),
]
