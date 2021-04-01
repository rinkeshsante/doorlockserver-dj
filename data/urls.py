from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rfid/', views.getId, name='rfid-api')
]
