from django.urls import path

from .views import client_view


app_name = "core"
urlpatterns = [
    path("", view=client_view, name="client-app"),
]