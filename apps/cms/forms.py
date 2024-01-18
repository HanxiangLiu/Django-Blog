from django import forms
from apps.post.models import Category, Post


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
