from rest_framework import generics

from . import serializers, models


# API V1

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
