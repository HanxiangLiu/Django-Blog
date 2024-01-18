from django.urls import path
from . import views
from apps.cms.category_view import CategoryView, CategoryEditView, CategoryDeleteView

app_name = "cms"

urlpatterns = [
    path("login/", views.cms_login, name="login"),
    path("dashboard/", views.cms_dashboard, name="dashboard"),
    path("dashboard/category/manage", views.category_manage_view, name="category_manage_view"),
    path("dashboard/category/publish", views.category_publish_view, name="category_publish_view"),
    path("dashboard/category/add", CategoryView.as_view(), name="category_add"),
    path("dashboard/category/edit", CategoryEditView.as_view(), name="category_edit_view"),
    path("dashboard/category/delete", CategoryDeleteView.as_view(), name="category_delete"),
]
