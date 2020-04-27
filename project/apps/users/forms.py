from django import forms

from .models import EdenUser


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = EdenUser
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Имя пользователя'
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Повторите пароль'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['email'].label = 'Почта'

    def clean(self):
        username = self.cleaned_data['username']
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        email = self.cleaned_data['email']
        if EdenUser.objects.filter(username=username).exists():
            raise forms.ValidationError('Логин занят')
        if EdenUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Данная почта уже зарегистрирована')
        if password1 != password2:
            raise forms.ValidationError('Ваши пароли не совпадают')