from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.catalog, name='catalog'),  # Page catalog
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # Page product detail
    path('category/<int:category_id>/', views.category_view, name='category_view'),
    path('search/', views.search, name='search'),
    path('account/', views.account_view, name='account'),
    path('cart/', views.cart_view, name='cart'),
]


def search(request):
    query = request.GET.get('q', '')
    if not query:
        return render(request, 'products/search_results.html', {'query': query, 'results': []})
    results = Product.objects.filter(name__icontains=query)
    return render(request, 'products/search_results.html', {'query': query, 'results': results})


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
