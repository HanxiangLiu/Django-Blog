from django.shortcuts import render


def index(request):
    return render(request, 'post/index.html')


def post_list_view(request):
    return render(request, 'post/list.html')


def detail(request, time_id):
    return render(request, 'post/detail.html')