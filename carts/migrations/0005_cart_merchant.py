# Generated by Django 3.1.3 on 2020-11-17 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20201117_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='merchant',
            field=models.IntegerField(default=0),
        ),
    ]
