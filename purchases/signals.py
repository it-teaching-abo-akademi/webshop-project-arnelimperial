from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta
from django.core.mail import send_mail, send_mass_mail, EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model
from merchandises.models import Merchandise
from purchases.models import Purchase
from carts.models import Cart


User = get_user_model()

## Update parent class (that belongs to queryset) on_stock field to false when Purchase object created 

def update_stock(sender, instance, **kwargs):
        merchandise_instance = Merchandise.objects.filter(id=instance.purchased_item_id).update(on_stock=False)
        cart_instance = Cart.objects.filter(item=instance.purchased_item_id).update(on_stock=False)


post_save.connect(update_stock, sender=Purchase)
       


default_sender = getattr(settings, 'DEFAULT_FROM_EMAIL')




@receiver(post_save, sender=Purchase)
def send_mail_to_buyer(sender, instance, created, **kwargs):
    if created:
        created_time = timezone.now() + timedelta(minutes=5)
        obj = Purchase.objects.filter(buyer=instance.buyer.id,created__lte=created_time)
        
        buyer_email = User.objects.get(username=instance.buyer_username).email
        sellers_email = User.objects.get(username=instance.sellers).email
        buyer_username = User.objects.get(username=instance.buyer_username)

       
        sub_buyer = "Purchase Notification"
        msg_for_buyer = 'Hi! {},\n\nThis notification only states that you have bought {} from {} via Nurtsrx.\n\n\nThank you,\n\nnurtsrx.herokuapp.com'.format(buyer_username, [l.purchased_item_name for l in obj], sellers_email)
        send_mail(sub_buyer, msg_for_buyer, default_sender, [buyer_email], fail_silently=False)

       
    


@receiver(post_save, sender=Purchase)
def send_mail_to_sellers(sender, instance, created, **kwargs):
    if created:
        created_time = timezone.now() + timedelta(minutes=5)
        obj = Purchase.objects.filter(sellers=instance.sellers,created__lte=created_time)
        obj1 = [item.purchased_item_name for item in obj]
        sellers_email = User.objects.get(username=instance.sellers).email
        sellers_username = User.objects.get(username=instance.sellers)

        sub_sellers = "Selling Notification"
        msg_for_sellers = 'Hi! {},\n\nThis notification states that your product/s({}) from Nurtsrx has been sold .\n\n\nThank you,\n\nnurtsrx.herokuapp.com'.format(sellers_username, obj1)
        send_mail(sub_sellers, msg_for_sellers, default_sender, [sellers_email], fail_silently=False)
       
      

       
