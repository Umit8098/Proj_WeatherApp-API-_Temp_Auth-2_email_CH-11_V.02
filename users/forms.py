from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm

# unique email için;
from django.core.exceptions import ValidationError

#! email ile giriş yapabilmek için;
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


class UserForm(UserCreationForm):
    class Meta():
      model = User
      fields = ('username', 'email')
      
    # unique email için;
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():  # CustomUser kullanıyorsanız bunu da değiştirin
            raise ValidationError("Bu e-posta adresi zaten kullanılıyor.")
        return email


class UserProfileForm(forms.ModelForm):
    class Meta:
      model = UserProfile
      # fields = '__all__'
      exclude = ('user',)
      help_texts = {
            'portfolio': 'Lüften url giriniz..',
        }
      widgets = {
            'portfolio': forms.TextInput(attrs={
                'placeholder': 'url giriniz..',
            }),
        }


#! email ile giriş yapabilmek için;
class EmailAuthenticationForm(AuthenticationForm):

    username = forms.EmailField(label="Email")  # E-posta alanı kullan

    def clean(self):
        email = self.cleaned_data.get('username')  # Form'daki "username" alanını email olarak kabul ediyoruz
        password = self.cleaned_data.get('password')

        if email and password:
            try:
                # E-posta ile kullanıcıyı bul
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("Bu e-posta ile bir kullanıcı bulunamadı.")
            
            # Bulunan kullanıcının kullanıcı adını (username) authenticate'e gönderiyoruz
            self.user_cache = authenticate(self.request, username=user.username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Geçersiz e-posta veya şifre.")
        
        return self.cleaned_data

    def get_user(self):
        return self.user_cache