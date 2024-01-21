from django.urls import path
from . import views
from apps.cms.category_view import CategoryView, CategoryEditView, CategoryDeleteView
from apps.cms.post_view import PostView, PostEditView, PostDeleteView
from apps.cms.link_view import LinkView, LinkEditView, LinkDeleteView
from apps.cms.advertise_view import AdvertiseView, AdvertiseEditView, AdvertiseDeleteView
from apps.cms.user_view import UserView, UserEditView, UserDeleteView

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
    # -------------Link URLs------------
    path("dashboard/link/manage", views.link_manage_view, name="link_manage_view"),
    path("dashboard/link/publish", views.link_publish_view, name="link_publish_view"),
    path("dashboard/link/add", LinkView.as_view(), name="link_add"),
    path("dashboard/link/edit", LinkEditView.as_view(), name="link_edit_view"),
    path("dashboard/link/delete", LinkDeleteView.as_view(), name="link_delete"),
    # -------------Advertise URLs------------
    path("dashboard/advertise/manage", views.advertise_manage_view, name="advertise_manage_view"),
    path("dashboard/advertise/publish", views.advertise_publish_view, name="advertise_publish_view"),
    path("dashboard/advertise/add", AdvertiseView.as_view(), name="advertise_add"),
    path("dashboard/advertise/edit", AdvertiseEditView.as_view(), name="advertise_edit_view"),
    path("dashboard/advertise/delete", AdvertiseDeleteView.as_view(), name="advertise_delete"),
    # -------------User URLs------------
    path("dashboard/user/manage", views.user_manage_view, name="user_manage_view"),
    path("dashboard/user/publish", views.user_publish_view, name="user_publish_view"),
    path("dashboard/user/add", UserView.as_view(), name="user_add"),
    path("dashboard/user/edit", UserEditView.as_view(), name="user_edit_view"),
    path("dashboard/user/delete", UserDeleteView.as_view(), name="user_delete"),
]
