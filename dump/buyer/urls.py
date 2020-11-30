from .views import (
    buyer_list_view,
    buyer_detail_view,
    buyer_create_view,
    buyer_update_view,
    buyer_delete_view,
)

from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'buyer'
urlpatterns = [
    path('', view=buyer_list_view, name='buyer_list'),
    path('<int:pk>', view=buyer_detail_view, name='buyer_detail'),
    path('create/', view=buyer_create_view, name='buyer_create'),
    path('<int:pk>/update/', view=buyer_update_view, name='buyer_update'),
    path('<int:pk>/delete/', view=buyer_delete_view, name='buyer_delete'),
]

