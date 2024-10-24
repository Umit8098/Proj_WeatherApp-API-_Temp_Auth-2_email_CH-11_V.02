
#### Baştan proje kurulumu ->

```bash
- python -m venv env
- ./env/Scripts/activate
- pip install django
- django-admin --version
- python.exe -m pip install --upgrade pip
- pip freeze
- pip install python-decouple
- pip freeze > requirements.txt # or - pip install -r requirements.txt
- django-admin startproject weather .
- py manage.py startapp weatherapp
- py manage.py migrate
- python manage.py createsuperuser
- py manage.py runserver
```


///////////////////////////////////////////////////
#### GİTHUB REPODAN clone bir projeyi ayağa kaldırma ->

```bash
- python -m venv env
- ./env/Scripts/activate
- pip install -r requirements.txt
- python.exe -m pip install --upgrade pip
- pip install python-decouple
- pip freeze > requirements.txt
```

- create .env and inside create SECRET_KEY 

```bash
- python manage.py migrate
- python manage.py runserver
```

///////////////////////////////////////////////////

### Secure your project

### .gitignore

.gitignore
```py
# Environments
.env
.venv
env/
venv/
```

### python-decouple

- Create .env file on root directory. We will collect our variables in this file.

.env
```py
SECRET_KEY = django-insecure-9p72pxko$)cm=wwzt81kg*6u-%#j*iyxhens02^96bw&iq2idn
```

settings.py
```py
from decouple import config

SECRET_KEY = config('SECRET_KEY')
```

- From now on you can send you project to the github, but double check that you added a .gitignore file which has .env on it.


- Projeyi ve app imizi oluşturduk, .gitignore ve .env dosyalarımızı da oluşturup SECRET_KEY imizi ve env ımızı içerisine koyduk.

- app imizi settings.py daki INSTALLED_APPS e ekliyoruz.

- Eğer kullanacaksak; 'crispy_forms' ve 'bootstrap5' paketlerini kurup INSTALLED_APPS'e ekliyoruz.

- projede media file kullanacaksak eğer; için MEDIA_ROOT ve MEDIA_URL settings.py'a ekliyoruz. urls.py'da ayarlarını yapıyoruz.
  
settings.py
```py
  INSTALLED_APPS = [
    ...
    # myApps
    'weatherapp',
]
```

- Run the server and see the initial setup:
 
```bash
- py manage.py migrate
```

```bash
- py manage.py runserver  # or;
- python manage.py runserver  # or;
- python3 manage.py runserver
```


### urls configurasyonu oluştur;

- go to app folder and create app's urls.py
- (oluşturulan app klasöründe urls.py dosyası oluştur.)

