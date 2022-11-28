#signup form
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from api.models import Car


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

class CarForm(ModelForm):
    image = forms.ImageField(required=False, error_messages={'required': 'Please upload an image'})
    name = forms.CharField(max_length=100, required=True, error_messages={'required': 'Please enter a name'})
    description = forms.CharField(max_length=1000, required=True, error_messages={'required': 'Please enter a description'})
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=True, error_messages={'required': 'Please enter a price'})

    class Meta:
        model = Car
        fields = ('name', 'price', 'description', 'image')

    def save(self, commit=True):
        try:
            car = Car(
                name=self.cleaned_data['name'],
                description=self.cleaned_data['description'],
                price=self.cleaned_data['price'],
            )
            if commit:
                car.save()
            return car
        except Exception as e:
            print(e)
            return None