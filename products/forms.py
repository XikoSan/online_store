
from django import forms


class PriceFiltersFrom(forms.Form):
    min_price = forms.DecimalField(required=False, label="Min. price", max_digits=10, decimal_places=2)
    max_price = forms.DecimalField(required=False, label="Max. price", max_digits=10, decimal_places=2)

