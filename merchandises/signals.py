from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from merchandises.models import Merchandise
from core.utils import generate_random_string

# Generate unique slug even the given title was not unique
@receiver(pre_save, sender=Merchandise)
def add_slug_to_item(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        random_string = generate_random_string()
        instance.slug = slug + "-" + random_string
