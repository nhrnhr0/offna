from django.contrib import admin
from .models import ProductSize ,ProductSizeGroup ,ProductColor ,ProductCategory ,GalleryImage ,Product
from django.utils.safestring import mark_safe
# Register your models here.

class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('id','size','size_group', 'order')
    search_fields = ('size',)
    list_editable = ('size', 'size_group', 'order')
    
    
admin.site.register(ProductSize,ProductSizeAdmin)

class ProductSizeGroupAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'sizes_list')
    search_fields = ('name',)
    def sizes_list(self, obj):
        return ", ".join([p.size for p in obj.sizes.all()])
admin.site.register(ProductSizeGroup,ProductSizeGroupAdmin)

class ProductColorAdmin(admin.ModelAdmin):
    list_display = ('id','color')
    search_fields = ('color',)
admin.site.register(ProductColor,ProductColorAdmin)

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)
admin.site.register(ProductCategory,ProductCategoryAdmin)

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id','image', 'image_tag')
    search_fields = ('image',)
    def image_tag(self, obj):
        return mark_safe(u'<img width="50px" height="50px" src="%s" />' % obj.image.url)
    image_tag.short_description = 'Image'
admin.site.register(GalleryImage,GalleryImageAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','sizes_list','colors_list','category','price','description','gallery_list','size_group')
    search_fields = ('name',)
    filter_horizontal = ('sizes','colors','gallery')
    def sizes_list(self, obj):
        return ", ".join([p.size for p in obj.sizes.all()])
    def colors_list(self, obj):
        return ", ".join([p.color for p in obj.colors.all()])
    def gallery_list(self, obj):
        return ", ".join([p.image.url for p in obj.gallery.all()])
admin.site.register(Product,ProductAdmin)
