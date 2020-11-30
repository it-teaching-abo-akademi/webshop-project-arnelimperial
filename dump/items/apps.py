from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ItemsConfig(AppConfig):
    name = 'items'
    verbose_name = _('Items')

    def ready(self):
        try:
            import items.signals
        except ImportError:
            pass


