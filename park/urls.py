from django.urls import path
from . import views

app_name = 'park'

urlpatterns = [
    path('parking_map/', views.parking_map, name="parking_map"),
    path('inquiry/', views.inquiry, name="inquiry"),
]