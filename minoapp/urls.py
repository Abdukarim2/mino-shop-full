from django.urls import path
from . import views

app_name = "minoapp"

urlpatterns = [
    path('categories/get/', views.CategoryList.as_view()),
    path('products/get/', views.ProductList.as_view()),
    path('products/bycategory/<str:category_slug>/', views.ProductByCategory.as_view()),
    path('products/detail/<str:slug>/<int:id>/', views.ProductDetail.as_view()),
]