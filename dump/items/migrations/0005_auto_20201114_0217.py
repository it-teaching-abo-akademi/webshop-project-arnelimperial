# Generated by Django 3.1.3 on 2020-11-14 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20201114_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=80),
        ),
    ]
