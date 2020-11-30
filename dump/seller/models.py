from django.db import models
from django.utils import timezone
from products.models import Product


class ProductSold(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sold')
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return '{} sold'.format(self.product_name)

    
    