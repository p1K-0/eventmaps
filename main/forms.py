from django import forms
from django.forms import TextInput
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    #def __init__(self, *args, **kwargs):
    #    super(LoginForm, self).__init__(*args, **kwargs)
    #    self.fields['username'].widget = TextInput(attrs={'class': 'auth-input'})
    #    self.fields['password'].widget = TextInput(attrs={'class': 'auth-input'})
            #'id': 'myCustomId',

            #'name': 'myCustomName',
            #'placeholder': 'myCustomPlaceholder'})


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Повторение пароля')
    address = forms.CharField()
    phone = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'last_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

