from rest_framework import generics

from .models import Manufacture
from .serializers import ManufactureSerializer


# API V1

class ManufacturesAPIView(generics.ListCreateAPIView):
    queryset = Manufacture.objects.all()
    serializer_class = ManufactureSerializer


class ManufacturerAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manufacture.objects.all()
    serializer_class = ManufactureSerializer
