from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:user_id>/', user_detail, name='user_detail'),
    path('create/', user_create, name='user_create'),
    path('update/<int:user_id>/', user_update, name='user_update'),
    path('delete/<int:user_id>/', user_delete, name='user_delete'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
]