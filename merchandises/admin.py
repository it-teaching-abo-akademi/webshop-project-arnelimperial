from django.contrib import admin
from .models import Merchandise
from users.admin import admin_log

admin.site.register(Merchandise)
admin_log.register(Merchandise)