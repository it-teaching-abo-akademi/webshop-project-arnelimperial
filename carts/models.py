from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from merchandises.models import Merchandise
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

UserModel = getattr(settings, 'AUTH_USER_MODEL')

class Cart(models.Model):
    item = models.ForeignKey(Merchandise, on_delete=models.CASCADE, related_name='carts')
    customer = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='customers')
    merchant = models.CharField(max_length=20)
    item_price = models.CharField(max_length=6, default='')
    item_price_dec = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    on_stock = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return '{}'.format(self.item)
    
    # def get_item_price(self):
    #     return self.item.price

    # def get_item_price_dec(self):
    #     return self.item.price_dec
    
    # def get_item_merchant(self):
    #     return self.item.merchant
    
    # def get_item_merchant_email(self):
    #     return self.item.merchant.email
    
    def clean(self, *args, **kwargs):
        """[summary]
         Prevent merchant from selecting his/her own merchandise
        Raises:
            ValidationError: [description]
        """
        invalid_customer = Cart.objects.filter(merchant=self.customer)
        if self.customer == self.item.merchant:
            raise ValidationError("Invalid. You're the merchant of this item.")

        super(Cart, self).clean(*args, **kwargs)
    
    def save(self, *args, **kwargs):
       
        self.item_price = self.item.price
        self.item_price_dec = self.item.price_dec
        self.merchant = self.item.merchant
        # self.merchant_email = self.item.merchant.email

        self.full_clean()
        super().save(*args, **kwargs)
      
       


