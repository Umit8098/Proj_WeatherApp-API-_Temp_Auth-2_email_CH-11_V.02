<!-- Please update value in the {}  -->

<h1 align="center">Project_Django_Template_Weather_App</h1>


<div align="center">
  <h3>
    <a href="https://umit8108.pythonanywhere.com/">
      Demo
    </a>
     | 
    <a href="https://umit8108.pythonanywhere.com/">
      Project
    </a>
 
  </h3>
</div>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Built With](#built-with)
- [How To Use](#how-to-use)
- [About This Project](#about-this-project)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

<!-- OVERVIEW -->

## Overview
- Weather App
![screenshot](project_screenshot/Weather_App_Temp.gif)

---

## Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->

- Django Templates
- JavaScript
- Bootstrap5
- HTML
- CSS

## How To Use

<!-- This is an example, please update according to your application -->

To clone and run this application, you'll need [Git](https://github.com/Umit8098/Proj_WeatherApp-API-_Temp_Auth-2_email_CH-11_V.04)

When installing the required packages in the requirements.txt file, review the package differences for windows/macOS/Linux environments. 

Complete the installation by uncommenting the appropriate package.

---

requirements.txt dosyasındaki gerekli paketlerin kurulumu esnasında windows/macOS/Linux ortamları için paket farklılıklarını inceleyin. 

Uygun olan paketi yorumdan kurtararak kurulumu gerçekleştirin.

```bash
# Clone this repository
$ git clone https://github.com/Umit8098/Proj_WeatherApp-API-_Temp_Auth-2_email_CH-11_V.04.git

# Install dependencies
    $ python -m venv env
    $ python3 -m venv env (for macOs/linux OS)
    $ env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt
    $ python manage.py migrate (for win OS)
    $ python3 manage.py migrate (for macOs/linux OS)

# Create and Edit .env
# Add Your SECRET_KEY in .env file

"""
# example .env;

SECRET_KEY =123456789abcdefg...

# API Key to retrieve data from https://openweathermap.org
# Obtained by registration at https://openweathermap.org
API_KEY =123456789abcdefg...
"""

# Run the app
    $ python manage.py runserver
```

## About This Project
- It is a Fullstack weather application prepared with the Django Framework template structure and using https://openweathermap.org/ APIs.

<hr>

- Django Framework şablon yapısıyla hazırlanmış, https://openweathermap.org/ API'lerini kullanan Fullstack bir hava durumu uygulamasıdır.

## Acknowledgements
- [Bootstrap5](https://getbootstrap.com/) - Projede kullanılan CSS framework'ü.
- [crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Projede kullanılan formların CSS framework'ü.
- [openweathermap API's](https://openweathermap.org/) - API's.

## Contact

<!-- - Website [your-website.com](https://{your-web-site-link}) -->
- GitHub [@Umit8098](https://github.com/Umit8098)

- Linkedin [@umit-arat](https://linkedin.com/in/umit-arat/)
<!-- - Twitter [@your-twitter](https://{twitter.com/your-username}) -->
