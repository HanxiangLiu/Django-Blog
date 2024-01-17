from django.urls import path
from . import views

app_name = "cms"

urlpatterns = [
    path("login/", views.cms_login, name="login"),
    path("dashboard/", views.cms_dashboard, name="dashboard"),
]
