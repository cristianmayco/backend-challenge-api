from django.contrib import admin

from . import models


@admin.register(models.Manufacture)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'unit_price', ]


@admin.register(models.Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['id', 'mode']


@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'mode']


@admin.register(models.Consumer)
class ConsumerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(models.Order)
class Order(admin.ModelAdmin):
    list_display = ['id', 'status']
