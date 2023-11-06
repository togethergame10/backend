from django import forms

from game.models import Game


class GameCreationForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title','minHeadcount', 'maxHeadcount',
                  'preparation', 'explanation', 'tip', 'image']

