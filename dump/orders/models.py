from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from products.models import Product
from django.core.exceptions import ValidationError

UserModel = getattr(settings, 'AUTH_USER_MODEL')

class Cart(models.Model):
    buyer = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='carts')
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    sold = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    cost = models.PositiveIntegerField()

    def __str__(self):
        return '{} items({}) sold by: {}'.format(self.quantity, self.item, self.buyer)


    def clean(self, *args, **kwargs):
        """[summary]
         Prevent seller from selecting his/her own product
        Raises:
            ValidationError: [description]
        """
        customer = Product.objects.filter(seller=self.buyer)
        if customer:
            raise ValidationError("Invalid. You're the seller of this item/s.")

        super(Cart, self).clean(*args, **kwargs)


    def save(self, *args, **kwargs):
        total = self.item.price * self.quantity
        self.cost = total
        self.full_clean()
        super().save(*args, **kwargs)
