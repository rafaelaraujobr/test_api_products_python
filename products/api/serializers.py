from rest_framework import serializers
from products import models


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Provider
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        # exclude = ["provider"]
        fields = '__all__'
