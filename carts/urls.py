from .views import (
    cart_list_view,
    cart_detail_view,
    cart_create_view,
    cart_update_view,
    cart_delete_view,
)

from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'carts'
urlpatterns = [
    path('', view=cart_list_view, name='cart_list'),
    path('<int:pk>', view=cart_detail_view, name='cart_detail'),
    path('create/', view=cart_create_view, name='cart_create'),
    path('<int:pk>/update/', view=cart_update_view, name='cart_update'),
    path('<int:pk>/delete/', view=cart_delete_view, name='cart_delete'),
]

