from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('check-speed/', views.check_speed, name='check_speed')
]
