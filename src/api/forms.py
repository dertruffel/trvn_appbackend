from django import forms
from django.forms import ModelForm

from .models import Car, Post


class PostForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ('title', 'description', 'image')

    def save(self, commit=True):
        post = Post(
            title=self.cleaned_data['title'],
            description=self.cleaned_data['description'],
            image=self.cleaned_data['image'],
        )
        if commit:
            post.save()
        return post

class CarForm(ModelForm):
    image = forms.ImageField(required=False, error_messages={'required': 'Please upload an image'})
    name = forms.CharField(max_length=100, required=True, error_messages={'required': 'Please enter a name'})
    description = forms.CharField(max_length=1000, required=True, error_messages={'required': 'Please enter a description'})
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=True, error_messages={'required': 'Please enter a price'})
    for_sale = forms.BooleanField(required=False)

    class Meta:
        model = Car
        fields = ('name', 'price', 'description', 'image', 'for_sale')

    def save(self, commit=True):
        try:
            car = Car(
                name=self.cleaned_data['name'],
                description=self.cleaned_data['description'],
                price=self.cleaned_data['price'],
                for_sale=self.cleaned_data['for_sale'],
            )
            if commit:
                car.save()
            return car
        except Exception as e:
            print(e)
            return None

class ChangeCarPriceForm(ModelForm):
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=True, error_messages={'required': 'Please enter a price'})

    class Meta:
        model = Car
        fields = ('price',)
