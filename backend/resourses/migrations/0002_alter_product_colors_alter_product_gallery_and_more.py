# Generated by Django 5.0.1 on 2024-01-30 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resourses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(blank=True, to='resourses.productcolor'),
        ),
        migrations.AlterField(
            model_name='product',
            name='gallery',
            field=models.ManyToManyField(blank=True, to='resourses.galleryimage'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(blank=True, to='resourses.productsize'),
        ),
    ]
