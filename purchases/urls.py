from .views import (
    purchase_list_view,
    purchase_detail_view,
    purchase_create_view,
    purchase_update_view,
    purchase_delete_view,
)

from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'purchases'
urlpatterns = [
    path('', view=purchase_list_view, name='purchase_list'),
    path('<int:pk>', view=purchase_detail_view, name='purchase_detail'),
    path('create/', view=purchase_create_view, name='purchase_create'),
    path('<int:pk>/update/', view=purchase_update_view, name='purchase_update'),
    path('<int:pk>/delete/', view=purchase_delete_view, name='purchase_delete'),
]
