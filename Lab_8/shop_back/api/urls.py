from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.get_products, name="get all products"),
    path('products/<int:product_id>/', views.get_product, name="get product"),
    path('categories/', views.get_categories, name="get all categories"),
    path('categories/<int:category_id>/', views.get_category, name="get category"),
    path('categories/<int:category_id>/products/', views.get_category_products, name="get category products"),
]
