from rest_framework import generics

from .models import Manufacture, Product
from .serializers import ManufactureSerializer, ProductSerializer


# API V1

class ManufacturesAPIView(generics.ListCreateAPIView):
    queryset = Manufacture.objects.all()
    serializer_class = ManufactureSerializer


class ManufacturerAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manufacture.objects.all()
    serializer_class = ManufactureSerializer


class ProductsAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
