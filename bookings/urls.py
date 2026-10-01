from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:worker_id>/', views.create_booking, name='create_booking'),
    path('my/', views.my_bookings, name='my_bookings'),
    path('dashboard/', views.worker_dashboard, name='worker_dashboard'),
    path('update/<int:booking_id>/<str:new_status>/', views.update_booking_status, name='update_booking_status'),
]
