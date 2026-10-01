from django.urls import path
from . import views

urlpatterns = [
    path('', views.worker_list, name='worker_list'),
    path('<int:worker_id>/', views.worker_detail, name='worker_detail'),
]
