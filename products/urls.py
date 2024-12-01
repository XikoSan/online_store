from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.catalog, name='catalog'),  # Главная страница
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # Страница товара
    path('category/<int:category_id>/', views.category_view, name='category_view'),  # Категории
    path('search/', views.search, name='search'),  # Поиск
    path('cart/', views.cart_view, name='cart'),  # Корзина
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)