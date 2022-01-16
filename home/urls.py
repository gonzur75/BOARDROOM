from django.urls import path

from . import views

app_name = 'home'


urlpatterns = [
    path('room/new', views.br_new, name='br_new'),
    path('', views.br_view, name='br_rooms'),
    path('room/modify/<int:pk>', views.br_modify, name='br_modify'),
    path('room/del/<int:pk>', views.br_del, name='br_del'),
    path('room/reserve/<int:pk>', views.br_reserve, name='br_reserve'),

]
