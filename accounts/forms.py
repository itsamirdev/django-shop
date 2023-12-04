from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from accounts.models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='confirm password')

    class Meta:
        model = User
        fields = ("email", "full_name", "phone_number")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('Passwords don\'t match')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="you can change your password using <a href=\"../password/\">this form</a>")

    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'email', 'password', 'last_login']


class UserRegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput, label='email')
    phone_number = forms.CharField(max_length=11, label='phone number')
    full_name = forms.CharField(label='full name')
    password = forms.CharField(widget=forms.PasswordInput, label='password')

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError('this email is already exists')
        return self.cleaned_data['email']

    def clean_phone_number(self):
        if User.objects.filter(phone_number=self.cleaned_data['phone_number']).exists():
            raise ValidationError('this phone number is already exists')
        return self.cleaned_data['phone_number']


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField()
