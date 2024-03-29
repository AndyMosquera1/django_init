"""django_init URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from aplicaciones.api import views
from aplicaciones.api.views import api_invoice, api_create_invoice

router=DefaultRouter()
router.register("Invoice",views.Invoiceapi)
router.register("Customer",views.Customerapi)
router.register("Items",views.Itemsapi)


schema_view = get_schema_view(
    openapi.Info(
        title="Back-End Emprendedor API",
        default_version='v1',
        description="Lógica de negocio de sitio de emprendedores",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="carlos.apariciov@ug.edu.ec"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('invoices/',api_invoice),
    path('create/invoice/',api_create_invoice),
    path('', include(router.urls)),
]
