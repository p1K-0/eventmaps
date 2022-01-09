from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),
    path('account/login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('account/logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('register', views.register, name='register'),
]