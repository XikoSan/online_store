from django.shortcuts import render
from .models import Product
from .forms import PriceFiltersFrom


def home(request):
    return render(request, "product_views/home.html")


def catalog(request):
    products = Product.objects.all()  # Получаем все продукты из базы данных

    form = PriceFiltersFrom(request.GET)
    if form.is_valid():
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if min_price:
            products = products.filter(price__gte=min_price)
        if max_price:
            products = products.filter(price__lte=max_price)

    return render(request, "product_views/catalog.html", {"form": form, "products": products})


def about(request):
    return render(request, "product_views/about.html")
