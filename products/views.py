from django.shortcuts import render
from .models import Product, Category
from .forms import PriceFilterFrom, ProductFilterForm


def home(request):
    return render(request, "product_views/home.html")


def catalog(request):
    products = Product.objects.all()  # Get all products from the database
    categories = Category.objects.all()  # Get all categories from the database

    category_filters = request.GET.get('category')
    if category_filters:
        products = products.filter(category_id=int(category_filters))

    # Filters of price
    form = PriceFilterFrom(request.GET)
    if form.is_valid():
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if min_price:
            products = products.filter(price__gte=min_price)
        if max_price:
            products = products.filter(price__lte=max_price)

    # Filters of product
    product_form = ProductFilterForm(request.GET)

    print("Products:", products)
    print("Categories:", categories)
    print("Form errors:", form.errors if not form.is_valid() else "No errors")

    return render(request, 'products/catalog.html', {
        'products': products,
        'categories': categories,
        'form': product_form,
        'product_form': product_form,
    })


def about(request):
    return render(request, "product_views/about.html")
