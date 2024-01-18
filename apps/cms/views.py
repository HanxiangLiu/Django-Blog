from django.shortcuts import render
from apps.post.models import Category, Post
from apps.bloguser.models import User


def cms_login(request):
    return render(request, "cms/login.html")


def cms_dashboard(request):
    return render(request, "cms/dashboard/home.html")


'''
Category manage view
'''
def category_manage_view(request):
    context = {
        "list_data": Category.objects.all()
        }
    return render(request, "cms/category/manage.html", context=context)


def category_publish_view(request):
    return render(request, "cms/category/publish.html")


'''
Post manage view
'''
def post_manage_view(request):
    posts = Post.objects.all()
    context = {
        "list_data": posts,
    }
    return render(request, 'cms/post/manage.html', context=context)


def post_publish_view(request):
    context = {
        'list_data_category': Category.objects.all(),
        'list_data_user': User.objects.all(),
        'list_data_status': Post.STATUS_ITEMS
    }
    return render(request, 'cms/post/publish.html', context=context)
