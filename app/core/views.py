from rest_framework import generics

from . import serializers, models

# V2 API imports
from rest_framework import viewsets


# API V1 ROUTES

class ManufacturesAPIView(generics.ListCreateAPIView):
    queryset = models.Manufacture.objects.all()
    serializer_class = serializers.ManufactureSerializer


class ManufacturerAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Manufacture.objects.all()
    serializer_class = serializers.ManufactureSerializer


class ProductsAPIView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ConsumersAPIView(generics.ListCreateAPIView):
    queryset = models.Consumer.objects.all()
    serializer_class = serializers.ConsumerSerializer


class ConsumerAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Consumer.objects.all()
    serializer_class = serializers.ConsumerSerializer


class OrdersAPIView(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


"""API V2"""


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ManufactureViewSet(viewsets.ModelViewSet):
    queryset = models.Manufacture.objects.all()
    serializer_class = serializers.ManufactureSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class ConsumerViewSet(viewsets.ModelViewSet):
    queryset = models.Consumer.objects.all()
    serializer_class = serializers.ConsumerSerializer
