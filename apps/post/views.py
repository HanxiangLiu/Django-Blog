from django.shortcuts import render
from apps.post.models import Post


def get_read_most_post():
    read_post = Post.objects.all().order_by("-read_num")
    if len(read_post) > 5:
        read_post = read_post[:5]
    context = {
        "read_post": read_post
    }
    return context


def index(request):
    top_post = Post.objects.filter(status=Post.STATUS_NORMAL, priority__gt=0).order_by('-priority')
    if len(top_post) > 4:
        top_post = top_post[:4]
    list_post = Post.objects.filter(status=Post.STATUS_NORMAL, priority=0)
    context = {
        'top_post': top_post,
        'list_post': list_post
    }
    context.update(get_read_most_post())
    return render(request, 'post/index.html', context=context)


def post_list_view(request):
    return render(request, "post/list.html")


def detail(request, time_id):
    return render(request, "post/detail.html")