- go to project urls.py and include app's urls.py
- (project urls.py'ında, app'in altındaki urls.py'ı include et.)

weather/urls.py
```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weatherapp.urls')),
]
```

weatherapp/urls.py
```py
from django.urls import path

urlpatterns = [
]
```

### templates için folder configurasyonu oluştur;

- go to app views.py and create a view like 'index','home' and rendered template
- (app views.py'ında 'index.html', 'home.html' gibi templateleri render edecek viewler oluştur. )

weatherapp/views.py
```py
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'weatherapp/index.html')
```

- go to app folder and under the folder create templates/weatherapp folder and inside create template file like index.html.
- (app klasöründe templates/weatherapp yapısında klasörleri oluştur. İçerisine 'index.html', 'home.html' gibi templatelerini oluştur.)

weatherapp/templates/weatherapp/index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WeatherApp</title>
</head>
<body>
    <h1>Weather App</h1>
</body>
</html>
```

- yazdığımız view ve template'in path'ini oluşturalım;

weatherapp/urls.py
```py
...
from .views import index


urlpatterns = [
    path('', index, name='home')
]
```


### API Application Programming Interface
    
    https://aws.amazon.com/tr/what-is/api/


- Tüm siteler API hizmeti sunmayabilir. Bunu sunmayan kaynaklardan da bazı yöntemlerle veri çekebiliyoruz. Kaynaklarını paylaşmayan uygulamalardan da bazı yöntelmelerle verileri çekebiliyoruz. Örneğin web scraping.

- Python un da beatiful-soap diye bir kütüphanesi var web scraping ile ilgili.

- e-ticaret sitelerinden veri çekmek için web scraping uygulamaları kullanılıyor.

- seleniumla yapılıyor.

- Biz de kendimiz RESTfull tarafında django ile API endpointler yazacağız. Kendi verilerimizi dışarı aktarıyor olacağız.

- Doküman hususu önemli. (API dokümanı)


#### openweathermap 

- API kaynagı olarak https://openweathermap.org/ sitesinin verilerini kullanacağız.

- API kaynagı olarak kullanacağımız site'ye register oluyoruz. (Ben register oldum. kullanıcı adı ve şifre chrome'da kayıtlı)

- openweathermap'de Current Weather Data (Anlık hava durumu verileri) kısmını kullanacağız.
- API doc linkine tıkladığımızda, How to make an API call (API çağrısı nasıl yapılır) kısmında bir link veriyor.Bu link ile API isteği/çağrısında bulunuyoruz. Burada çeşitli seçenekler de var. Bu seçenekler arasından Built-in API request by city name (şehir ismine göre API isteği) olan endpoint'i kullanacağız. Ona tıklıyoruz,  

##### openweather link, API key alma;

- End point imi aldım; 
    
    https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

- parametre olarak, 'city name' ve 'API key' istiyor bizden. Bunları sağladıktan sonra bu endpoint'e istek atabiliriz.
 
- ayrıca hemen altta çeşitli parametreler de var. 
  - appid parametresini eklememiz gerekiyor.
  
  - Mesela Default olarak JSON formatında veri gelecek olan veriyi 'mode' parametresiyle 'xml', 'html' olarak değiştirebiliriz.
  
  - units parametresini de kullanacağız.

- Tamam, şimdi şehir ismine göre olan endpoint'i alıp, çalışacağımız yer olan weatherapp app'imizin views.py ındaki index view'imize url değişkenine tanımlıyoruz. Ayrıca f" sring e çeviriyoruz.


weatherapp/views.py

```py
...

def index(request):
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'
    
    return render(request, 'weatherapp/index.html')
```

- üyesi olduğumuz openweatherapp sitesinin bize verdiği API_KEY i (navbar'daki kullanıcı adımıza tıklayıp açılan menüden MyAPI keys linkine tıklayıp, oradan API key'imizi alabiliriz.) alıp aynı SECRET_KEY gibi .env dosyasına kaydediyoruz,
- ardından weatherapp/views.py'da decouple dan config i import edip, aşağıda API_KEY imizi çağırıyoruz. f-string ile de endpoint'in içine API_KEY'imizi yerleştiriyoruz.

.env
```py
API_KEY=e7dfd8d9f4ce5948e8881d2f5515c605
```

weatherapp/views.py
```py
from decouple import config

def index(request):

    API_KEY = config('API_KEY')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API_KEY}'
    
    return render(request, 'weatherapp/index.html')
```

- city değişkeni oluşturup bir city ismi veriyoruz.city ve API_KEY olarak f' string imizi ayarlıyoruz. Böylelikle url imizde bizden istenen queryleri, değişkenleri yukarıda tanımlıyoruz. city ve API_KEY.
    
weatherapp/views.py
```py
def index(request):
    API_KEY = config('API_KEY')
    city = 'Yozgat'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

```

- Artık url imize istek atabiliriz. 
- Python da istek atabilmek için requests modülümüz var. Önce requests modülümüzü install ediyoruz,
  
```bash
- pip install requests
- pip freeze > requirements.txt
```

- views.py'da requests modülümüzü import ediyoruz. requests.get(url) ile istek atıp dönen veriyi de response değişkenine tanımlayıp print ile de terminalde ne geldiğine bakıyoruz. 
- print ile ne geldiğine bakmak için template imizi render etmemiz gerekiyor, runserver ve ne geldiğini görüyoruz. terminalde ->  <Response [200]>

weatherapp/views.py
```py
from django.shortcuts import render
from decouple import config
import requests

def index(request):
    ...
    response = requests.get(url)
    print(response)
    
    ...
```


##### json(), pprint() methodları

- response a gelen verilerimizi content diye bir değişkene atayarak response dan çekebiliriz.
- burada response bir obje gibi ama aslında çektiğimiz veriler bu response'un içerisinde. Bunları json() methodunu kullanarak response'un içinden çıkarabiliriz. 
- Burada response.json() ile response içerisindeki verileri json() methodu ile çıkarıyoruz. 
- json() methodu ne işe yarıyor? json tipinde gelen veriyi python dictionary yapısına çeviriyor.

weatherapp/views.py
```py
...

def index(request):
    
    API_KEY = config('API_KEY')
    city = 'Yozgat'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    content = response.json()
    print(content)
    
    return render(request, 'weatherapp/index.html')
```


- Gelen veriyi terminalde görüyoruz, daha düzgün görünmesi için pprint'ten pprint i import edip pprint() kullanıyoruz.
- view'imizi tekrar urls'deki endpointimizden tetikleyerek çalıştırıyoruz.

weatherapp/views.py

```py
from pprint import pprint

def index(request):
    
    API_KEY = config('API_KEY')
    city = 'Yozgat'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    content = response.json()
    pprint(content)
    
    ...
```


- Terminale gelen veri aşağıdaki gibi-> ;
  
```bash
{'base': 'stations',
 'clouds': {'all': 29},
 'cod': 200,
 'coord': {'lat': 39.5833, 'lon': 35.3333},
 'dt': 1663151893,
 'id': 296560,
 'main': {'feels_like': 292.93,
          'grnd_level': 889,
          'humidity': 37,
          'pressure': 1013,
          'sea_level': 1013,
          'temp': 293.84,
          'temp_max': 293.84,
          'temp_min': 293.84},
 'name': 'Yozgat Province',
 'sys': {'country': 'TR', 'sunrise': 1663125519, 'sunset': 1663170618},
 'timezone': 10800,
 'visibility': 10000,
 'weather': [{'description': 'scattered clouds',
              'icon': '03d',
              'id': 802,
              'main': 'Clouds'}],
 'wind': {'deg': 11, 'gust': 2.51, 'speed': 2.59}}
```


- Şimdi verinin içinden istediklerimizi alıyoruz;
- Bunun için deictionary'den veri çekme methodunu ['name'] kullanıyoruz.
- Ancak mesela weather tek elemanlı bir liste, onun tek elemanını alırken index numarasıyla [0] alıyoruz, ve o tek elemanı da bir dictionary. onu da yine ['description'] şeklinde dict methoduyla alıyoruz. ->  pprint(content['weather'][0]['icon'])

weatherapp/views.py

```py
...

def index(request):
    
    API_KEY = config('API_KEY')
    city = 'Yozgat'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    content = response.json()
    # pprint(content)
    pprint(content['name'])
    pprint(content['main']['temp'])
    pprint(content['weather'][0]['description'])
    pprint(content['weather'][0]['icon'])
    
    ...
```

- Çektiğimiz veriyi gördük, terminalde inceledik, 
- template'e göndermek için dictionary yapısında context içerisine koyuyor ve template de bu veileri çekip gösteriyoruz.

weatherapp/views.py
```py
...

def index(request):
    
    API_KEY = config('API_KEY')
    city = 'Yozgat'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    content = response.json()
    # pprint(content)
    pprint(content['name'])
    pprint(content['main']['temp'])
    pprint(content['weather'][0]['description'])
    pprint(content['weather'][0]['icon'])
    
    context = {
        'city': content['name'],
        'temp': content['main']['temp'],
        'icon': content['weather'][0]['icon'],
        'desc': content['weather'][0]['description'],
    }
    
    return render(request, 'weatherapp/index.html', context)

```

- index view imizin template'i olan ->

weatherapp/templates/weatherapp/index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WeatherApp</title>
</head>
<body>
    <h1>Weather App</h1>

    {{city}} <br>
    {{temp}} <br>
    {{icon}} <br>
    {{desc}} <br>
    
</body>
</html>
```

##### openweathermap iconlarının kullanımı

- openweathermap icon larını nasıl kullanacağız?
  
- https://openweathermap.org/   sayfasına gidiyoruz, API leri aldığımız yere gidip Ctrl+f ile "icon" diye aratınca (List of weather condition codes kısmında), weather condition codes with icon kısmından linke tıklayıp, ilgili sayfaya geliyoruz. 

    https://openweathermap.org/weather-conditions

- Burada icon'ların id'lerine karşılık gelen resimler görünüyor.
- verdiği url'i alıp, icon id'sini değiştirerek, değişen icon'a göre resim çekebiliriz.
- url'i alıyoruz,
- bu aldığımız url aslında bir image. url i alıp, bir image tag i içerisinde image src="http://openweathermap.org/img/wn/10d@2x.png" şeklinde yazıyoruz, 
- Ancak icon un kodunun yeraldığı kısma dinamik olarak gelecek olan bizim kodumuzu çift süslü parantez içinde yazıyoruz. Yani ->  image src="http://openweathermap.org/img/wn/{{icon}}@2x.png"


weatherapp/templates/weatherapp/index.html
```html
...
<body>
    <h1>Weather App</h1>

    {{city}} <br>
    {{temp}} <br>
    <img src="http://openweathermap.org/img/wn/{{icon}}@2x.png" alt=""> <br>
    {{desc}} <br>

</body>
```

- test ettik, çalıştı.

##### units parametresi ile gelen verinin cinsini (fahrenhight/celcius) değiştirme

- temp verisi calvin olarak geliyor biz bunu celcius a çevirelim. Bunun için dokümandan bakıyoruz ve units parametresini kullanıyoruz.
- Parametreleri ampersant işareti ile ekliyoruz. İstek attığımız url in sonuna yani views.py daki url in sonuna &units=metric  ekliyoruz ve tekrar istek atınca celcius derece olarak geldiğini gördük.

weatherapp/views.py
```py
...

def index(request):
    ...
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    ...
```


##### static city_name parametresini dinamik olarak belirleme;

- Şimdiye kadar city name lerini static olarak belirttik ancak biz bu city name ini kullanıcıdan dinamik olarak almak istiyoruz. 
- Bize bir input alanı lazım. 
- Bir form da oluşturabiliriz ama hemen basitçe template imize bir form da ekleyip kullanıcıdan city_name' i oradan da alabiliriz.

weatherapp/templates/weatherapp/index.html
```html
...
<body>
    <h1>Weather App</h1>

    <form action="" method="post">
        {% csrf_token %}
        <input type="text" name="name" placeholder="Şehir adı giriniz..">
        <input type="submit" value="add_city">
    </form>
    <br><hr>

    {{city}} <br>
    {{temp}} <br>
    <img src="http://openweathermap.org/img/wn/{{icon}}@2x.png" alt=""> <br>
    {{desc}} <br>

</body>
...
```

- views.py' a gidip, template' imizde yazdığımız formdan post ile input'tan dictionary yapısında gelen, city adını -> name'ine = 'name' vermiştik, bu değeri dictionary methodlarından get('name') methoduyla, name ile yakalayıp bir u_city değişkenine tanımlıyoruz.
  
  u_city = request.POST.get('name')
  print(u_city)

terminalden print ile bakıyoruz yakalayabimiş miyiz? Evet yakalayabiliyoruz.

- Burada bir condition kuracağız;

- if condition ımızı yazıyoruz; eğer kullanıcı bir city verisi girmişse istek attığı url de kullanıcının ismini girdiği city ile istek atsın bize response dönecek mi acaba diye de terminalden kontrolünü yapıyoruz. response.ok true olarak dönerse istek attığımız yerden response almışız demektir. 
   response = requests.get(url)
   print(response.ok)

weatherapp/views.py
```py
...

def index(request):
    
    API_KEY = config('API_KEY')
    city = 'Yozgat'

    u_city = request.POST.get('name')
    
    # eğer kullanıcı şehir ismi girdiyse;
    if u_city:
            url = f'https://api.openweathermap.org/data/2.5/weather?q={u_city}&appid={API_KEY}&units=metric'
            response = requests.get(url)
            print(response.ok)
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    content = response.json()
        
    context = {
        'city': content['name'],
        'temp': content['main']['temp'],
        'icon': content['weather'][0]['icon'],
        'desc': content['weather'][0]['description'],
    }
    
    return render(request, 'weatherapp/index.html', context)

```
- test ediyoruz, Evet terminalde True gördük. template'ten user olarak "adana" girdik, evet adana diye bir şehir varmış, response.ok bize True döndü.
- Olmayan bir şehir yazalım, evet False döndü.

- Kullanıcıdan city olmayan bir veri geldiği zaman yapılan istek False dönüyor. 
- Buna göre yeni bir condition daha yazıyoruz, Yani response.ok'ye göre yeni bir condition daha yazıyoruz;
- response.ok -> True ise de yine bir condition daha yazacağız.(eğer şehir db'de varsa, zaten var diyip göstereceğiz, eğer yoksa create edip göstereceğiz.)
  
    if response.ok:
        pass
    else:
        pass

    eğer böyle bir şehir varsa bunu yap yoksa şunu yap! 

##### messages

- ikinci kısım olan (else) response.ok değil ise, eğer böyle bir şehir yoksa kısımında bir mesaj yazdıracağız. django.contrib den messages ı import edip,
  
      if response.ok:
        pass
    else:
        messages.warning(request, 'There is no city')

yazdırıyoruz.

- messages ları kullanabilmemiz için template imize h1 tag ının altıda yahut istediğimiz bir yere ekliyoruz.

<views.py> ->

```py
...
from django.contrib import messages

def index(request):
    
    ...    
    
    if u_city:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={u_city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        # print(response.ok)
        
        if response.ok:
            pass
        else:
            messages.warning(request, 'There is no city')
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    content = response.json()
    
    ...

```


weatherapp/templates/weatherapp/index.html

```html
...
<body>
    <h1>Weather App</h1>

    {% if messages %}
    {% for message in messages %}
        <div class='message'>{{message}}</div>
    {% endfor %}
    {% endif  %}
    <hr><br>

...

```
- test ettik, olmayan bir şehir yazdık, messages'ı gördük.


- ilk kısım condition'ımız olan; "eğer böyle bir şehir varsa", API varsa veri dönüyorsa kısmında yine bir condition yazacağız;
  - Burada bir tablo oluşturacağız, 
    - eğer girilen şehir tablomuzda var ise tablodan şehri çekip, bu şehrin verilerini yansıtacağız,
    - eğer girilen şehir tablomuzda yoksa, önce o şehri tablomuzda create edeceğiz, ardından o şehir ile istek atıp, verilerini göstereceğiz.


- Burada bir es verip, db imize gidip şehirlerimizi kaydetmek için modelimizi/tablomuzu oluşturacağız;

- weatherapp/models.py a gidip; modelimizi oluşturuyoruz; models.Model den City isminde bir tablo/model oluşturuyoruz. Sadece city lerin ismini tutan bir tablo oluşturuyoruz.
  
weatherapp/models.py
```py
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
```

weatherapp/admin.py
```py
from django.contrib import admin
from .models import City

# Register your models here.
admin.site.register(City)
```


```bash
- py manage.py makemigrations
- py manage.py migrate
```

- Artık db'de şehir isimlerinin tutulduğu bir tablomuz/modelimiz var.
- Amacımız şu:
  - Bir condition ile;
  
  - Kullanıcının girmiş olduğu şehir name'ini önce db'mize kaydetmek,

  - Eğer response.ok ise, yani kullanıcı doğru bir name ismi girmiş ise;

  - Eğer kullanıcının girmiş olduğu şehir name'i db'mizde var ise, mesaj göster -> "Bu şehir var." 

  - Eğer Yoksa kullanıcının girmiş olduğu şehir name'i db'mizde yok ise, şehir name'ini db'deki City tablomuza/modelimize kaydet!

  - Eğer Yoksa, yani response.ok değil ise, kullanıcının girmiş olduğu şehir name'inde bir şehir yoksa mesaj ver -> "Böyle bir şehir yoktur."


###### Kullanıcıdan şehir isimlerini alıp, db'ye kaydetme;

- Bundan sonra, kullanıcının girdiği şehir name'leri db'ye kaydedilecek, 
- Ardından db'deki tüm şehirler için bir for döngüsü ile API isteği atılacak.
- liste şeklinde bir city_data değişkeni oluşturup, City tablosundaki her şehir için API isteği atılıp, dönen her şehir datasıyla birlikte city_data listesine eklenip template'e gönderilecek,
- Template'de gelen şehirler yine bir for döngüsüyle card componentler ile sergilenecek.

   
- views.py da oluşturduğumuz tabloyu çağırıyoruz,
     from .models import City

- Eğer kullanıcı şehir name'i girdiyse;
     if u_city:
          ...

  - Eğer response.ok ise, yani API'dan veri dönüyorsa,
        if response.ok:

  - response.json()  ile API kaynağından gelen veriyi dictionary yapısına çevirip, content değişkenine tanımlıyoruz,
        content = response.json()
  - r_city = content['name']  Bu content içerisinden city ismini alıp r_city değişkenine tanımlıyoruz.
        r_city = content['name']

  - Arkasından bu name i if condition ile kontrol ediyoruz, 
    - eğer City tablomuzda name'i r_city ile aynı olan bir obje var ise bir message gösteriyoruz 'city already exist' şehir zaten var.
        if City.objects.filter(name=r_city):
            messages.warning(request, 'City already exist!')

    - ancak yoksa City tablomuza create ediyoruz.
        else:
            City.objects.create(name=r_city)

- Özet: 
  - Eğer response ok ise yani böyle bir veri geliyorsa, o verinin içerisinden name i al bir değişkene ata, 
  - o değişken ile db yi kontrol et. 
  - Eğer db de böyle bir city name varsa mesaj döndür, böyle bir city zaten var de. 
  - Eğer db de böyle bir city name yoksa db ye bu şehri ekle.

- Test ediyoruz, db yi açıp City tablomuza bakıyoruz veri yok. 
  - Template imizden veri girişi yapıyoruz. Evet Sinop'u db ye kaydetti.
  - Aynı şehri (sinop) tekrar kaydetmeye çalışınca condition gereği bu sefer hata mesajını (City already exist!) döndürüyor.
  - veya alakasız bir şehir ismi giridiğimizde de (sndaajk) condition gereği bu sefer de (There is no city) hata mesajını döndürüyor.


weatherapp/views.py

```py
...
from .models import City

def index(request):
    
    API_KEY = config('API_KEY')
    city = 'Yozgat'

    u_city = request.POST.get('name')

    # eğer kullanıcı şehir ismi girdiyse;
    if u_city:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={u_city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        # print(response.ok)
        
        if response.ok:
            content = response.json()
            r_city = content['name']
            if City.objects.filter(name=r_city):
                messages.warning(request, 'City already exists!')
            else:
                City.objects.create(name=r_city)
        else:
            messages.warning(request, 'There is no city')
   
    ...
    
```


- Şimdi city name'ini dinamik olarak kullanıcıdan alabiliyoruz. Ve bunu çeşitli algoritmalardan geçirip response umuzu dönüyoruz. 
- Eğer API mizde öyle bir city yoksa mesajla bunu kullanıcıya bildiriyoruz. 
- Böyle bir city varsa bu sefer kendi db mizi kontrol ediyoruz, db mizde varsa yine kullanıcıya bu city name zaten var diye mesajla bildiriyoruz, 
- db mizde yoksa city nam i db mize create ediyoruz.


###### DB'deki şehir isimleriyle API kaynağından veri çekme;

- Bu aşamadan sonra db mizdeki city lerin hava durumlarını çekip template'imizde yansıtalım. 
- db imizdeki şehirleri çekelim ve   o şehirler üzerinden isteklerimizi atalım.
- cities isimli bir değişken oluşturup City.objects.all() ile db mizdeki City tablomuzdaki tüm city leri değişkenimize tanımladık. 
    cities = City.objects.all()

- Bu bize bir queryset dönüyor ve biz bir queryset'i bir for döngüsüne sokabiliyoruz.

- for döngüsü ile; 
    cities queryset'inden her bir city objesini çekiyoruz, ve her bir city objesi ile API kaynağına isteğimizi atıyoruz.

weatherapp/views.py

```py
...
cities = City.objects.all()
for city in cities:
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    content = response.json()
...
```

- Burada ne yaptık? 
  - for döngüsü ile her bir city için tekrardan istek atmış olduk. 
  - Tek bir istekte birden fazla city i çekemiyoruz, bize öyle bir imkan sunmuyor. 
  - O yüzden db deki city leri çektik, değişkene atadık, for döngüsü ile her bir city için isteği atıyoruz ve gelen datayı yakalıyoruz.
- her bir city için isteğimizi attık, gelen veriyi json() ile dictionary ye çevirdik ve content e attık. 
- Bu content ten her bir city için name, temp, icon ve desc çektik ve data değişkenine attık.


- Şimdi bu data değişkenini bir liste ye atmamız lazım. Çünkü bu data her bir for  döngüsünde değişecek, her bir city değişkeninde bu data değişecek. 
- O yüzden boş bir liste şeklinde city_data diye değişken tanımlayıp her döngüde append() methoduyla her bir döngüde değişecek olan data değişkenindeki data yı ekleyelim.
        city_data = []
        ...
        city_data.append()

- city_data değişkenini de context içerisinde template imize gönderiyoruz.


weatherapp/views.py

```py
from django.shortcuts import render
from decouple import config
import requests
from pprint import pprint
from django.contrib import messages
from .models import City

def index(request):
    
    API_KEY = config('API_KEY')
    city = 'Yozgat'
    
    u_city = request.POST.get('name')

    # eğer kullanıcı şehir ismi girdiyse;
    if u_city:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={u_city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        # print(response.ok)
        
        if response.ok:
            content = response.json()
            r_city = content['name']
            if City.objects.filter(name=r_city):
                messages.warning(request, 'City already exists!')
            else:
                City.objects.create(name=r_city)
        else:
            messages.warning(request, 'There is no city')
    
    city_data = []
    # cities = City.objects.all().order_by('-name')
    cities = City.objects.all().order_by('-id')
    for city in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        content = response.json()
        data = {
            'city': content['name'],
            'temp': content['main']['temp'],
            'icon': content['weather'][0]['icon'],
            'desc': content['weather'][0]['description'],
        }
        city_data.append(data)
    

    context = {
        'city_data': city_data,
    }
    
    return render(request, 'weatherapp/index.html', context)
```


- city_data mız bir liste olduğu için template'imizde bir for döngüsüyle dönebiliriz;

- temp data sının yanına "&#8451" kodu ile de "C-santigrad derece işareti koyabiliriz." 

weatherapp/templates/weatherapp/index.html

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WeatherApp</title>
</head>
<body>
    <h1>Weather App</h1>

    {% if messages %}
        {% for message in messages %}
            <div class='message'>{{message}}</div>
        {% endfor %}
    {% endif  %}
    <hr>
    <br>

    <form action="" method="post">
        {% csrf_token %}
        <input type="text" name="name" id="">
        <input type="submit" value="add_city">
    </form>
    <br><hr>

    {% for i in city_data %}
    
    {{i.city}} <br>
    {{i.temp}} &#8451<br>
    <img src="http://openweathermap.org/img/wn/{{i.icon}}@2x.png" alt=""> <br>
    {{i.desc}} <br><hr> 

    {% endfor %}
        
</body>
</html>
```

##### statics ekleme
###### timeout.js

- messages larımızın ekrandan silinmesi için javascripts imizi ekleyebiliriz.

- static lerimizin çalışması için template imizin en başına {% load static %}  ekliyoruz,

- weatherapp imizin içerisine static/weatherapp/js klasör yapısı ve çerisine timeout.js dosyamızı ekliyoruz.
- daha sonra javascripts leri eklediğimiz gibi template imizin body sinin en altına ekliyoruz.
    <script src="{% static 'weatherapp/js/timeout.js' %}"></script>


weatherapp/static/weatherapp/js/timeout.js
```js
let element = document.querySelector('.message');

setTimeout(function () {
    element.style.display = 'none';
}, 3000);
```


weatherapp/templates/weatherapp/index.html
        
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WeatherApp</title>
</head>
<body>
    <h1>Weather App</h1>

    {% if messages %}
        {% for message in messages %}
            <div class='message'>{{message}}</div>
        {% endfor %}
    {% endif  %}
    <hr>
    <br>

    <form action="" method="post">
        {% csrf_token %}
        <input type="text" name="name" id="">
        <input type="submit" value="add_city">
    </form>
    <br><hr>

    {% for i in city_data reversed %}
    
    {{i.city}} <br>
    {{i.temp}} &#8451<br>
    <img src="http://openweathermap.org/img/wn/{{i.icon}}@2x.png" alt=""> <br>
    {{i.desc}} <br>
    <hr>

    {% endfor %}
    
    <script src="{% static 'weatherapp/js/timeout.js' %}"></script>

</body>
</html>
```


##### delete

- delete ekleyeceğiz; yani eklediğimiz şehirleri çıkaracağız.
- delete view i yazıyoruz. Burada specific bir obje ile işlem yapacağımız için request ile birlikte id yi de parametre olarak gönderiyoruz.

    def delete(request, id):
       city = City.objects.get(id=id)

   normalde şu ana kadar böyle yapmıştık ama daha kullanışlı ve yaygın versiyonu şöyle ->

   django.shortcuts dan get_object_or_404 import ediyoruz;
   
    from django.shortcuts import get_object_or_404
    
    def delete(request, id):
       city = get_object_or_404(City, id=id)

   https://docs.djangoproject.com/en/4.2/topics/http/shortcuts/


- eğer öyle bir obje yoksa model in DoesNotExist hatası yerine Http404 hatası döndürüyor. Bu daha anlamlı bir response. Bunun için try-except yapısını kullanıyorduk. Ancak bu yapı daha kullanışlı. İçerisine bir queryset de alabilir ama genelde bir model alır. Kullanıcıya hatayı daha yumuşak döndürmeye yarayan bir yapı.

- city'i sil!
  city.delete()

- bir messaj da verelim;
  messages.warning(request, 'City deleted.')

- Son olarak bizi home page e redirect etsin;

  from django.shortcuts import redirect

  return redirect('home')


weatherapp/views.py

```py
from django.shortcuts import render, get_object_or_404, redirect
...

...

def delete_city(request, id):
    # city = City.objects.get(id=id)
    city = get_object_or_404(City, id=id)
    city.delete()
    messages.warning(request, 'City deleted.')
    return redirect('home')
```


- delete_city view imizi yazdık. şimdi onu tetikleyecek urls'ini/endpoint'ini yazalım.

weatherapp/urls.py
```py
from django.urls import path
from .views import index, delete_city

urlpatterns = [
    path('', index, name='home' ),
    path('delete/<int:id>', delete_city, name='delete' ),
]
```


###### delete için id yakalama;

- tek bir işlemimiz kaldı. 

- Biz delete view i için bir template belirlemedik, home template ine redirect ettik. 

- Şimdi home yani index.html template inde delete url ini tetikleyecek bir button oluşturacağız. Bu button her bir city'ye ait olacağı için, bunu for döngüsü içerisine ekliyoruz.
 
- card ın içinde bir delete butonu koyduk, url inide id olarak yazdık ama, bize db den city_data ile bir dictionary verisi geliyor, bir object değil. Biz dictionary verisi çektiğimiz için orada da id verisi yok.

- pprint(city_data)  ile .json() tipinde gelen veriye terminalde bakıyoruz; bir liste içerisinde, dictionary şeklinde geldiğini görüyoruz.
    
    [{'city': 'Erzurum Province', 'desc': 'clear sky', 'icon': '01n', 'temp': 7.82},
    {'city': 'Iğdır', 'desc': 'clear sky', 'icon': '01n', 'temp': 18.96},
    {'city': 'Mersin Province', 'desc': 'clear sky', 'icon': '01n', 'temp': 25.28},
    {'city': 'Moscow', 'desc': 'clear sky', 'icon': '01n', 'temp': 8.59},]

- Bu id verisine erişebilmek için;
  - 1. yol -> views de, data değişkenine  'city': content['name'] şeklinde dictionary olarak almak yerine yerine,
    -   for döngüsünde cities'lerin içinden aldığımız city objesini, 'city': city   şeklinde obje olarak da alabiliriz.
    -   böylelikle objenin id'sine erişebiliriz.
    -   template'te de str methodunda name'i ile görüneceğinden yine city name'i görünür, bir değişiklik olmaz.
  
  - 2. yol -> view de data değişkenine 'id': city.id  de ekleyebilirdik.


- 1. Yol -> views de data değişkenine dictionary şeklindeki 'city': content['name']  yerine, object şeklinde 'city': city   objesini gönderebiliriz.
- Bu projede 1. Yol kullanıldı.

weatherapp/views.py
```py
...

def index(request):
    ...
    
    city_data = []     
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
        }
        city_data.append(data)
        # 1. yol;
        # print(city.id)
        # print(city.id)

    
    # pprint(city_data)

    context = {
        'city_data': city_data,
    }
    
    return render(request, 'weatherapp/index.html', context)

def delete_city(request, id):
    city = get_object_or_404(City, id=id)
    city.delete()
    messages.warning(request, 'City deleted.')
    return redirect('home')
```


weatherapp/templates/weatherapp/index.html
```html
...

{% for i in city_data %}

    {{i.city}} <br>
    {{i.temp}} &#8451<br>
    <img src="http://openweathermap.org/img/wn/{{i.icon}}@2x.png" alt=""> <br>
    {{i.desc}} <br>
    
    <button><a href="{% url 'delete' i.city.id %}">Delete</a></button>

    <br>
    <hr>

{% endfor %}

...

```


- 2. yol -> view de data değişkenine 'id': city.id  de ekleyebilirdik. for'daki city objesinin id'sini ekleyebiliriz.

weatherapp/views.py
```py
...

def index(request):
    ...
    
    city_data = []     
    cities = City.objects.all().order_by('-id')
    for city in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang=tr&appid={API_KEY}&units=metric' # &lang=tr ile türkçe yapılıyor.
        response = requests.get(url)
        content = response.json()
        data = {
            'city': content['name'],
            'temp': content['main']['temp'],
            'icon': content['weather'][0]['icon'],
            'desc': content['weather'][0]['description'],
            'id': city.id, # 2. yol for'daki city objesi'nin id'si
        }
        city_data.append(data)
    
    # pprint(city_data)

    context = {
        'city_data': city_data,
    }
    
    return render(request, 'weatherapp/index.html', context)

def delete_city(request, id):
    city = get_object_or_404(City, id=id)
    city.delete()
    messages.warning(request, 'City deleted.')
    return redirect('home')
```


weatherapp/templates/weatherapp/index.html
```html
...

{% for i in city_data %}

    {{i.city}} <br>
    {{i.temp}} &#8451<br>
    <img src="http://openweathermap.org/img/wn/{{i.icon}}@2x.png" alt=""> <br>
    {{i.desc}} <br>
    
        <button><a href="{% url 'delete' i.id %}">Delete</a></button>

    <br>
    <hr>

{% endfor %}

...

```


##### add bootstrap V5.2

- bootstrap V5.2 ile güzelleştirilmiş hali

weatherapp/templates/weatherapp/index.html
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Umit WeatherApp</title>

    <!-- CSS only -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">

</head>

<body class="bg-dark p-2 text-dark bg-opacity-75">

<div class="container py-2 ">
    <h1 class="text-white">Weather App</h1>

    <div class="messages">
        {% if messages %}
            {% for message in messages %}
            <p class="message text-center alert alert-{{ message.tags }}">
                {% if message.level == messages.ERROR %}Important: {% endif %}
                {{ message }}
            </p>
            {% endfor %}
        {% endif %}
    </div>
    
    <form action="" method="post">
        {% csrf_token %}
        <div class="input-group mb-3">
            <input type="text" class="form-control" placeholder="Şehir adı giriniz.." aria-label="Recipient's username" aria-describedby="button-addon2" name="name">
            <button class="btn btn-outline-secondary bg-info text-white" type="submit" id="button-addon2">Add City</button>
          </div>
    </form>
    
</div>
<div class="container py-2 ">
    <div class="row row-cols-4 row-cols-md-3 g-4">
        {% for i in city_data reversed %}
            <div class="col-sm-4 ">
                <div class="card card text-center rounded-4">
                    <div class="card-body p-6 ">
                        {{i.city}} <br>
                        {{i.temp}}&#8451<br>
                        <img src="http://openweathermap.org/img/wn/{{i.icon}}@2x.png" alt=""> <br>
                        {{i.desc}} <br>
                        <button><a href="{% url 'delete' i.city.id %}">Delete</a></button>
                        {% comment %}<button><a href="{% url 'delete' i.id %}">Delete</a></button>{% endcomment %}
                    </div>
                </div>
            </div>
        {% endfor %}
    </div>
</div>

<!-- JavaScript Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>

<script src="{% static 'weatherapp/js/timeout.js' %}"></script>

</body>
</html>

```


### Authentication-2_V.01

- authentication app'imiz (users) kuralım;

```bash
- py manage.py startapp users
```

- users app'imizi INSTALLED_APPS'e ekleyelim

settings.py
```py
  INSTALLED_APPS = [
    ...
    # myApps
    'myapp',
    'users',
]
```

- urls configurasyonu;

weather/urls.py
```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weatherapp.urls')),
    path('users/', include('users.urls')),
]
```

- users app'imiz için urls.py dosyası oluşturuyoruz.

users/urls.py
```py
from django.urls import path

app_name = 'users'
urlpatterns = [

] 
```

- ÖNEMLİ: 
  - users app'imizin urls.py'ında namespace kullandığımız için diğer app'imiz olan weatherapp için de urls.py da namespace kullanmamız gerekiyor.
  - ayrıca weatherapp'in url'lerinin tetiklendiği her linke gidip weatherapp:link şeklinde upgrade ediyoruz.
  - views.py'da da redirect ettiğimiz url varsa ona da weatherapp:url şeklinde updrade ediyoruz. 

weatherapp/urls.py
```py
...

app_name = 'weatherapp'
urlpatterns = [
    ...
] 
```

weatherapp/templates/weatherapp/index.html
```html
...
<button><a href="{% url 'weatherapp:delete' i.city.id %}">Delete</a></button>
...
```

weatherapp/views.py
```py
...
return redirect('weatherapp:home')
```

##### home view-urls-template (weatherapp);

- şimdi weatherapp app'imizin index.html olarak bir home template'i var.

#### navbar.html - base.html - home.html
#### bootstrap5 
#### static_files

- Best practice 
  - navbar.html, 
  - base.htm
  - home.html
oluşturalım.
- Booststrap5 ile de style verelim.
- Navbarda logo kullanalım. Bunun için static folder oluşturalım, statics ayarlarını yapalım.

weatherapp/templates/weatherapp/navbar.html
```html
{% load static %}
<nav class="navbar navbar-expand-lg navbar-dark bg-dark navbar fixed-top">

    <a class="navbar-brand ms-3" href="{% url 'weatherapp:home' %}">
        <img src="{% static 'users/images/cw_logo.jpg' %}" alt="CLARUSWAY_LOGO" /> Umit Developer</a>
    
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
    </button>

    <div class="container-fluid">

        <div class="collapse navbar-collapse">
        
            <ul class="navbar-nav me-auto">

                {% if request.user.is_superuser %}
        
                <li class="nav-item">
                    <a class="nav-link" href="/admin" target="_blank">Admin Panel</a>
                </li>
                
                {% endif %}        

                <li class="nav-item">
                    <a class="nav-link" href="#">Students</a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="#">Contact</a>
                </li>

            </ul>

            <ul class="navbar-nav ms-auto">
                {% if request.user.is_authenticated %} 

                <li class="nav-item">
                    <a class="nav-link" href="#">{{ user.username }}</a>
                </li>
        
                <li class="nav-item">
                    {% comment %} {% url 'users:logout' %} {% endcomment %}
                    <a class="nav-link" href="{% url 'users:logout' %}">Logout</a>
                </li>

                {% else %}
                
                <li class="nav-item">
                    {% comment %} {% url 'users:login' %} {% endcomment %}
                    <a class="nav-link" href="#">Login</a>
                </li>
                <li class="nav-item">
                    {% comment %} {% url 'users:register' %} {% endcomment %}
                    <a class="nav-link" href="{% url 'users:register' %}">Register</a>
                </li>
                {% endif %}
            </ul>
        </div>
    </div>
</nav>
```

weatherapp/templates/weatherapp/base.html
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Umit WeatherApp</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    
    
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
    
    <link rel="stylesheet" href="{% static 'weatherapp/css/stylee.css' %}">
    
</head>
<body class="full-page pt-5;">


    {% include "weatherapp/navbar.html" %}
    
        <div class="container">
            {% block content %}
        
            {% endblock content %}
        </div>
    </div>


<!-- JavaScript Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>

<script src="{% static 'weatherapp/js/timeout.js' %}"></script>

</body>
</html>
```


weatherapp/templates/weatherapp/index.html
```html
{% extends 'weatherapp/base.html' %}

{% block content %}

{% if request.user.is_authenticated %}
    
<div class="container py-2 ">
    <h1 class="text-white">Weather App</h1>

    <div class="messages">
        {% if messages %}
            {% for message in messages %}
            <p class="message text-center alert alert-{{ message.tags }}">
                {% if message.level == messages.ERROR %}Important: {% endif %}
                {{ message }}
            </p>
            {% endfor %}
        {% endif %}
    </div>
    
    <form action="" method="post">
        {% csrf_token %}
        <div class="input-group mb-3">
            <input type="text" class="form-control" placeholder="Şehir adı giriniz.." aria-label="Recipient's username" aria-describedby="button-addon2" name="name">
            <button class="btn btn-outline-secondary bg-info text-white" type="submit" id="button-addon2">Add City</button>
          </div>
    </form>
    
</div>
<div class="container py-2 ">
    <div class="row row-cols-4 row-cols-md-3 g-4">
        {% comment %} {% for i in city_data reversed %} {% endcomment %}
        {% for i in city_data %}
            <div class="col-sm-4 ">
                <div class="card card text-center rounded-4">
                    <div class="card-body p-6 ">
                        {{i.city}} <br>
                        {{i.temp}}&#8451<br>
                        <img src="http://openweathermap.org/img/wn/{{i.icon}}@2x.png" alt=""> <br>
                        {{i.desc}} <br>
                        <button><a href="{% url 'weatherapp:delete' i.city.id %}">Delete</a></button>
                        {% comment %}<button><a href="{% url 'delete' i.id %}">Delete</a></button>{% endcomment %}
                    </div>
                </div>
            </div>
        {% endfor %}
    </div>
</div>

{% else %}

<div class="container py-2 pt-5 text-center">
    <h1>Wellcome <span class="text-danger">Guest!</span>  Please login app.</h1>
</div>

{% endif %} 

{% endblock content %}
```


##### statics

- users app'inde static files' lar kullanacağız. Mesela logo, picture, image, css, js file gibi. Bunlar için şu klasör yapısını kullanacağız;
- user app'inin altında şu klasör yapısını oluşturuyoruz; 
    users/static/users

- bu klasör yapısı altında oluşturduğumuz images, css, js klasörlerinin içinde files'larımızı baındıracağız.
    users/static/users/images
                   .../css
                   .../js


- logo resmini kopyalayıp images klasörüne yapıştırıyoruz.

- Ayrıca template'lerimizde {% load static %} tag'ını da kullanmayı unutmuyoruz.


#### Authentication-2_V.01 Buradan itibaren;

-  Authentication için kullanacağımız user için djangonun default User modelinden yaralanacağız.
-  Fakat default User modelinde bulunmayan ekstra fieldlar da olsun istiyoruz.
- Ekstra istenen fieldlar için bir model/tablo oluşturup ve bu default User model/table ile ilişki kuracağız. users app'imizde models.py'a giderek;
 ile OneToOneField ilişki kurmak.)
     ![](OneToOneField.png)

