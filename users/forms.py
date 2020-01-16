from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                             'placeholder': 'your unique login'
                                                                             }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'example@mail.com'
                                                            }))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                    'placeholder': 'password'
                                                                                    }))
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                            'placeholder': 'password'
                                                                                            }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                             'placeholder': 'your unique login'
                                                                             }))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                   'placeholder': 'password'
                                                                                   }))
