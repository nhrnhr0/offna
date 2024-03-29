# Generated by Django 5.0.1 on 2024-02-08 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resourses', '0007_product_created_at_product_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='productcolor',
            name='color',
            field=models.CharField(default='#000000', max_length=100),
        ),
        migrations.AlterField(
            model_name='productcolor',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
