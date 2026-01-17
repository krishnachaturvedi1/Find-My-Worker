from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_workers, name='search_workers'),
    path('dashboard/<int:worker_id>/', views.worker_dashboard, name='worker_dashboard'),
]
