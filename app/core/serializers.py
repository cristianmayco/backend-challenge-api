from rest_framework import serializers

from . import models


class ManufactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manufacture
        fields = ('id', 'name',)


class ProductSerializer(serializers.ModelSerializer):
    manufacture = ManufactureSerializer(read_only=True)

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
    products = ProductSerializer(many=True, read_only=True)
    consumer = ConsumerSerializer(read_only=True)
    delivery = DeliverySerializer(read_only=True)
    payment = PaymentSerializer(read_only=True)

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
