from . views import (
    products_list_view,
    products_detail_view,
    products_create_view,
    products_update_view,
    products_delete_view,
)

from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'products'
urlpatterns = [
    path('', view=products_list_view, name='products_list'),
    path('<slug:slug>', view=products_detail_view, name='products_detail'),
    path('create/', view=products_create_view, name='products_create'),
    path('<slug:slug>/update/', view=products_update_view, name='products_update'),
    path('<slug:slug>/delete/', view=products_delete_view, name='products_delete'),
]