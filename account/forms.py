from django.contrib.auth.forms import UserCreationForm
from django import forms
from account.models import User


class AccountCreateForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    nickname = forms.CharField(label="닉네임")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "nickname", "email")


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True