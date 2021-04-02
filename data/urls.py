from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # post testin if server is working up
    path('api/', views.verifySystem, name='test-api'),
    # post your rfid no here
    path('api/rfid/', views.verifyRFID, name='rfid-api'),
    # post your rfid , face , room id here
    path('api/face/', views.verifyRFID, name='rfid-api'),
    # post your leaving info here
    # scanned from inside , includes , rfid , room id
]
