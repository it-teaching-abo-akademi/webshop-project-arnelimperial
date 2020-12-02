from django.contrib import admin
from .models import Cart
from users.admin import admin_log

admin.site.register(Cart)
admin_log.register(Cart)