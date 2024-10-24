from django.shortcuts import render, get_object_or_404, redirect
from decouple import config
import requests
from pprint import pprint
from django.contrib import messages
from .models import City
#! profile_pic. için
from users.models import UserProfile

# Create your views here.
def index(request):
    
    API_KEY = config('API_KEY')
    city = 'Yozgat'
        
    u_city = request.POST.get('name')
    
    # eğer kullanıcı şehir ismi girdiyse;
    if u_city:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={u_city}&lang=tr&appid={API_KEY}&units=metric' # &lang=tr ile türkçe yapılıyor.
        response = requests.get(url)
        # print(response.ok)
        
        if response.ok:
            content = response.json()
            r_city = content['name']
            if City.objects.filter(name=r_city):
                messages.warning(request, 'City already exist!')
            else:
                City.objects.create(name=r_city)
        
        else:
            messages.warning(request, 'There is no city')

    
    city_data = []
    # cities = City.objects.all().order_by('name')
    cities = City.objects.all().order_by('-id')
    for city in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang=tr&appid={API_KEY}&units=metric' # &lang=tr ile türkçe yapılıyor.
        response = requests.get(url)
        content = response.json()
        data = {
            # 'city': content['name'],
            'city': city, # 1. yol for'daki city objesi
            'temp': content['main']['temp'],
            'icon': content['weather'][0]['icon'],
            'desc': content['weather'][0]['description'],
            # 'id': city.id, # 2. yol for'daki city objesi'nin id'si
        }
        city_data.append(data)
        # 1. yol;
        # print(city.id)
        # print(city.id)
    
    # pprint(city_data)
    
    #! profile_pic. için
    profile = None
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
    
    
    context = {
        'city_data': city_data,
        'profile': profile, #! profile_pic. için
    }

    return render(request, 'weatherapp/index.html', context)

def delete_city(request, id):
    city = get_object_or_404(City, id=id)
    city.delete()
    messages.warning(request, 'City deleted.')
    return redirect('weatherapp:home')