from django.db import models
# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Sku_item(models.Model):
    id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=False, related_name='brands')
    category = models.ForeignKey(Category,  on_delete=models.CASCADE, null=False, related_name='brands')

class Items(models.Model):
    id = models.AutoField(primary_key=True)
    gross = models.FloatField()
    discounts = models.FloatField()
    subtotal = models.FloatField()
    tax = models.FloatField()
    total = models.FloatField()
    sku = models.ForeignKey(Sku_item, on_delete=models.CASCADE, null=False, related_name='sku_items')

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    document_type = models.CharField(max_length=100)
    document_number = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    createtime = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, related_name='customers')
    item = models.ForeignKey(Items, on_delete=models.CASCADE, null=False, related_name='items_product')