from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    url("create_account/", views.create_account_view, name="create_account"),
    path('login/', LoginView.as_view(), name="login"),
    url("logout/", views.logout_view, name="logout"),
]