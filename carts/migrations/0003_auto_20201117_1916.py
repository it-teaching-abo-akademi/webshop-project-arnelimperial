# Generated by Django 3.1.3 on 2020-11-17 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_auto_20201116_1810'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['-created']},
        ),
    ]
