from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from django.db.models import Q

from aplicaciones.api.serializers import InvoiceSerializer, CustomerSerializer, ItemsSerializer
from aplicaciones.facturacion.models import Invoice, Customer, Items


class Invoiceapi(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class Customerapi(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class Itemsapi(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
