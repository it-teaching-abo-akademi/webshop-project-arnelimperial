from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PurchasesConfig(AppConfig):
    name = 'purchases'
    verbose_name = _('Purchases')

    def ready(self):
        try:
            import purchases.signals 
        except ImportError:
            pass

    
