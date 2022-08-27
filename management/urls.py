from django.urls import path
from . import views

app_name = "management"

urlpatterns = [
    path('order/', views.CrateOrder.as_view())
]