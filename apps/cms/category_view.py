from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import View
from django.shortcuts import redirect, render

from apps.cms.forms import CategoryAddForm, CategoryEditForm
from apps.post.models import Category


class CategoryView(View):
    def post(self, request):
        # 新建提交
        if 'submit' in request.POST:
            form = CategoryAddForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data.get('name')
                Category.objects.create(name=name)
                return redirect(reverse("cms:category_manage_view"))
            else:
                return redirect(reverse("cms:category_publish_view"))
        # 修改Category
        elif 'modify' in request.POST:
            form = CategoryEditForm(request.POST)
            if form.is_valid():
                pk = form.cleaned_data.get('pk')
                name = form.cleaned_data.get('name')
                Category.objects.filter(id=pk).update(name=name)
                return redirect(reverse("cms:category_manage_view"))
            else:
                return redirect(reverse("cms:category_manage_view"))
        # 修改状态返回
        elif 'back' in request.POST:
            return redirect(reverse("cms:category_manage_view"))
        # 新建状态的取消
        else:
            return redirect(reverse("cms:category_publish_view"))


class CategoryEditView(View):
    def get(self, request):
        category_id = request.GET.get("category_id")
        category = Category.objects.get(pk=category_id)
        context = {
            "item_data": category,
        }
        return render(request, "cms/category/publish.html", context=context)


class CategoryDeleteView(View):
    def get(self,request):
        category_id = request.GET.get('category_id')
        Category.objects.filter(id=category_id).delete()
        return redirect(reverse("cms:category_manage_view"))
