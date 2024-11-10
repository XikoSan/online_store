from django.shortcuts import render


# Home page
def home(request):
    return render(request, "product_views/home.html")


# Catalog page
def catalog(request):
    return render(request, "product_views/catalog.html")


# Company page
def about(request):
    return render(request, "product_views/about.html")
