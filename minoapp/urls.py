from django.urls import path
from . import views

app_name = "minoapp"

urlpatterns = [
    path('categories/get/', views.CategoryList.as_view()),
    path('products/get/', views.ProductList.as_view()),
    path('products/bycategory/<int:category_id>/', views.ProductByCategory.as_view()),
    path('products/detail/<int:id>/', views.ProductDetail.as_view()),
]