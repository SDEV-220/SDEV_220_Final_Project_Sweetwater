from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_logs/', views.view_logs, name='view_logs'),
]