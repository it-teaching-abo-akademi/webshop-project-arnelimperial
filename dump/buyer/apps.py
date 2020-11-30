from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _



class BuyerConfig(AppConfig):
    name = 'buyer'
    verbose_name = _('Buyer')

    # def ready(self):
    #     try:
    #         import buyer.signals  # noqa F401
    #     except ImportError:
    #         pass


