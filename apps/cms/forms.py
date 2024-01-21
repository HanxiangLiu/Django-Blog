from django import forms
from apps.post.models import Category, Post
from apps.link.models import Link


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