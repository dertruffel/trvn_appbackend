from django import forms
from django.forms import ModelForm

from .models import Car, Post, Contact, Comment


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

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, error_messages={'required': 'Please enter a name'})
    email = forms.EmailField(required=True, error_messages={'required': 'Please enter an email'})
    message = forms.CharField(widget=forms.Textarea, required=True, error_messages={'required': 'Please enter a message'})

    def save(self, commit=True):
        try:
            contact = Contact(
                name=self.cleaned_data['name'],
                email=self.cleaned_data['email'],
                message=self.cleaned_data['message'],
            )
            if commit:
                contact.save()
            return contact
        except Exception as e:
            print(e)
            return None

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')

class CommentForm(forms.Form):
    comment = forms.CharField(max_length=100, required=True, error_messages={'required': 'Please enter a comment'})



    class Meta:
        model = Comment
        fields = ('comment',)