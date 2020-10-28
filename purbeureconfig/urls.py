"""purbeureconfig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from home import views
from products import views as productViews
from accounts import views as accountViews
from django.contrib.auth import views as auth_views

"""alouer les views"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.get_product, name='home'),
    path("", views.get_product, name='home'),
    path("products/", productViews.get_products_choice,name="products"),
    path("product/", productViews.product_view,name="product"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', accountViews.login_view,name="login"),
    path("logout/", accountViews.logout_view,name="logout"),
]
