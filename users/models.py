from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from merchandises.models import Merchandise

class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)

    # def get_absolute_url(self):
    #     return reverse("users:detail", kwargs={"username": self.username})
    class Meta:
        ordering = ['-id']

    # def save(self, *args, **kwargs):
    #     new_user = not self.pk
    #     super().save(*args, **kwargs)
    #     if new_user:
    #         Merchandise.objects.create(merchant=self)
           
