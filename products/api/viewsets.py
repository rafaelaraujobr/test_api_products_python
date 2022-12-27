from rest_framework import viewsets

from products.models import Product
from products.models import Provider
from products.api.serializers import ProductSerializer
from products.api.serializers import ProviderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
