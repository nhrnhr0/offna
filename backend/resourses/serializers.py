
from typing import Any
from rest_framework import serializers
from .models import ProductSize,ProductSizeGroup,ProductColor,ProductCategory, Product


class IdListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        return data.values_list('id', flat=True)
    
class ListSerializer(serializers.ListSerializer):
    child = None
    # set the child to the field you want to serialize on init
    def __init__(self, child, *args, **kwargs):
        self.child = child
        super().__init__(*args, **kwargs)
    
    
    def to_representation(self, data):
        return [self.child.to_representation(item) for item in data.all()]

    
class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = '__all__'

class ProductSizeGroupSerializer(serializers.ModelSerializer):
    sizes_ids = serializers.PrimaryKeyRelatedField(many=True, source='productsize_set', queryset=ProductSize.objects.all())
    
    class Meta:
        model = ProductSizeGroup
        fields = ('id','name','sizes_ids')
        
    
class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
        
class GalleryItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    image = serializers.SerializerMethodField()
    
    def get_image(self, obj):
        from django.conf import settings
        photo_url = obj.image.url
        return settings.BASE_SERVER_URL + photo_url


# we have a problem that sizes and colors are many to many fields, and from the clientside we get them as a str of ids separated by commas
# so we need to create a custom field to handle this
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','header_image')


class ProductSerializer(serializers.ModelSerializer):
    gallery = ListSerializer(child=GalleryItemSerializer(), required=False)
    header_image = serializers.SerializerMethodField()
    def get_header_image(self, obj):
        from django.conf import settings
        
        photo_url = obj.header_image.url
        return settings.BASE_SERVER_URL + photo_url
    def update(self, instance, validated_data):
        print('update: ', validated_data)
        gallery = validated_data.pop('gallery', None)
        instance = super().update(instance, validated_data)
        if gallery is not None:
            gallery_ids = [item['id'] for item in gallery]
            instance.gallery.set(gallery_ids)
        return instance
    
    class Meta:
        model = Product
        fields = '__all__'
