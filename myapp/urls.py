
# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('time/', views.current_datetime, name='current_datetime'),
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]