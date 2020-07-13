from rest_framework import serializers

from .models import Manufacture


class ManufactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacture
        fields = ('id', 'name')
