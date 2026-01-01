from django.urls import path
from . import views

app_name = 'logs'

urlpatterns = [
    path('', views.bodylog_list, name='index'),                             # http://127.0.0.1:8000/logs/
    path('create/', views.bodylog_create, name='create'),                   # http://127.0.0.1:8000/logs/create/
    path('<int:pk>/edit/', views.bodylog_edit, name='edit'),                # http://127.0.0.1:8000/logs/<int:pk>/edit/
    path('<int:pk>/delete/', views.bodylog_delete, name='delete'),          # http://127.0.0.1:8000/logs/<int:pk>/delete/
    path('api/log/<int:pk>/', views.log_detail_api, name='log_detail_api'), # http://127.0.0.1:8000/logs/api/log/<int:pk>/
]