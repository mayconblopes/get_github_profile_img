from django.urls import path
from . import views

urlpatterns = [
    path('', views.getgit, name='getgit'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('images', views.images, name='images'),
    path('getgit', views.getgit, name='getgit'),
    path('getface', views.getface, name='getface'),

]