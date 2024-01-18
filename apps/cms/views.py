from django.shortcuts import render
from apps.post.models import Category


def cms_login(request):
    return render(request, "cms/login.html")


def cms_dashboard(request):
    return render(request, "cms/dashboard/home.html")


def category_manage_view(request):
    context = {
        "list_data": Category.objects.all()
        }
    return render(request, "cms/category/manage.html", context=context)


def category_publish_view(request):
    return render(request, "cms/category/publish.html")
