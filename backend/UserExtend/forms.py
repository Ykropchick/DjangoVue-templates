from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from .models import User


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="пароль", widget=forms.TextInput(
        attrs={'class': "from-input", "placeholder": "Введите пароль"}))
    password2 = forms.CharField(label="повторите пароль", widget=forms.TextInput(
        attrs={'class': "from-input", "placeholder": "Повторите пароль"}))

    class Meta:
        model = User
        fields = ['username', 'phone', 'avatar', "approved", "banned"]

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 is not None and password1 != password2:
            self.add_error("password2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password1 in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password1 = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = "__all__"