import json
import markdown
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import View
from django.http import HttpResponse

from apps.cms.forms import PostAddForm, PostEditForm
from apps.post.models import Post


class PostView(View):
    def post(self, request):
        # 新建提交
        if "submit" in request.POST:
            form = PostAddForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get("title")
                description = form.cleaned_data.get("description")
                author = form.cleaned_data.get("author")
                thumbnail = form.cleaned_data.get("thumbnail")
                status = form.cleaned_data.get("status")
                content = form.cleaned_data.get("content")
                category = form.cleaned_data.get("category")
                priority = form.cleaned_data.get("priority")
                is_hot = form.cleaned_data.get("is_hot")
                time_id = form.cleaned_data.get("time_id")
                Post.objects.create(
                    title=title,
                    description=description,
                    author=author,
                    thumbnail=thumbnail,
                    status=status,
                    content=content,
                    category=category,
                    priority=priority,
                    is_hot=is_hot,
                    time_id=time_id,
                )
                return redirect(reverse("cms:post_manage_view"))
            else:
                return HttpResponse(content=json.dumps(form.errors.get_json_data()))
        # 修改Post
        elif "modify" in request.POST:
            form = PostEditForm(request.POST)
            if form.is_valid():
                pk = form.cleaned_data.get("pk")
                title = form.cleaned_data.get("title")
                description = form.cleaned_data.get("description")
                author = form.cleaned_data.get("author")
                thumbnail = form.cleaned_data.get("thumbnail")
                status = form.cleaned_data.get("status")
                content = form.cleaned_data.get("content")
                category = form.cleaned_data.get("category")
                priority = form.cleaned_data.get("priority")
                is_hot = form.cleaned_data.get("is_hot")
                time_id = form.cleaned_data.get("time_id")
                instance = Post.objects.filter(id=pk)
                md = markdown.Markdown(
                    extensions=[
                        # 包含 缩写、表格等常用扩展
                        "markdown.extensions.extra",
                        # 语法高亮扩展
                        "markdown.extensions.codehilite",
                        # 目录扩展
                        "markdown.extensions.toc",
                    ]
                )
                content_html = md.convert(content)
                instance.update(
                    title=title,
                    description=description,
                    author=author,
                    thumbnail=thumbnail,
                    status=status,
                    content=content,
                    category=category,
                    priority=priority,
                    is_hot=is_hot,
                    time_id=time_id,
                    content_html=content_html,
                )
                return redirect(reverse("cms:post_manage_view"))
            else:
                return HttpResponse(content=json.dumps(form.errors.get_json_data()))
        # 修改状态返回
        elif "back" in request.POST:
            return redirect(reverse("cms:post_manage_view"))
        # 新建状态的取消
        else:
            return redirect(reverse("cms:post_publish_view"))


class PostEditView(View):
    def get(self, request):
        post_id = request.GET.get("post_id")
        post = Post.objects.get(pk=post_id)
        context = {
            "item_data": post,
        }
        return render(request, "cms/post/publish.html", context=context)


class PostDeleteView(View):
    def get(self, request):
        post_id = request.GET.get('post_id')
        Post.objects.filter(pk=post_id).update(status=Post.STATUS_DELETE)
        return redirect(reverse("cms:post_manage_view"))
