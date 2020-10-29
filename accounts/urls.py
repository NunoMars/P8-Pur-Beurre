from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path("create_account/", views.create_account_view),
    path("login/", views.login_view),
    path("logout/", views.logout_view),
]