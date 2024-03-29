# Generated by Django 5.0.1 on 2024-01-31 01:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resourses', '0003_productsize_order_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productsize',
            options={'ordering': ['order']},
        ),
        migrations.RemoveField(
            model_name='productsizegroup',
            name='sizes',
        ),
        migrations.AddField(
            model_name='productsize',
            name='size_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resourses.productsizegroup'),
        ),
    ]
