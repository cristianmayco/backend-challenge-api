from django.contrib import admin

from .models import Manufacture


@admin.register(Manufacture)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
