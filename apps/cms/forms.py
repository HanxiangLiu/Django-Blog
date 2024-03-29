from django import forms
from apps.post.models import Category, Post
from apps.link.models import Link, Advertise


# Category form
class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryEditForm(forms.ModelForm):
    pk = forms.CharField(max_length=100)

    class Meta:
        model = Category
        fields = "__all__"


# Post form
class PostAddForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("read_num",)


class PostEditForm(forms.ModelForm):
    pk = forms.CharField(max_length=100)
    class Meta:
        model = Post
        exclude = ('read_num',)


# Link form
class LinkAddForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = "__all__"


class LinkEditForm(forms.ModelForm):
    pk = forms.CharField(max_length=100)
    class Meta:
        model = Link
        fields = "__all__"


# Advertise form
class AdvertiseAddForm(forms.ModelForm):
    class Meta:
        model = Advertise
        fields = "__all__"


class AdvertiseEditForm(forms.ModelForm):
    pk = forms.CharField(max_length=100)
    class Meta:
        model = Advertise
        fields = "__all__"


# User form
class UserAddForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(max_length=20, min_length=6)


class UserEditForm(forms.Form):
    pk = forms.CharField(max_length=100)
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(max_length=20, min_length=6)