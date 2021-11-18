from rest_framework import serializers

from aplicaciones.facturacion.models import Invoice, Customer



class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = ['createtime','customer']

        def __str__(self):
            return self.first_name


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
