from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('room/new', views.br_new, name='br_new'),
    path('', views.br_view, name='br_rooms'),
    path('room/modify/<pk>', views.br_modify, name='br_modify'),

]