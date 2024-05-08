from django.urls import path, include 
from . import views

urlpatterns = [
  path('', views.getProductos),
  path('create', views.addProducto),
  path('read/<str:pk>', views.getProducto),
  path('update/<str:pk>', views.updateProducto),
  path('delete/<str:pk>', views.deleteProducto),
]