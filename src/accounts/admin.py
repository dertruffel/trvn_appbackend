from django.contrib import admin
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _
# Register your models here.

from .models import User



class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_('Passwords do not match.'))
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label=(_('Password')),
                                         help_text=("Raw passwords are not stored, "
                                                    "so there is no way to see "
                                                    "this user's password, "
                                                    "but you can change the password "
                                                    "using <a href=\"../password/\">"
                                                    "this form</a>."))

    class Meta:
        model = User
        fields = ('email', 'password', 'is_active', 'is_superuser',)
        readonly_fields = ('created_at', 'updated_at')

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'is_superuser',
                    'is_staff', 'is_admin', 'is_email_verified')
    list_filter = ('is_superuser', 'is_staff', 'is_admin', 'is_active', 'is_email_verified')
    fieldsets = (
        (_('Personal info'), {'fields': ('email', 'password', 'phone_number', 'first_name', 'last_name', 'username')}),

        (_('Permissions'), {'fields': (
            'is_active', 'is_email_verified', 'is_superuser', 'is_staff', 'is_admin', 'jwt_secret',

        )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)