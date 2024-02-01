
from rest_framework import serializers
from .models import ProductSize,ProductSizeGroup


class IdListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        return data.values_list('id', flat=True)
    
        


class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = '__all__'

class ProductSizeGroupSerializer(serializers.ModelSerializer):
    sizes_ids = serializers.PrimaryKeyRelatedField(many=True, source='productsize_set', queryset=ProductSize.objects.all())
    
    class Meta:
        model = ProductSizeGroup
        fields = ('id','name','sizes_ids')