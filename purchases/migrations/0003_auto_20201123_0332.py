# Generated by Django 3.1.3 on 2020-11-23 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0002_auto_20201121_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='purchased_item_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='purchase',
            name='purchased_item_name',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='purchase',
            name='purchased_item_product_image',
            field=models.URLField(blank=True, default='https://via.placeholder.com/150', max_length=255),
        ),
    ]
