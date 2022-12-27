from rest_framework import serializers
from products import models


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Provider
        fields = ('name', 'email', 'phone', 'created_at')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        # exclude = ["provider"]
        fields = '__all__'
