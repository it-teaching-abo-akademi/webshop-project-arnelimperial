# Generated by Django 3.1.3 on 2020-11-14 23:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Merchandise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('slug', models.SlugField(editable=False, max_length=90, unique=True)),
                ('description', models.TextField(validators=[django.core.validators.MaxLengthValidator(limit_value=53)])),
                ('price', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^[-,0-9]+$', 'Only numbers and commas are allowed.')])),
                ('price_dec', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('product_image', models.URLField(blank=True, default='https://via.placeholder.com/150', max_length=255)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='merchandises', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
