from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from django.db.models import Q

from aplicaciones.api.serializers import InvoiceSerializer
from aplicaciones.facturacion.models import Invoice


class InvoiceList(APIView):
    def get(self, request):
        prod = Invoice.objects.all()
        data = InvoiceSerializer(prod, many=True).data
        print (data)
        return Response(data)
