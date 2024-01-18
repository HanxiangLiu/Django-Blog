from django.urls import path
from . import views
from apps.cms.category_view import CategoryView, CategoryEditView, CategoryDeleteView
from apps.cms.post_view import PostView, PostEditView, PostDeleteView


app_name = "cms"

urlpatterns = [
    path("login/", views.cms_login, name="login"),
    path("dashboard/", views.cms_dashboard, name="dashboard"),
    # -------------Category URLs------------
    path("dashboard/category/manage", views.category_manage_view, name="category_manage_view"),
    path("dashboard/category/publish", views.category_publish_view, name="category_publish_view"),
    path("dashboard/category/add", CategoryView.as_view(), name="category_add"),
    path("dashboard/category/edit", CategoryEditView.as_view(), name="category_edit_view"),
    path("dashboard/category/delete", CategoryDeleteView.as_view(), name="category_delete"),
    # -------------Post URLs------------
    path("dashboard/post/manage", views.post_manage_view, name="post_manage_view"),
    path("dashboard/post/publish", views.post_publish_view, name="post_publish_view"),
    path("dashboard/post/add", PostView.as_view(), name="post_add"),
    path("dashboard/post/edit", PostEditView.as_view(), name="post_edit_view"),
    path("dashboard/post/delete", PostDeleteView.as_view(), name="post_delete"),
]
