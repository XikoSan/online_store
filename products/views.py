from django.shortcuts import render
from .models import Product


def home(request):
    return render(request, "product_views/home.html")


def catalog(request):
    products = Product.objects.all()  # Получаем все продукты из базы данных
    return render(request, "product_views/catalog.html", {"products": products})


def about(request):
    return render(request, "product_views/about.html")
