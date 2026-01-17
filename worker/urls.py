from . import views
from django.urls import path

urlpatterns = [
        path('register/', views.register, name="register"),
        path('register/form/', views.register_form, name="register_form"),
        path('dashboard/', views.dashboard, name="dashboard"),
        path('logout/', views.logout_view, name="logout"),
        path('login/', views.login_view, name="login"),
        path('edit/', views.edit_worker, name="edit_worker"),
        
]
