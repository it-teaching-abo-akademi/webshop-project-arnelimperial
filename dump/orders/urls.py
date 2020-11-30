from .views import (
    orders_list_view,
    orders_detail_view,
    orders_create_view,
    orders_update_view,
    orders_delete_view,
)

from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'orders'
urlpatterns = [
    path('', view=orders_list_view, name='orders_list'),
    path('<int:pk>', view=orders_detail_view, name='orders_detail'),
    path('create/', view=orders_create_view, name='orders_create'),
    path('<int:pk>/update/', view=orders_update_view, name='orders_update'),
    path('<int:pk>/delete/', view=orders_delete_view, name='orders_delete'),
]

