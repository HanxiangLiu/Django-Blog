from django import forms
from apps.post.models import Category


class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryEditForm(forms.ModelForm):
    pk = forms.CharField(max_length=100)

    class Meta:
        model = Category
        fields = "__all__"
