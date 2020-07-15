from django.contrib import admin

from .models import Manufacture, Product


@admin.register(Manufacture)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'unit_price', ]
