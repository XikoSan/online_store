from .models import Category
from django import forms


class PriceFilterFrom(forms.Form):
    min_price = forms.DecimalField(required=False, label="Min. price", max_digits=10, decimal_places=2)
    max_price = forms.DecimalField(required=False, label="", max_digits=10, decimal_places=2)


class ProductFilterForm(forms.Form):
    min_price = forms.DecimalField(required=False, label='Min. price', max_digits=10, decimal_places=2)
    max_price = forms.DecimalField(required=False, label='Max. price', max_digits=10, decimal_places=2)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, label='Category')