users/model.py
```py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
```

- modelimizde image field kullandığımız için Pillow paketini kurmamız gerekiyor.

```bash
- python -m pip install Pillow
# - pip install pillow
- pip freeze > requirements.txt
- py manage.py makemigrations
- py manage.py migrate
- py manage.py runserver
```

- modelimizde image field ile profile picture için de bir media klasörü oluşturacağımız için media ayarlarını da yapıyoruz.

- admin panelinde modelimizi görmek için admin.py da modelimizi import edip register ediyoruz. 

users/admin.py
```py
...
from .models import UserProfile

admin.site.register(UserProfile)
```

- admin panelimizde user profile modelimizi görüyoruz.


###### media

- Projede media file'ları (profil resimleri) için proje klasörü ile aynı seviyede;
   /media/profile_pics 
klasör yapısını oluşturuyoruz. (Yada oluşturmuyoruz. Zaten settings.py'da media için klasör belirteceğimiz için kendisi otomatik oluşturacak.)

- Ayrıca settings.py'da ve urls.py'da şu ayarları yapıyouz;

settings.py
```py
# Media dosyaları için ayarlar
MEDIA_URL = '/media/'  # Tarayıcıdan erişim için URL
MEDIA_ROOT = BASE_DIR / 'media'  # Yüklenen dosyaların depolanacağı yer
```


main/urls.py
```py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Diğer URL patternleri
]

if settings.DEBUG:  # Yalnızca development modda çalışacak
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- admin panelimizden bir user profile objesi create ediyoruz.
- media ayarları sayesinde profile picture'ın da görüntülendiğini görüyoruz.


- Admin panelden giriş yaptığımızda, giriş yapmış olan user'ı home page'de de giriş yapmış olarak kabul ediyor.
- weatherapp'de home page'de, base.html'den extend ettiğimiz, oraya da navbar.html'den include ettiğimiz Log Out linkinin kullandığı fonksiyonu, users app'imizde (views-urls) aktif hale getirip, home page den logout yapalım. 


##### logout

- navbar.html'de bulunan Logout linkini aktif hale getireceğiz;
- users app'imizde views.py a gidiyoruz, logout için bir view yazıyoruz. 
- logout() django tarafından bize hazır verilen bir yapı. 
- Bunun için django.contrib.auth dan logout ı import ediyoruz;
- logout ettikten sonra da nereye döndürsün onu belirtiyoruz (redirect'i de import ediyoruz.);

  from django.shortcuts import render, redirect
  from django.contrib.auth import logout
  
  def user_logout(request):
    logout(request)
    return redirect('weatherapp:home')

users/views.py

```py
from django.shortcuts import render, redirect
from django.contrib.auth import logout


def user_logout(request):
    logout(request)
    return redirect('weatherapp:home')
```

- logout view imizi yazdıktan sonra onu tetikleyecek url imizi de urls.py da yazıyoruz;

users/urls.py
```py
from django.urls import path
from .views import user_logout

app_name = 'users'
urlpatterns = [
    path('logout/', user_logout, name='logout'),
]
```

- logout için bir link vermemiz gerekiyor, bu link de zaten weatherapp app'imizdeki navbarda mevcut, yorumdaki bu linki veriyoruz ve aktif hale getiriyoruz. 

myapp/templates/myapp/navbar.html
```html
    <li class="nav-item">
        <a class="nav-link" href="{% url 'users:logout' %}">Logout</a>
    </li>
```

- Test ediyoruz, çalıştı.

##### register

- register işlemi yapacağız;
- djangonun bize sağlamadığı tekşey registration. registration view ini biz kendimiz yazacağız.
- register için kullanıcıya bir form gönderip doldurmasını ve formla gelen bilgileri kaydetmemiz gerekiyor.
- Normalde bizim default olarak User ımız ve ekstra fieldlarımızın olduğu UserProfile modelimiz vardı. İkisini de kullanmamız lazım.

- User için bir form, UserProfile için ikinci bir form kullanmamız lazım.

- 1.

- users app'imizin içinde forms.py create ediyoruz, 
- Madem form oluşturacağım, djangodan fromları da istememiz lazım.
  from django import forms

- ilk olarak djangonun admin panelde default olarak kullandığı modeli User modelini import ediyoruz;
  from django.contrib.auth.models import User

- Bir de bizim ekstra fieldlar için oluşturduğumuz UserProfile modeli, onu da import ediyoruz.
  from .models import UserProfile

- Formumuzu oluşturmaya başlıyoruz, djangonun default modelinden yani User modelinden oluşturduğumuz formlar için UserCreationForm'dan inherit ederek kullanıyoruz, tabi bunun için de import etmemiz lazım,
  from django.contrib.auth.forms import UserCreationForm

-  UserForm diye UserCreationForm dan formumuzu yazmaya başlıyoruz, hangi modelden alacak? User modelinden, hazır formlarda class Meta tanımlayıp, modelin ismini veriyorsunuz, bu kadar.
  
  class UserForm(UserCreationForm):
    class Meta():
      model = User

- Sonra fieldları vereceğiz, o modeldeki tüm fieldları almak zorundan değiliz, hangilerini istiyorsak onları belirtiyoruz; (password işini django kendisi hallediyor, biz birşey yapmıyoruz.)
   model = User
   fields = ('username', 'email')

- 2.

- Yukarıdaki UserForm, default olarak djangonun User modelinden elde ettiğimiz form, şimdi kendi yazdığımız ekstra fieldların olduğu modelden oluşturacağımız form var, ona da UserProfileForm diyoruz ve onu forms.ModelForm dan oluşturuyoruz,
- class Meta tanımlayıp modelimizin ismi ve hangi field ları kullanacağımızı belirtiyoruz. 
- Burada exclude = ('user') kullanıyoruz. Yani user haricindeki tüm fieldlar demektir. 
- Neden user haricinde? çünkü user ı burada manuel olarak kullanmamam gerekir. Çünkü bire bir ilişkili diğer tabloda user var ve onu kullanacak.
- hariç tuttuğumuz user field'ını view'de ekleyeceğiz.

  class UserProfileForm(forms.ModelForm):
    class Meta:
      model = UserProfile
      # fields = '__all__'
      exclude = ('user',)

users/forms.py
```py
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username', 'email')

class UserProfileForm(forms.ModelForm):
    class Meta:
      model = UserProfile
      # fields = '__all__'
      exclude = ('user',)
```

- Formlarımızı yazdık, şimdi bu haliyle ekrana formlarımız gönderiyoruz; onun için view imize gidiyoruz, 

- register view imizi oluşturup formlarımızı çekip bir context e koyup template e göndereceğiz;

users/views.py
```py
from .forms import UserForm, UserProfileForm 

...

def register(request):
    form_user = UserForm()
    form_profile = UserProfileForm()
    context = {
        'form_user': form_user,
        'form_profile': form_profile,
    }
    return render(request, 'users/register.html', context)
```


- url ini yazıyoruz;

users/urls.py

```py
from .views import (
    ...,
    register,
)

urlpatterns = [
    ...,
    path('register/', register, name='register'),
    
]
```

- şimdi sıra geldi register template'ini yazmaya;
- users app'imizin templates leri için; 
    users/templates/users/register.html
klasör yapısını oluşturuyoruz.
- register template'imizde kullanacağımız formlar düzgün görünsün diye de crispy paketini yükleyeceğiz.

- users app'imizde kullanacağımız templates'leri oluşturalım;
- register.html

users/templates/users/register.html
```html
{% extends 'weatherapp/base.html' %} 
{% block content %} 
{% load crispy_forms_tags %}

<h2>Registration Form</h2>

{% if request.user.is_authenticated %}

<h3>Thanks for registering</h3>

{% else %}

<h3>Fill out the form please!</h3>
    <form action="" method="post" enctype="multipart/form-data">
        {% csrf_token %} 
        {{ form_user | crispy }} 
        {{ form_profile | crispy }}
        <button type="submit" class="btn btn-danger">Register</button>
    </form>
{% endif %} 
{% endblock content %}
```

- weatherapp'deki navbar template imize gidip register linkini açıyoruz;

myapp/templates/myapp/navbar.html
```html
      <li class="nav-item active">
        {% comment %} {% url 'register' %} {% endcomment %}
        <a class="nav-link" href="{% url 'users:register' %}">Register</a>
      </li>
```

- test ediyoruz;

- serverı mıza gelip page imize baktığımızda, register template'imizde yazdığımız condition gereği eğer zaten authenticate olmuş isek bize form göstermiyor. Logout ile çıkalım, tekrar registration ile girdiğimizde, evet iki formumuzu da alt alta görüyoruz.

- password alanlarını django kontrol ediyor.

- Şu anda sadece formları ekrana getirdik. Herhangi bir post işlemi ile gelen verileri kaydetmiyor.


- register template'imizde kullanacağımız formlar düzgün görünsün diye de crispy paketini yükleyeceğiz.


###### crispy_forms & bootstrap5

```bash
- pip install django-crispy-forms
- pip install crispy-bootstrap5
- pip freeze > requirements.txt
```

settings.py
```py
  INSTALLED_APPS = [
    ...
    # myApps
    'users',
    'myapp',
    # 3rd_party_package
    'crispy_forms',
    'crispy_bootstrap5',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"
```

- register template'imizde kullanacağımız formlar düzgün görünsün diye de crispy paketini template'te kullanalım.

users/templates/users/register.html
```html
{% extends 'weatherapp/base.html' %} 
{% block content %} 
{% load crispy_forms_tags %}

<h2 class="mt-3 text-center">Registration Form</h2>

{% if request.user.is_authenticated %}

<h3 class="mt-3 text-center">Thanks for registering.</h3>

{% else %}

<h3 class="mt-3 text-center">Fill out the form please!</h3>

<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <form action="" method="post" enctype="multipart/form-data" class="text-white mt-3 mb-5">
                {% csrf_token %}
                {{ form_user | crispy }} 
                {{ form_profile | crispy }}
                <button type="submit" class="btn btn-danger">Register</button>
            </form>
        </div>
    </div>
</div>

{% endif %} 
{% endblock content %}

```

- register form'umuz güzelleşti.

- register view ini tamamlıyoruz;
  if request.method == 'POST':

- userdan gelen formları içlerinde request ile birlikte tekrar yakalıyoruz. form_profile kısmında request.POST ile birlikte Request.FILES kullanıyoruz çünkü picture da upload edeceğiz.

  form_user = UserForm(request.POST)
  form_profile = UserProfileForm(request.POST, request.FILES)

- her iki form da valid ise; 
    if form_user.is_valid() and form_profile.is_valid():

- ikinci formu kaydederken id gerekecek, ama biz formumuzda user field ını modelimizden alırken hariç tutmuştuk. yani form_user ı save ederken kullandığı id yi, form_profile ı save ederken de kullanmamız lazım. Şöyle bir yöntem kullanıyoruz. verisi eksik olan form_profile ı hemen save() etmiyoruz, form_user kaydedilince oluşan id sini şöyle elde edebiliriz;

her iki form da valid ise 
 form_user ı save et ve bir user değişkenine tanımla,

 user = form_user.save() 

profile diye bir değişken belirleyip form_profile.save(commit=False) şeklinde tanımlıyoruz. Yani formdan gelen bilgileri kaydet ama save etmeden profile değişkenine tanımla;

  profile = form_profile.save(commit=False)

yukarıdaki user değişkenini aşağıdaki profile değişkeninin user ına tanımlayarak o sorunu çözüyoruz.
        profile.user=user
        profile.save()

- daha sonra kullanıcıyı login yapıp home page e redirect ediyoruz.; login i import ediyoruz.
  from django.contrib.auth import (
    ...
    login,
  )

  login(request, user)
  return redirect('weather:home')


users/view.py
```py
from django.contrib.auth import (
  logout, 
  login,
)
...

def register(request):
    form_user = UserForm()
    form_profile = UserProfileForm()
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_profile = UserProfileForm(request.POST, request.FILES)
        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save() 
            # form_profile.save() 
            profile = form_profile.save(commit=False)
            profile.user=user
            profile.save()
            
            login(request, user)
            
            return redirect('weather:home')
        
    context = {
        'form_user': form_user,
        'form_profile': form_profile,
    }
    return render(request, 'users/register.html', context)
```

- test ettik, çalıştı.


##### login

- geriye login işlemi kaldı;
  login işlemi için, yine bize kullanıcının doldurması için bir form lazım;

- login işlemini de djangonun default formunu kullanarak yapacağız.
- views.py'da;
- django.contrib.auth.forms dan AuthenticationForm u import ediyoruz.
       from django.contrib.auth.forms import AuthenticationForm
  
  bu formu kullanarak bir view oluşturacağız.
  def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('weatherapp:home')
    return render(request, 'users/login.html', {'form' : form})

- Kullanıcıya form'u gönder.
- Eğer request, POST ile gelirse demekki kullanıcı dolu bir form gönderiyor.
- O zaman bu dolu formu al ve if ile devam et...

users/views.py
```py
...
from django.contrib.auth.forms import AuthenticationForm

...

def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('weatherapp:home')
    return render(request, 'users/login.html', {'form': form})
```

- url ini yazıyoruz;

users/urls.py  ->
```py
from .views import (
  ... 
  user_login,
)

urlpatterns = [
    ...
    path('login/', user_login, name='login'),
    
]
```

- user_login template'ini oluşturuyoruz;

users/templates/users/login.html
```html
{% extends 'weatherapp/base.html' %} 

{% block content %} 

{% load crispy_forms_tags %}

<div class="container mt-4">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <h3 class="custom-border-radius text-center">Please Login</h3>
            <form method="post" class="text-white mt-3 mb-5">
                {% csrf_token %}
                {{ form | crispy }}
                <button type="submit" class="btn btn-danger">Login</button>
            </form>
        </div>
    </div>
</div>

{% endblock content %}
```

- navbar template imize gidip login linkini açıyoruz;

myapp/templates/myapp/navbar.html
```html
      <li class="nav-item">
        <a class="nav-link" href="{% url 'users:login' %}">Login</a>
      </li>
```


###### kullanıcı profile_picture'ını navbar'da gösterme;

- Kullanıcı profil resmini navbar.html dosyasında göstermek için, bu dosyaya kullanıcı bilgilerini geçmeniz gerekecek. 
- base.html dosyası üzerinden navbar.html'a gerekli kullanıcı bilgilerini

1. View'da Kullanıcı Bilgilerini Sağlamak
İlk olarak, kullanıcı profil bilgilerini view'da elde edip template'e geçirin. Eğer ana sayfanızda veya ilgili bir view'da kullanıcı bilgilerini geçiriyorsanız, kullanıcı profilini context'e eklemeniz gerekir.

views.py
```py
from django.shortcuts import render
from .models import UserProfile

def home(request):
    profile = None
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
    
    context = {
        'profile': profile,
    }
    
    return render(request, 'index.html', context)
```

2. base.html Dosyasına navbar.html'da Kullanıcı Bilgilerini Geçirme;
- base.html dosyanızda, navbar.html'ı include ettiğinizde kullanıcı bilgilerini de geçirmelisiniz. Bunu şu şekilde yapabilirsiniz:

base.html
```html
...

 {% include 'navbar.html' with profile=profile %}

...

```

3. navbar.html Dosyasında Profil Resmini Gösterme
navbar.html dosyasında profile değişkenini kullanarak profil resmini gösterebilirsiniz.

navbar.html
```html
{% if request.user.is_authenticated %}
                <a class="nav-link" href="{% url 'profile' %}">
                    {% if profile %}
                        <img src="{{ profile.profile_pic.url }}" alt="Profil Resmi" class="rounded-circle" style="width: 40px; height: 40px;">
                    {% else %}
                        <img src="{% static 'path/to/default/avatar.png' %}" alt="Varsayılan Profil Resmi" class="rounded-circle" style="width: 40px; height: 40px;">
                    {% endif %}
                </a>
            {% else %}
```

- Özet:
- View'da kullanıcı profil bilgilerini elde edip context'e ekleyin.
- base.html dosyanızda, navbar.html'ı include ederken kullanıcı profil bilgisini geçirin.
- navbar.html dosyanızda, kullanıcı profil resmini gösterin ve eğer profil resmi yoksa varsayılan bir resim gösterin.


- Şöyle bir sorun çıktı; profile picture'ı olmayan kullanıcı giriş yaptığında bir resim göstermiyor. else kısmına {% static 'media/avatar.png' %} yazdım. media klasöründeki avatar.png'yi göstersin dedim ama göstermedi.

- Çözüm:
- Profil resmi olmayan kullanıcılar için varsayılan bir resim göstermek için doğru static dosya yolu kullanmanız gerekiyor.

1. Varsayılan Profil Resmi Yolunu Doğru Belirleme

navbar.html
```html
...
{% if profile and profile.profile_pic %}
                        <img src="{{ profile.profile_pic.url }}" alt="Profil Resmi" class="rounded-circle" style="width: 40px; height: 40px;">
                    {% else %}
                        <img src="{% static 'users/images/avatar.png' %}" alt="Varsayılan Profil Resmi" class="rounded-circle" style="width: 40px; height: 40px;">
                    {% endif %}
...
```

2. Varsayılan Resmi Static Klasörüne Taşıma;
Varsayılan resminizi (örneğin, avatar.png) static klasörünün içine yerleştirin.

 weather (project)
   users
     static
       images
         avatar.png

- Özet:
- Profil resmi olmayan kullanıcılar için media dizinini kullanmak yerine static klasöründeki varsayılan resmi gösterin.
- Varsayılan resmi static dizinine ekleyin ve yolunu kontrol edin.
- Geliştirme sırasında statik dosyaların düzgün sunulup sunulmadığını kontrol edin.



###### form'da email'i unique yapılması

###### form'da bir field için help_text oluşturulması 

###### form'da bir field için widgets ile placeholder oluşturulması

###### modelde image field için default picture oluşturulması

###### navbar'da authenticate user'ın username'i gösterilmesi 

###### sürükleme barı oluşturulması (css'de) 


en son css, index.html, 

index.html
```html
{% extends 'weatherapp/base.html' %}

{% block content %}

{% if request.user.is_authenticated %}
    
<div class="container py-2">
    <h1 class="text-white text-center custom-border-radius">Weather App</h1>

    <div class="messages">
        {% if messages %}
            {% for message in messages %}
            <p class="message text-center alert alert-{{ message.tags }}">
                {% if message.level == messages.ERROR %}Important: {% endif %}
                {{ message }}
            </p>
            {% endfor %}
        {% endif %}
    </div>
    
    <form action="" method="post">
        {% csrf_token %}
        <div class="input-group mb-3">
            <input type="text" class="form-control bg-warning text-white border-secondary" placeholder="Şehir adı giriniz.." aria-label="Recipient's username" aria-describedby="button-addon2" name="name">
            <button class="btn btn-outline-secondary bg-info text-white" type="submit" id="button-addon2">Add City</button>
        </div>
    </form>
    
</div>
<div class="container py-2 ">
    <div class="row row-cols-4 row-cols-md-3 g-4">
        {% comment %} {% for i in city_data reversed %} {% endcomment %}
        {% for i in city_data %}
            <div class="col-sm-4 ">
                <div class="card card text-center rounded-4 custom-card">
                    <div class="card-body p-6 ">
                        {{i.city}} <br>
                        {{i.temp}}&#8451<br>
                        <img src="http://openweathermap.org/img/wn/{{i.icon}}@2x.png" alt=""> <br>
                        {{i.desc}} <br>
                        <a href="{% url 'weatherapp:delete' i.city.id %}" class="btn btn-danger btn-sm text-white text-decoration-none mt-2">Delete</a>
                    </div>
                </div>
            </div>
        {% endfor %}
    </div>
</div>

{% else %}

<div class="container py-2 pt-5 text-center">
    <h1>Wellcome <span class="text-danger">Guest!</span>  Please login app.</h1>
</div>

{% endif %} 

{% endblock content %}
```

style.css
```css
.custom-card {
    background-color: #495057; /* Daha açık bir koyu gri ton */
    color: white; /* Metin rengini beyaz yap */
}

.custom-border-radius {
    border-radius: 10px; /* İstediğiniz değer */
    /*background-color: rgba(0, 0, 0, 0.5); /* Arka plan rengi eklemek isteyebilirsiniz */
    padding: 10px; /* İç boşluk */
}
```

#### email ile giriş;

- forms.py'da EmailAuthenticationForm(AuthenticationForm) oluşturduk.
- views.py'da bu formu kullanarak user_login view'i oluşturduk.



### pythonanywhere deployment

- Projeyi github a push layın. reponun görünürlüğünü Public olarak ayarlayın. (push larken dbsqlite3'yi ve media'yı da pushluyorum. Db boş olmasın diye.)
- pythonanywhere sign up oluyoruz.
- pythonanywhere free account içinde sadece 1 app konulabiliyor. Birden çok app konulacaksa, birden fazla e-mail ile birden fazla free account oluşturulup ve herbir free account a 1 app konulabilir.
- pythonanywhere default olarak olarak sql3 db sunuyor. free account ta postgresql için para ödemek gerekiyor.
  
- repoda bir değişiklik olduğunda deploy edilmiş app a değişiklikler otomatik yansımıyor. (pipline) Değişiklikleri repoya pushladıktan sonra, pythonanywhere e gidip, terminalden yapılan değişiklikler tekrardan çekilip!!, app i reload etmek gerekiyor.

- pythonanywhere -> dashboard -> New console -> $Bash yeni sekmede açıyoruz.
- pythonanywhere deki bash terminalde;
- rm -rf ....   ile eskilerini siliyoruz. (README.txt kalıyor.)
```bash
rm -rf klkf.txt
```

- github taki deploye edeceğimiz reponun url ini kopyalıyoruz (clonelar gibi)
- pythonanywhere deki bash terminale;

```bash
git clone https://github.com/Umit8098/Project_Django_Rest_Framework_Rent_A_Car_App_CH-12.git
```

- project imizi pythonanywhere clonladık.
- terminalde ls komutuyla dosyaları görüyoruz,
- projemizin içine, manage.py dosyasıyla aynı seviyeye geliyoruz (cd komutuyla), yani ls komutunu çalıştırdığımızda manage.py ı görmemiz lazım.

- Türkiyede cloud platformlar çok kullanılmıyor, genelde Dedicated Server lar üzerinden işlemler yapılıyor. Tüm proje o server içerisinde oluyor. Servera girip, projeyi clonlama işlemi yapılıyor, veya pipeline kuruluyor (localde bir değişiklik yapıldı, github a pushlandı, merge oldu, development server ından bu değişikliğin algılanıp canlıda değişiklik yapılması...). Bunun için github hook ları var, bu hooklar ile işlem yapılıyor.  Bir değişiklik olduğunda github hookları takip ediliyor, değişiklik olduğunda trigger ediyor, o trigger ile server ınızda otomatik git pull yapıyor, değişiklikleri çekiyor, projeyi yeni şekliyle ayağa kaldırıyor.

- Localde iken yapmamız gereken işlemlerin aynısını yapıyoruz;
    - virtual environment oluşturuyoruz,
    - bazı eski versiyonlarda python 2. versiyonu gelebiliyor. Önce "python --version" ile kontrol edilip, eğer 2. versiyon geliyorsa "python3 --version" ile bir daha kontrol edip bu sefer 3. versiyonun geldiğini görüp, "python3 -m venv env" ile virtual environment oluşturuyoruz.
    - "source env/bin/activate" komutu ile env yi aktif hale getiriyoruz.(Bu ortam linux ortamı olduğu için windows kullanıcıları da ancak bu komutla env aktif hale getirebilir.)
    - projenin dependency lerini (bağımlılıklarını) kuruyoruz.

```bash
- python --version
- python3 --version
- python3 -m venv env  # python -m venv env 
- source env/bin/activate
- pip install -r requirements.txt
```

- Eğer paketlerden bir veya birkaçı için şöyle bir hata alınırsa;
```bash
No matching distribution found for Django==5.1.1 (from -r requirements.txt (line 3))
```

- Paketin upgrade versiyonunu yüklüyoruz. Bazen pythoneanywhere paketleri geriden takip edebiliyor. ugrade yapınca aslında bize göre önceki versiyonlarından ancak kendisine göre en güncel versiyonlarından birini yüklüyor.
```bash
- pip install django --upgrade
```

- Daha sonra pip freeze yapıp geri kalan paketleri manuel olarak versiyonları ile birlikte yükleyebiliriz.
```bash
- pip install crispy-bootstrap5==2024.2
- django-crispy-forms==2.3
```

  - pythonanywhere -> dashboard -> Web -> Add a new web app -> next -> Manual configuration (including virtualenvs) -> Python 3.10 (python versionu) -> next
        All done! Your web app is now set up. Details below. 
        (Hepsi tamam! Web uygulamanız artık kuruldu. Detaylar aşağıda.)
  - Artık app kuruldu ve app ile ilgili bir dashboard sundu bize. Burada manuel configurations lar yapacağız. 
        Bu site 28 Temmuz 2024 Pazar günü devre dışı bırakılacaktır. Buradan 3 ay daha app i çalıştırmak için bir button var.

- Şimdi yapacağımız işlemler -> 
  - Code:
        Source code: -> source codumuzu koyduğumuz yeri yazacağız.
        Working directory: -> source code ile aynı oluyor, bu directory de çalışacaksın diyoruz.  
        WSGI configuration file: -> manuel olarak update edeceğiz.
  - Virtualenv:
        Enter path to a virtualenv, if desired -> env nin nerede olduğunu göstereceğiz, yolunu vereceğiz.


- Source code: -> bash terminalde app in olduğu klasör içerisinde iken, "pwd" yazıp klasörün yolunu görebiliyoruz.
        /home/umit8107/Proj_WeatherApp-API-_Temp_Auth-2_email_CH-11_V.02
- Working directory: -> Source code kısmına yazdığımız yolu buraya da yazıyoruz.
        /home/umit8107/Proj_WeatherApp-API-_Temp_Auth-2_email_CH-11_V.02
- WSGI configuration file: Manuel configuration yaptığımız için bu WSGY (Web Server Gateway Interface) configuration u da kendimiz yapacağız. django application ile server arasındaki iletişimi sağlayan gateway. Bunda ayarlar yapmalıyız. sağ tıklayıp new tab ile yeni pencerede açıyoruz, Default olarak farmeworklerin ayar template leri var. 74-89 satırları arasında django kısmı var. Bunun haricindeki herşeyi siliyoruz, sadece django ile ilgili kısım kalıyor. İlk iki satır hariç yorumdan kurtarıyoruz.

```py
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

# assuming your django settings file is at '/home/umit8098/mysite/mysite/settings.py'
# and your manage.py is is at '/home/umit8098/mysite/manage.py'
path = '/home/umit8098/mysite'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

```

- path kısmında bize manage.py ın yolunu vermemizi istiyor. Aslında source code umuzun olduğu path, biraz önce "pwd" ile almıştık, "/home/umit8103/Project_Django_Rest_Framework_Stock_App_CH-13". Bunu path değişkenine tanımlıyoruz. Yani manage.py ımız bu klasörün içinde bunu söylüyoruz.

```py
path = '/home/umit8107/Proj_WeatherApp-API-_Temp_Auth-2_email_CH-11_V.02'
```

- os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'  -> settings klasörümüzün bulunduğu yeri belirtiyoruz. Bizim settings klasörümüz core in altında. buraya 'core.settings' yazıyoruz.

```py
os.environ['DJANGO_SETTINGS_MODULE'] = 'weather.settings'
```


- save ediyoruz.

- Virtualenv: env yolunu vermemiz lazım. Tekrar console a geri dönüyoruz, 
  - env nin olduğu dizne gidiyoruz. (ls yaptığımızda env yi görüyoruz.) 
  - "cd env/" ile env nin dizinine giriyoruz. 
  - pwd yazıp env nin path'ini yani yolunu kopyalıyoruz.
  - kopyaladığımız path i Virtualenv kısmındaki bölüme yazıp tik e tıklıyoruz. env miz de hazır.

```py
/home/umit8104/Project_Django_Rest_Framework_Rent_A_Car_App_CH-12/env
```


- Genel olarak ayarlarımız tamam ama birkaç ayar daha kaldı.
  - SECRET_KEY, DEBUG, ENV_NAME, DJANGO_LOG_LEVEL=INFO (bu projeye özel)
  - Bunları ayarlayacağımız yer Source code kısmındaki Go to directory. sağ tıklayarak yeni sekmede açıyoruz,
  - projemizde bu verileri tuttuğumuz yer .env file ı idi. Açılan sekmede Files kısmına .env yazıp New File oluşturuyoruz. bize .env isminde yeni bir file oluşturdu. manage.py, requirements.txt ile aynı seviyede.
  - Eğer dev, prod şeklinde env mizi ayırmadıysak sadece .env deki değişkenleri tanımlamamız yeterli.
  - Ancak env miz dev ve prod olarak ayrılmış ise -> 
    - SECRET_KEY tanımladık, 
    - DEBUG=True  (Önce True yazıyoruz, hataları görebilmek için. daha sonra False a çekebiliriz.)
    - settings klasörünün __init__.py daki env değişkeninin ismine ne verdiysek onu alıp .env file ında değişken ismi olarak kullanıyoruz. ENV_NAME
    - ENV_NAME=development  
        - prod ayarlarımızda db olarak postgresql var. bizim dev ayarlarını kullanmamız daha iyi. 
        - Ayrıca dev ayarlarını kullanırken de; debug.toolbar sadece localhost ta çalışıyor. Bu yüzden debug.toolbar ayarları ile development çalıştırılırsa hata verecektir. Bu hatayı almamak için dev.py daki debug.toolbar ayarlarını yoruma alıyoruz.
    - Bir de DJANGO_LOG_LEVEL=INFO ayarımız vardı onu da .env file ımıza ekliyoruz.

settings/dev.py
```py
from .base import *

# THIRD_PARTY_APPS = ["debug_toolbar"]

DEBUG = config("DEBUG")

# INSTALLED_APPS += THIRD_PARTY_APPS

# THIRD_PARTY_MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# MIDDLEWARE += THIRD_PARTY_MIDDLEWARE

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# INTERNAL_IPS = [
#     "127.0.0.1",
# ]
```


- .env dosyamızın en son hali -> 

.env
```py
SECRET_KEY=o_zoo)sc$ef3bbctpryhi7pz!i)@)%s!ffg_zsxd^n+z+h5=7i
DEBUG=True
ENV_NAME=development
DJANGO_LOG_LEVEL=INFO
```

- bash console a gidip db mizdeki tablolarımız oluşturacağız.
- (Biz projemizi github'a pushlarken db.sqlite3' yi de pushlamıştık. Yani db miz var. Eğer db'siz olarak github'a pushlayıp, oradan pythonanywhere'e deploye ediyorsak o zaman migrate ve superuser yapmamız gerekiyor.) 
- bash console da manage.py file ının bulunduğu dizine gidip db miz deki tablolarımızı oluşturuyoruz, superuser oluşturuyoruz,

```bash
python manage.py migrate
python manage.py createsuperuser
```

- dashboard a gidip Reload butonuna tıklıyoruz. Tüm değişiklikleri algılayacaktır. Daha sonra hemen bir üstte verdiği link ile projemizi pythonanywhere de yeni sekmede çalıştırıyoruz. 
- Bazen ALLOWED_HOSTS hatası veriyor. pythonanywher'e yüklediğimiz projenin settings.py'ına gidip ALLOWED_HOSTS = ['*'] şeklinde update/save ediyoruz ve tekrardan reload ediyoruz.
- admin panele giriyoruz,
- statics ler olmadan, css ler olmadan sayfamız geldi. 
- statics lerin görünmemesinin sebebi; django admin panel bir application ve bunun static file ları env içerisinde duruyor. Bunu localhost ta çalıştırdığımız zaman sıkıntı yaşamıyoruz ama canlı servera aldığımız zaman static root diye bir directory belirtmemiz gerekiyor. Static root, bütün environment ta olan static file ları veya application içerisinde varsa static file larımızı (css, javascript, image)  bunların hepsini tek bir klasör altında topluyor ve canlıdayken oradan çekiyor. Bu static ayarı nı yapmamız gerekiyor. Nasıl yapacağız;
- dashboard -> Source code -> Go to directory -> main -> settings -> base.py  içine STATİC_URL = 'static' altına STATIC_ROOT = BASE_DIR / 'static' yazıyoruz.

settings/base.py
```py
STATİC_URL = 'static'
STATIC_ROOT = BASE_DIR / 'static'
```

- base directory altında static isminde bir klasör oluştur, tüm static file ları bu static folder içerisinde topla demek için şu komutu (collectstatic) bash console da çalıştırıyoruz;

```bash
python manage.py collectstatic
```
- bu komut çalıştırıldıktan sonra; 197 adet static file kopyalandı ve belirttiğimiz folder altında toplandı.
" 162 static files copied to '/home/umit8104/Project_Django_Rest_Framework_Rent_A_Car_App_CH-12/static'. "

- Şimdi dashboarda gidip, web kısmında Static files: kısmında URL altında URL ini (/static/),  ve Directory altında path ini giriyoruz. (path ini zaten bize vermişti -> 197 static files cop..... kısmının sonunda. (/home/umit8098/Project_Django_Rest_Framework_Stock_App/core/static))
- girdikten sonra ✔ işareti ile kaydetmeliyiz.
  
```py
/static/
/home/umit8098/Project_Django_Rest_Framework_Stock_App/core/static
```

- Bu işlemi yaptıktan sonra değişikliklerin algılanması için tekrardan Reload butonuna tıklıyoruz. Artık sayfalarımızın statics leri de geliyor.

 - Şuanda backend projesi deploye edildi. Eğer bu backend için bir frontend yazılmış ise deploye edilmiş projenin endpointlerine istek atması gerekir. Mesela frontend kısmı React ile yazılmışsa istek atılacak endpointler düzenlenip netlify'a deploye edilip, oradan çalıştırılması daha uygun olur. 