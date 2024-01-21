from django.shortcuts import redirect, render
from django.urls import reverse
from apps.cms.forms import AdvertiseAddForm, AdvertiseEditForm
from apps.link.models import Link
from apps.link.models import Advertise
from django.views.generic import View

class AdvertiseView(View):
    def post(self, request):
        # 新建提交
        if 'submit' in request.POST:
            form = AdvertiseAddForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                image_url = form.cleaned_data.get('image_url')
                link_url = form.cleaned_data.get('link_url')
                Advertise.objects.create(title=title, image_url=image_url, link_url=link_url)
                return redirect(reverse("cms:advertise_manage_view"))
            else:
                return redirect(reverse("cms:advertise_publish_view"))
        # 修改Link
        elif 'modify' in request.POST:
            form = AdvertiseEditForm(request.POST)
            if form.is_valid():
                pk = form.cleaned_data.get('pk')
                title = form.cleaned_data.get('title')
                image_url = form.cleaned_data.get('image_url')
                link_url = form.cleaned_data.get('link_url')
                instance = Advertise.objects.filter(id=pk)
                instance.update(title=title, image_url=image_url, link_url=link_url)
                return redirect(reverse("cms:advertise_manage_view"))
            else:
                return redirect(reverse("cms:advertise_manage_view"))
        # 修改状态返回
        elif 'back' in request.POST:
            return redirect(reverse("cms:advertise_manage_view"))
        # 新建状态的取消
        else:
            return redirect(reverse("cms:advertise_publish_view"))

class AdvertiseEditView(View):
    def get(self,request):
        advertise_id = request.GET.get('advertise_id')
        category = Advertise.objects.get(pk=advertise_id)
        context = {
            'item_data': category,
        }
        return render(request, 'cms/advertise/publish.html', context=context)
