from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from django.db.models import Q

from aplicaciones.api.serializers import InvoiceSerializer, CustomerSerializer, ItemsSerializer
from aplicaciones.facturacion.models import Invoice, Customer, Items, Category


@api_view(['GET'])
def api_invoice(request):
    id_params = request.GET.get('id')
    queryset = ''
    if id_params != None:
        queryset = Invoice.objects.filter(id=id_params)
    else:
        queryset = Invoice.objects.all()

    serializer_class = InvoiceSerializer(queryset, many=True)
    dicc = {'id': '', 'createtime': '', 'document_number': '', 'customer': '', 'items': ''}

    for x in queryset:
        queryset_invoice = Invoice.objects.filter(id=x.id)
        dicc['id'] = x.id
        dicc['createtime'] = x.createtime
        dicc['customer'] = SerializaCustomer(x.customer_id)
        queryset_item = Items.objects.filter(invoice_id=x.id)
        dicc['items'] = ItemsSerializer(queryset_item, many=True).data

    # dicc = {'api':serializer_class.data}
    return Response(dicc)


@api_view(['POST'])
def api_create_invoice(request):
    data = request.data
    serializers = ItemsSerializer(data=data)
    if serializers.is_valid():
        serializers.save()
        return Response(data)
    else:
        return Response(serializers.error_messages)


def SerializaCustomer(id_customer):
    response = CustomerSerializer(Customer.objects.filter(id=id_customer), many=True).data[0]
    return response

def ConsultCustomer(id):
    queryset=Customer.objects.filter(id=id)
    return queryset

class Invoiceapi(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class Customerapi(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class Itemsapi(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
