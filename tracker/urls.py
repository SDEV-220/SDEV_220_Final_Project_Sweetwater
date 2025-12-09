from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_logs/<str:username>/', views.view_specific_log, name='view_logs'),
    path('view_logs/', views.view_logs, name='view_logs'),
    path('add_log/', views.add_log, name='add_log'),
    path('edit_log/<int:pk>/', views.edit_log, name='edit_log'),
    path('delete_log/<int:pk>/', views.delete_log, name='delete_log'),
]