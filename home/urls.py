from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('room/new', views.new_room, name='new_room'),

]