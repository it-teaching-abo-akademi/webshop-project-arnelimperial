# Generated by Django 3.1.3 on 2020-11-23 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0005_auto_20201123_0422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='purchased_item_slug',
        ),
    ]
