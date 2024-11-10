from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('catalog', views.catalog, name='catalog'),  # Catalog page
    path('about', views.about, name='about'),  # Company page
]
