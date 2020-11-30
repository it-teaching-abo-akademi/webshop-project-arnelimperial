from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class MerchandisesConfig(AppConfig):
    name = 'merchandises'
    verbose_name = _('Merchandises')

    def ready(self):
        try:
            import merchandises.signals
        except ImportError:
            pass


