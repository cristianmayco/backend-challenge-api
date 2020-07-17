from django.db import models


class Manufacture(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    barcode = models.CharField(max_length=15)
    manufacture = models.ForeignKey(Manufacture, related_name='manufactures', on_delete=models.DO_NOTHING)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    mode = models.CharField(max_length=120)

    def __str__(self):
        return self.mode


class Payment(models.Model):
    mode = models.CharField(max_length=120)
    installments = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.mode


class Consumer(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=13)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Order(models.Model):
    products = models.ManyToManyField(Product)
    consumer = models.ForeignKey(Consumer, on_delete=models.DO_NOTHING)
    delivery = models.ForeignKey(Delivery, on_delete=models.DO_NOTHING)
    payment = models.ForeignKey(Payment, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=(
        ('P', 'Peding confirmation'),
        ('C', 'Order confirmed'),
        ('W', 'Order awaiting delivery'),
        ('D', 'Òrder deliveried')
    ), default='P')
