from django.urls import path
from .views import index, delete_city

app_name = 'weatherapp'
urlpatterns = [
    path('', index, name='home'),
    path('delete/<int:id>', delete_city, name='delete')
]
