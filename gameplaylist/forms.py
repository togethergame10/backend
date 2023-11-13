from django import forms

from gameplaylist.models import GamePlaylist


class GamePlaylistCreationForm(forms.ModelForm):
    class Meta:
        model = GamePlaylist
        fields = ['title', 'image']

