from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


UserModel = getattr(settings, 'AUTH_USER_MODEL')


class Product(models.Model):
    title = models.CharField(max_length=240)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='products')
    product_image = models.URLField(max_length=255, default='https://via.placeholder.com/150',blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)



    