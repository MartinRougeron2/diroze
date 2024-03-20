from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:poll_id>/', poll_detail, name='poll_detail'),
    path('create/', poll_create, name='poll_create'),
    path('update/<int:poll_id>/', poll_update, name='poll_update'),
    path('delete/<int:poll_id>/', poll_delete, name='poll_delete'),
]