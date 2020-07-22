from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

# V2 API
router = SimpleRouter()
router.register('products', views.ProductViewSet)
router.register('manufactures', views.ManufactureViewSet)
router.register('consumers', views.ConsumerViewSet)
router.register('orders', views.OrderViewSet)

urlpatterns = [
    path('manufactures/', views.ManufacturesAPIView.as_view(), name='manufactures'),
    path('manufactures/<int:pk>',
         views.ManufacturerAPIView.as_view(),
         name='manufacturer'),
    path('products/', views.ProductsAPIView.as_view(), name='products'),
    path('products/<int:pk>', views.ProductAPIView.as_view(), name='product'),
    path('consumers/', views.ConsumersAPIView.as_view(), name='consumers'),
    path('consumers/<int:pk>', views.ConsumerAPIView.as_view(), name='consumer'),
    path('orders/', views.OrdersAPIView.as_view(), name='orders'),
    path('orders/<int:pk>', views.OrderAPIView.as_view(), name='order'),
]
