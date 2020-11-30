from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class InitialConfig(AppConfig):
    name = 'initial'
    verbose_name = _('Initial')

    def ready(self):
        try:
            import initial.signals 
        except ImportError:
            pass



