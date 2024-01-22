import datetime
from django.shortcuts import render

from apps.post.models import Category, Post
from apps.bloguser.models import User
from apps.link.models import Link, Advertise
from apps.bloguser.models import User, UserVisit, DailyVisitNum, TotalVisitNum
from utils.paginator_helper import get_paginator, get_pagination_data


'''
Dashboard view
'''
def cms_login(request):
    return render(request, "cms/login.html")


def cms_dashboard(request):
    context = {}
    context.update(get_dashboard_top_data())
    return render(request, 'cms/dashboard/home.html', context=context)


def get_dashboard_top_data():
    post_num = Post.objects.all().count()
    cur_date = datetime.datetime.now().strftime('%Y-%m-%d')
    day_visit_ip_set = set()
    day_visit_ip_list = UserVisit.objects.filter(day=cur_date)
    if day_visit_ip_list:
        for user_ip_item in day_visit_ip_list:
            if user_ip_item.ip_address not in day_visit_ip_set:
                day_visit_ip_set.add(user_ip_item.ip_address)
    day_visit_ip_num = len(day_visit_ip_set)
    day_visit_num = DailyVisitNum.objects.filter(day=cur_date)[0].count if DailyVisitNum.objects.filter(day=cur_date).count() else 0
    total_visit_num = TotalVisitNum.objects.all()[0].count if TotalVisitNum.objects.all().count() else 0
    context = {
        "post_num": post_num,
        "day_visit_ip_num": day_visit_ip_num,
        "day_visit_num": day_visit_num,
        "total_visit_num": total_visit_num
    }
    return context


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


'''
User manage view
'''
def user_manage_view(request):
    context = {
        "list_data": User.objects.all(),
    }
    return render(request, 'cms/user/manage.html', context=context)


def user_publish_view(request):
    return render(request, 'cms/user/publish.html')