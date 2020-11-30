# Generated by Django 3.1.3 on 2020-11-09 12:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBought',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bought', to='products.product')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
