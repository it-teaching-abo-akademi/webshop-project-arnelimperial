from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SellerConfig(AppConfig):
    name = 'seller'
    verbose_name = _('Seller')


