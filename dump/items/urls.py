from . views import (
    item_list_view,
    item_detail_view,
    item_create_view,
    item_update_view,
    item_delete_view,
)

from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'items'
urlpatterns = [
    path('', view=item_list_view, name='item_list'),
    path('<slug:slug>', view=item_detail_view, name='item_detail'),
    path('create/', view=item_create_view, name='item_create'),
    path('<slug:slug>/update/', view=item_update_view, name='item_update'),
    path('<slug:slug>/delete/', view=item_delete_view, name='item_delete'),
]