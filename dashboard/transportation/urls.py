from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('transportation', views.transportation, name='transportation'),
    path('diabetes', views.transportation, name='diabetes'),
    path('nutrition', views.transportation, name='nutrition'),
]

