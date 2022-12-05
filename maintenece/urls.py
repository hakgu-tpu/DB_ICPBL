from django.urls import path
from myapp import views

app_name = 'maintenence'

urlpatterns = [
    path('', views.index_1),
    path('<int:date>/', views.detail_1, name='detail'),
]
