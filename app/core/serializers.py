from rest_framework import serializers

from .models import Manufacture, Product


class ProductSerializer(serializers.ModelSerializer):
    # manufactures = ManufactureSerializer(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'barcode',
            # 'manufactures',
            'manufacture',
            'unit_price'
        )


class ManufactureSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Manufacture
        fields = ('id', 'name', 'products')
