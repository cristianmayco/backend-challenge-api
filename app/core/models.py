from django.db import models


class Manufacture(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    barcode = models.CharField(max_length=15)
    manufacture = models.ForeignKey(Manufacture, related_name='products', on_delete=models.DO_NOTHING)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
