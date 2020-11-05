from django.conf.urls import url
from . import views


urlpatterns = [
    url("create_account/", views.create_account_view, name="create_account"),
    url("auth/", views.login_view, name="auth"),
    url("logout/", views.logout_view, name="logout"),
]