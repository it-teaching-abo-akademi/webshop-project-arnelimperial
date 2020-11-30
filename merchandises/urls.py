from .views import (
    merchandise_list_view,
    merchandise_detail_view,
    merchandise_create_view,
    merchandise_update_view,
    merchandise_delete_view,
)

from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'merchandises'
urlpatterns = [
    path('', view=merchandise_list_view, name='merchandise_list'),
    path('<slug:slug>', view=merchandise_detail_view, name='merchandise_detail'),
    path('create/', view=merchandise_create_view, name='merchandise_create'),
    path('<slug:slug>/update/', view=merchandise_update_view, name='merchandise_update'),
    path('<slug:slug>/delete/', view=merchandise_delete_view, name='merchandise_delete'),
]