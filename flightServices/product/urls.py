from django.urls import path
from product import views

urlpatterns = [
    path("products/", views.AllProducts, name="AllProducts"),
]
