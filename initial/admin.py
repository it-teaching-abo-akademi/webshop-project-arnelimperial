from django.contrib import admin
from .models import Initial
from users.admin import admin_log

admin.site.register(Initial)
admin_log.register(Initial)