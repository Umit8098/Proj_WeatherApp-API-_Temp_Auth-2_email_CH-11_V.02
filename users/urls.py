from django.urls import path
from .views import (
    user_logout,
    register,
    user_login,
)

app_name = 'users'
urlpatterns = [
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
] 
