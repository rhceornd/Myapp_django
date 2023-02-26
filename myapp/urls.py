from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('/time', views.current_datetime, name='current_datetime')
]