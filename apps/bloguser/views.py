from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.http import require_POST

from apps.bloguser.forms import LoginForm


@require_POST
def login_view(request):
    form = LoginForm(request.POST)
    print(form)
    if form.is_valid():
        print("form is valid")
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect(reverse('cms:dashboard'))
        else:
            return redirect(reverse('cms:login'))
    else:
        print("form is not valid")
        return redirect(reverse('cms:login'))


def logout_view(request):
    logout(request)
    return redirect(reverse('cms:login'))
