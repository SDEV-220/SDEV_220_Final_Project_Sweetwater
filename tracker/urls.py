from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_logs/', views.view_logs, name='view_logs'),
    path('add_log/', views.add_log, name='add_log'),
    path('edit_log/', views.edit_log, name='edit_log'),
]