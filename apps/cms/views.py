from django.shortcuts import render
from apps.post.models import Category, Post
from apps.bloguser.models import User
from apps.link.models import Link, Advertise
from utils.paginator_helper import get_paginator, get_pagination_data


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
    page = int(request.GET.get('p', 1))
    posts = Post.objects.all()
    paginator = get_paginator(posts)
    page_obj = paginator.page(page)
    context = {
        "list_data": page_obj.object_list,
        'list_data_status': Post.STATUS_ITEMS
    }
    context.update(get_pagination_data(paginator, page_obj))
    return render(request, 'cms/post/manage.html', context=context)


def post_publish_view(request):
    context = {
        'list_data_category': Category.objects.all(),
        'list_data_user': User.objects.all(),
        'list_data_status': Post.STATUS_ITEMS
    }
    return render(request, 'cms/post/publish.html', context=context)


'''
Link manage view
'''
def link_manage_view(request):
    context = {
        "list_data": Link.objects.all(),
        'list_data_status': Link.STATUS_ITEMS
    }
    return render(request, 'cms/link/manage.html', context=context)


def link_publish_view(request):
    context = {
        'list_data_status': Link.STATUS_ITEMS
    }
    return render(request, 'cms/link/publish.html', context=context)


'''
Advertise manage view
'''
def advertise_manage_view(request):
    context = {
        "list_data": Advertise.objects.all()
    }
    return render(request, 'cms/advertise/manage.html', context=context)


def advertise_publish_view(request):
    return render(request, 'cms/advertise/publish.html')
