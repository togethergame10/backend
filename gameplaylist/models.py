from django.db import models

# Create your models here.
from account.models import User
from game.models import Game


class GamePlaylist(models.Model):
    title = models.CharField(max_length=30, null=False)
    games = models.ManyToManyField(Game, null=True)
    author = author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='posted_gamelist')
    created_at = models.DateField(auto_now_add=True)
    #modified_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/gamelist/", null=True, blank=True)
    collectors = models.ManyToManyField(User, null=True,blank=True, related_name='collected_gamelist')

    def __str__(self):
        return f'{self.title}'


