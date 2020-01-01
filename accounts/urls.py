from django.urls import path

from . import views #'.' denotes from this (accounts) folder

urlpatterns = [
    
    path('signup',views.signup, name='signup'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
]  