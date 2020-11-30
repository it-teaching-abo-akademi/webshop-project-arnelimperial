from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.utils.formats import localize_input, sanitize_separators
from django.core.validators import MaxLengthValidator, RegexValidator

UserModel = getattr(settings, 'AUTH_USER_MODEL')
User = get_user_model()

validate_price = RegexValidator('^[-,0-9]+$', 'Only numbers and commas are allowed.')

class Item(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=90, unique=True, editable=False)
    description = models.TextField(validators=[MaxLengthValidator(limit_value=53)])
    price = models.CharField(max_length=6, validators=[validate_price])
    price_dec = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    vendor = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='products', default=User.objects.filter(id=2).values('pk','username','email','password'))
    product_image = models.URLField(max_length=255, default='https://via.placeholder.com/150',blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return 'Item: {} by {}'.format(self.title, self.vendor)

    def get_absolute_url(self):
        return reverse('item_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        p = self.price.replace(",", ".")
        price = "{:.2f}".format(float(p))
        self.price_dec = price
        return super().save(*args, **kwargs)



    