from django.contrib import admin
from purchases.models import Purchase
from users.admin import admin_log

admin.site.register(Purchase)
admin_log.register(Purchase)