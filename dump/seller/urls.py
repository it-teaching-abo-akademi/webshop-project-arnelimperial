from .views import (
    seller_list_view,
    seller_detail_view,
    seller_create_view,
    seller_update_view,
    seller_delete_view,
)

from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'seller'
urlpatterns = [
    path('', view=seller_list_view, name='seller_list'),
    path('<int:pk>', view=seller_detail_view, name='seller_detail'),
    path('create/', view=seller_create_view, name='seller_create'),
    path('<int:pk>/update/', view=seller_update_view, name='seller_update'),
    path('<int:pk>/delete/', view=seller_delete_view, name='seller_delete'),
]

