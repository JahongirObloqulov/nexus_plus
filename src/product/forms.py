from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', "description", 'category', 'price', 'city', 'discount', 'condition', 'address']
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control input-md', 'placeholder': 'Title'}),
            "category": forms.Select(attrs={'class': 'tg-select form-control'}),
            "price": forms.NumberInput(attrs={'class': 'form-control input-md', 'placeholder': 'Ad your Price'}),
            "discount": forms.NumberInput(attrs={'class': 'form-control input-md', 'placeholder': 'Ad your Discount'}),
            "city": forms.Select(attrs={'class': 'tg-select form-control'}),
            "address": forms.TextInput(attrs={'class': 'form-control input-md'}),
            "condition": forms.Select(attrs={'class': 'form-control input-md'}),
            "description": SummernoteWidget(attrs={'class': 'summernote'})
        }


class ProductImageForm(forms.Form):
    image = forms.ImageField(label='image')


ProductImageFormset = forms.formset_factory(ProductImageForm, extra=2)
