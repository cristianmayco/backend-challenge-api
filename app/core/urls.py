from django.urls import path
# from rest_framework.routers import SimpleRouter

from .views import ManufacturesAPIView, ManufacturerAPIView

urlpatterns = [
    path('manufactures/', ManufacturesAPIView.as_view(), name='manufactures'),
    path('manufactures/<int:pk>',
         ManufacturerAPIView.as_view(),
         name='manufacturer'),
]
