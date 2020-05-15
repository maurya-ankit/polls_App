from django.urls import path, include

from . import views

app_name = 'register'
urlpatterns = [
    path('', views.register, name='register'),
    path('signin/', views.loginpage, name='signin'),
    path('logout/', views.logout_user, name='logout'),
]
