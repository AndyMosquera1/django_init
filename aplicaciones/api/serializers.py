from rest_framework import serializers

from aplicaciones.facturacion.models import Invoice, Customer, Items, Sku, Brand, Category


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Invoice
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class SkuSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()

    class Meta:
        model = Sku
        fields = '__all__'


class ItemsSerializer(serializers.ModelSerializer):
    sku = SkuSerializer()

    class Meta:
        model = Items
        fields = '__all__'
