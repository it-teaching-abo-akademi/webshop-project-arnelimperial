from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from django.core.exceptions import ValidationError


UserModel = getattr(settings, 'AUTH_USER_MODEL')


class Initial(models.Model):
    name = models.CharField(max_length=255, default='init')
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return 'Initial {} created at {} '.format(self.name,self.created_date)

    
   
    