from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='vdo_index'),
    path('vrform', views.vrform, name='vrform')
]
