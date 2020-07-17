from rest_framework import serializers

from . import models


class ManufactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manufacture
        fields = ('id', 'name',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = (
            'id',
            'name',
            'description',
            'barcode',
            'manufacture',
            'unit_price'
        )


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Delivery
        fields = ('id', 'mode',)


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = ('id', 'mode', 'installments')


class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Consumer
        fields = ('id', 'name', 'phone', 'email')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = (
            'id',
            'products',
            'consumer',
            'delivery',
            'payment',
            'status'
        )
