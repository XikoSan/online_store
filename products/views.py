from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from .forms import PriceFilterFrom
from django.core.paginator import Paginator


def home(request):
    return render(request, "product_views/home.html")


def search(request):
    query = request.GET.get('q', '')
    results = Product.objects.filter(name__icontains=query) if query else []
    return render(request, 'products/search_results.html', {'query': query, 'results': results})


def catalog(request):
    products = Product.objects.all()  # Get all products from the database
    categories = Category.objects.all()  # Get all categories from the database

    # Filters of categories
    selected_categories = request.GET.getlist('category')  # list of categories
    if selected_categories:
        products = products.filter(category_id__in=selected_categories)

    # Filters of price
    form = PriceFilterFrom(request.GET)
    if form.is_valid():
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if min_price:
            products = products.filter(price__gte=min_price)
        if max_price:
            products = products.filter(price__lte=max_price)

    # Pagination output
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'form': form,
        'page_obj': page_obj,
        'selected_categories': selected_categories,
    }

    print("Products:", products)
    print("Categories:", categories)
    print("Form errors:", form.errors if not form.is_valid() else "No errors")

    return render(request, 'products/catalog.html', context)


def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'products/category.html', {'category': category, 'products': products})


def cart_view(request):
    return render(request, 'cart_view.html')


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, 'products/product_detail.html', {'product': product})