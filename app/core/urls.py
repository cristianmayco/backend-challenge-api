from django.urls import path
# from rest_framework.routers import SimpleRouter

from .views import ManufacturesAPIView, ManufacturerAPIView, ProductAPIView, ProductsAPIView

urlpatterns = [
    path('manufactures/', ManufacturesAPIView.as_view(), name='manufactures'),
    path('manufactures/<int:pk>',
         ManufacturerAPIView.as_view(),
         name='manufacturer'),
    path('products/', ProductsAPIView.as_view(), name='products'),
    path('products/<int:pk>', ProductAPIView.as_view(), name='product'),
]
