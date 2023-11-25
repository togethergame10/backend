from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

def hp_validator(value):
    if len(str(value)) != 10:
        raise forms.ValidationError('정확한 핸드폰 번호를 입력해주세요.')

def student_id_validator(value):
    if len(str(value)) != 8:
        raise forms.ValidationError('본인의 학번 8자리를 입력해주세요.')


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='비밀번호 확인', widget=forms.PasswordInput)
    email = forms.CharField(max_length=100, label="이메일")
    nickname = forms.CharField(max_length=100, label="닉네임")


    class Meta:
        model = User
        fields = ('email', 'nickname')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("패스워드가 일치하지 않습니다.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'nickname',
                  'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]