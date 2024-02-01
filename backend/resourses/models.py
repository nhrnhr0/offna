from django.db import models

# Create your models here.
class ProductSize(models.Model):
    size = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    size_group = models.ForeignKey('ProductSizeGroup', on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        ordering = ['size_group','order']
    
    def __str__(self):
        return self.size

class ProductSizeGroup(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ProductColor(models.Model):
    color = models.CharField(max_length=100)
    def __str__(self):
        return self.color

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.image.url

class Product(models.Model):
    name = models.CharField(max_length=100)
    sizes = models.ManyToManyField(ProductSize, blank=True)
    colors = models.ManyToManyField(ProductColor, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    description = models.TextField(blank=True)
    gallery = models.ManyToManyField(GalleryImage, blank=True)
    size_group = models.ForeignKey(ProductSizeGroup, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name