from django import forms

from gameplaylist.models import GamePlaylist
from django.forms import ModelForm, TextInput


class GamePlaylistCreationForm(forms.ModelForm):
    class Meta:
        model = GamePlaylist
        fields = ['title', 'image']
        widgets = {
            'title': TextInput(attrs={
                'id': "playlistName",
                'placeholder': '제목을 입력하세요'
            }),
        }

