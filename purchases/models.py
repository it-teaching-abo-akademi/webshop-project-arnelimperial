from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from merchandises.models import Merchandise
from carts.models import Cart
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
#from django.core.mail import send_mail, send_mass_mail

User = get_user_model()

UserModel = getattr(settings, 'AUTH_USER_MODEL')

default_sender = getattr(settings, 'DEFAULT_FROM_EMAIL')

class Purchase(models.Model):
    purchases = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='purchases')
    purchased_item_id = models.PositiveIntegerField(default=0) 
    purchased_item_name = models.CharField(max_length=60, default='')
    purchased_item_description = models.TextField(default='')
    purchased_item_product_image = models.URLField(max_length=255, default='https://via.placeholder.com/150',blank=True)
    buyer = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='buyer')
    buyer_username = models.CharField(max_length=30, default='')
    #buyer_email = models.CharField(max_length=100, default='')
    #sellers_email = models.CharField(max_length=100, default='')
    sellers = models.CharField(max_length=30)
    purchases_price = models.CharField(max_length=6, default='')
    purchases_price_dec = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    on_stock = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return '{}'.format(self.purchases)


    
    def save(self, *args, **kwargs):
        #created = self.pk is None
        self.buyer = self.purchases.customer
        self.purchased_item_id = self.purchases.item.id
        self.sellers = self.purchases.merchant
        #self.sellers_email = self.purchases.item.merchant
        self.buyer_username = self.purchases.customer.username
        self.purchases_price = self.purchases.item_price
        self.purchases_price_dec = self.purchases.item_price_dec
        self.purchased_item_name = self.purchases.item.title
        self.purchased_item_description = self.purchases.item.description
        self.purchased_item_product_image = self.purchases.item.product_image
        super().save(*args, **kwargs)
        #if created:

      
       



