from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # Page product detail
    path('', views.home, name='home'),  # Home page
    path('catalog/', views.catalog, name='catalog'),  # Catalog page
    path('about', views.about, name='about'),  # Company page
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
