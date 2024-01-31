
from rest_framework import serializers
from .models import ProductSize,ProductSizeGroup


class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = '__all__'

class ProductSizeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSizeGroup
        fields = '__all__'