from .views import (
    initial_list_view,
    initial_detail_view,
    initial_create_view,
    
)

from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'initial'
urlpatterns = [
    path('', view=initial_list_view, name='initial_list'),
    path('<int:pk>', view=initial_detail_view, name='initial_detail'),
    path('create/', view=initial_create_view, name='initial_create'),
]

