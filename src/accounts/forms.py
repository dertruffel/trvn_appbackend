#signup form
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth import get_user_model
User = get_user_model()



class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class SignInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

