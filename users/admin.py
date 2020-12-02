from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.sites.models import Site
from rest_framework.authtoken.models import Token 
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount, SocialToken, SocialApp
from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.models import TOTPDevice

from users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser", "id"]
    search_fields = ["name"]


class OTPAdmin(OTPAdminSite):
    pass

admin_log = OTPAdmin(name='OTPAdmin')


admin_log.register(User, UserAdmin)
admin_log.register(TOTPDevice)
admin_log.register(Group)
admin_log.register(Permission)
admin_log.register(Site)
admin_log.register(Token)
admin_log.register(EmailAddress)
admin_log.register(SocialAccount)
admin_log.register(SocialToken)
admin_log.register(SocialApp)




